#!/usr/bin/env bash
# Single quality gate for all course material (issue #25).
#
#   scripts/check_materials.sh
#
# Does two things, in order:
#   1. Lint  — nbqa flake8 over every notebook in day*/ (repo-root .flake8)
#   2. Execute — every OFFLINE module's notebooks, top to bottom, in a clean
#      environment built from the pinned uv.lock (offline stack + the
#      transitional v1-legacy group, since the v1 modules still in
#      day1/–day3/ use xgboost/shap).
#
# Kaggle GPU modules are intentionally OUT of scope here — they are validated
# manually on Kaggle; see the "ก่อนวันอบรม" checklist in README.md.
#
# Knobs (environment variables):
#   KAGGLE_MODULES  space-separated module dir names to skip (v2 GPU modules
#                   get added here when they land; empty for now — every v1
#                   module is offline)
#   NB_TIMEOUT      per-notebook execution timeout in seconds (default 600)
#   CHECK_ENV       path of the scratch environment (default .check-env)
#
# Requirements: bash, uv (https://docs.astral.sh/uv/). Run from anywhere.

set -euo pipefail
cd "$(dirname "$0")/.."

CHECK_ENV="${CHECK_ENV:-.check-env}"
NB_TIMEOUT="${NB_TIMEOUT:-600}"
# v2 GPU modules that land with their material; extend as the next one follows.
KAGGLE_MODULES="${KAGGLE_MODULES:-module3_thai_sentiment_mbert module4_esc50_cnn module5_kws_demucs_asr}"

NBQA="$CHECK_ENV/bin/nbqa"
JUPYTER="$CHECK_ENV/bin/jupyter"

failures=()

note()  { printf '\n\033[1;34m== %s\033[0m\n' "$*"; }
ok()    { printf '  \033[0;32mPASS\033[0m %s\n' "$*"; }
fail()  { printf '  \033[0;31mFAIL\033[0m %s\n' "$*"; failures+=("$*"); }

# ---------------------------------------------------------------------------
note "[0/2] Clean check environment ($CHECK_ENV)"
# A dedicated env so the developer's .venv is never touched and the check
# always runs against exactly what uv.lock pins.
UV_PROJECT_ENVIRONMENT="$CHECK_ENV" uv sync --frozen --quiet
ok "uv sync --frozen -> $CHECK_ENV"

# ---------------------------------------------------------------------------
note "[1/2] flake8 via nbqa (repo-root .flake8)"
lint_failed=0
day_dirs=()
for d in day*/; do [ -d "$d" ] && day_dirs+=("$d"); done
if [ "${#day_dirs[@]}" -eq 0 ]; then
    fail "no day*/ directories found"
    lint_failed=1
elif "$NBQA" flake8 "${day_dirs[@]}"; then
    ok "nbqa flake8 ${day_dirs[*]}"
else
    fail "nbqa flake8 (see output above)"
    lint_failed=1
fi

# ---------------------------------------------------------------------------
note "[2/2] Execute offline modules (allow_errors only for exercise/background notebooks)"
exec_failed=0
# Intentional placeholder/teaching-error notebooks are executed with
# allow_errors=True; everything else must run strictly (allow_errors=False).
ALLOW_PATTERNS='(exercise|background)\.ipynb$'

for module_dir in day*/module*/; do
    mod_name="$(basename "$module_dir")"
    skip=0
    for k in $KAGGLE_MODULES; do
        [ "$k" = "$mod_name" ] && skip=1
    done
    if [ "$skip" -eq 1 ]; then
        printf '  --skip %s (Kaggle GPU — manual validation, see README)\n' "$mod_name"
        continue
    fi
    for nb in "$module_dir"*.ipynb; do
        [ -f "$nb" ] || continue
        if echo "$nb" | grep -Eq "$ALLOW_PATTERNS"; then
            allow="--ExecutePreprocessor.allow_errors=True"
        else
            allow="--ExecutePreprocessor.allow_errors=False"
        fi
        if "$JUPYTER" nbconvert --to notebook --execute --stdout \
                --ExecutePreprocessor.timeout="$NB_TIMEOUT" $allow \
                "$nb" > /dev/null 2>"$CHECK_ENV/nbconvert.log"; then
            ok "$nb"
        else
            fail "$nb"
            sed -n '1,15p' "$CHECK_ENV/nbconvert.log" | sed 's/^/       /'
            exec_failed=1
        fi
    done
done

# ---------------------------------------------------------------------------
note "Summary"
[ "$lint_failed" -eq 0 ] && ok "lint" || fail "lint"
[ "$exec_failed" -eq 0 ] && ok "execution" || fail "execution"
if [ "${#failures[@]}" -gt 0 ]; then
    printf '\nFailed items:\n'
    printf '  - %s\n' "${failures[@]}"
    exit 1
fi
printf '\nAll material checks passed.\n'
