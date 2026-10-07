#!/usr/bin/env python3
"""Generate synthetic Thai metrology calibration-report scan pages.

สร้างภาพหน้ากระดาษจำลอง (synthetic scan) ของใบรับรองการสอบเทียบภาษาไทย
จากห้องปฏิบัติการสมมติ เพื่อใช้เป็นสื่อการเรียนรู้สำหรับโมดูล OCR ภาษาไทย
และโครงงานปลายทางของคอร์ส เนื้อหาทั้งหมดสมมติขึ้นเอง ไม่อ้างอิงหน่วยงานจริง

Usage:
    python tools/generate_measurement_reports.py [--outdir DIR] [--seed N]

Output: A4-ratio PNG pages (1240 x 1754 px) with subtle scan realism
(slight rotation, faint noise, light margin shading) written to
datasets/measurement_reports/ by default.

Dependencies: stdlib + numpy + Pillow + matplotlib (deterministic seed).
"""

import argparse
import io
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

PAGE_W = 1240
PAGE_H = 1754
MARGIN = 70
CONTENT_W = PAGE_W - 2 * MARGIN

INK = (25, 25, 28)
INK_SOFT = (75, 75, 82)
GRID = (120, 120, 130)
HEAD_BG = (232, 233, 236)
PAPER = (255, 255, 255)

# (font path, face index for body text, face index for bold text)
FONT_CANDIDATES = [
    ("/System/Library/Fonts/Supplemental/SukhumvitSet.ttc", 2, 5),
    ("/System/Library/Fonts/Supplemental/Thonburi.ttc", 0, 0),
    ("/System/Library/Fonts/NotoSansThai.ttc", 0, 0),
]

# Thai combining marks (must never be split from their base character
# when hard-wrapping a long unspaced Thai run).
COMBINING = set(
    "ัิีึืฺุู"
    "็่้๊๋์ํ๎"
)

ORG_NAME = "ห้องปฏิบัติการเทคนิคพื้นฐาน"
ORG_PARENT = "ศูนย์มาตรฐานอุตสาหกรรมตัวอย่าง"
ORG_ADDR = "88/9 ถนนสาทรใต้ แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500"
ORG_CONTACT = "โทร. 0 2101 2345  |  calib@example-lab.co.th"
REPORT_NO = "2568/0107"
REPORT_ISSUED = "15 มกราคม 2568"
REPORT_EXPIRY = "15 มกราคม 2569"
TOTAL_PAGES = 6

# Calibration points of a digital thermometer (bath reference value,
# instrument reading error, expanded uncertainty with k = 2).
POINTS = [-50, -30, -10, 0, 20, 40, 60, 100, 150, 200]
STD_VALS = [-50.02, -30.04, -10.03, 0.01, 20.02, 40.00, 60.03,
            100.01, 150.02, 200.00]
ERRORS = [-0.03, 0.02, 0.04, -0.01, 0.02, 0.03, -0.02, 0.05, 0.04, -0.03]
UNCERTS = [0.05, 0.05, 0.05, 0.04, 0.04, 0.04, 0.05, 0.06, 0.07, 0.08]

REPEAT_POINTS = [0.01, 40.00, 100.01, 200.00]
REPEAT_READS = [
    [0.00, 0.02, 0.01],
    [40.01, 39.99, 40.00],
    [100.05, 100.07, 100.04],
    [199.98, 200.01, 199.97],
]

_FONT_PATH = None
_FONT_BODY = 0
_FONT_BOLD = 0
_FONT_CACHE = {}


def find_repo_root():
    """Walk up from this file until requirements-offline.txt is found."""
    here = Path(__file__).resolve().parent
    for cand in (here, *here.parents):
        if (cand / "requirements-offline.txt").exists():
            return cand
    raise SystemExit(
        "could not locate repo root (requirements-offline.txt not found)"
    )


def resolve_font():
    """Pick the first loadable Thai font and remember its face indices."""
    global _FONT_PATH, _FONT_BODY, _FONT_BOLD
    for path, body_idx, bold_idx in FONT_CANDIDATES:
        try:
            ImageFont.truetype(path, 20, index=body_idx)
            ImageFont.truetype(path, 20, index=bold_idx)
        except OSError:
            continue
        _FONT_PATH = path
        _FONT_BODY = body_idx
        _FONT_BOLD = bold_idx
        return path
    raise SystemExit("no loadable Thai font found on this system")


def font(size, bold=False):
    """Return a cached Sukhumvit/Thonburi font face at the given size."""
    idx = _FONT_BOLD if bold else _FONT_BODY
    key = (size, idx)
    if key not in _FONT_CACHE:
        _FONT_CACHE[key] = ImageFont.truetype(_FONT_PATH, size, index=idx)
    return _FONT_CACHE[key]


def is_combining(ch):
    return ch in COMBINING


def wrap_text(draw, text, f, max_w):
    """Greedy word wrap; hard-break overlong Thai runs between syllable
    boundaries without separating a combining mark from its base."""
    lines = []
    cur = ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
            continue
        if cur:
            lines.append(cur)
        cur = word
        while draw.textlength(cur, font=f) > max_w:
            cut = len(cur)
            while cut > 1 and draw.textlength(cur[:cut], font=f) > max_w:
                cut -= 1
            while cut > 1 and is_combining(cur[cut]):
                cut -= 1
            lines.append(cur[:cut])
            cur = cur[cut:]
    if cur:
        lines.append(cur)
    return lines


def draw_par(draw, x, y, text, size=20, width=CONTENT_W, bold=False,
             fill=INK, leading=1.55):
    """Draw a wrapped paragraph; return the y coordinate below it."""
    f = font(size, bold)
    step = int(size * leading)
    for line in wrap_text(draw, text, f, width):
        draw.text((int(x), int(y)), line, font=f, fill=fill)
        y += step
    return y


def draw_centered(draw, y, text, size, bold=False, fill=INK):
    f = font(size, bold)
    w = draw.textlength(text, font=f)
    draw.text((int((PAGE_W - w) / 2), int(y)), text, font=f, fill=fill)
    return y + int(size * 1.5)


def draw_section(draw, x, y, text):
    """Bold section heading with a rule underneath."""
    draw.text((x, y), text, font=font(24, bold=True), fill=INK)
    y += 36
    draw.line([(x, y), (x + CONTENT_W, y)], fill=INK, width=2)
    return y + 16


def draw_table(draw, x, y, headers, rows, widths, aligns=None, size=19):
    """Bordered table; headers may be None for a label/value table.
    Returns the y coordinate below the table."""
    if aligns is None:
        aligns = ["left"] * len(widths)
    hf = font(size, bold=True)
    bf = font(size)
    pad = 10
    line_h = int(size * 1.5)
    maxw = [w - 2 * pad for w in widths]
    if headers is None:
        head_cells = None
        head_h = 0
    else:
        head_cells = [wrap_text(draw, h, hf, mw)
                      for h, mw in zip(headers, maxw)]
        head_h = max(len(c) for c in head_cells) * line_h + 2 * pad
    body_cells = [[wrap_text(draw, c, bf, mw)
                   for c, mw in zip(row, maxw)] for row in rows]
    row_hs = [max(len(c) for c in cells) * line_h + 2 * pad
              for cells in body_cells]
    total_h = head_h + sum(row_hs)
    total_w = sum(widths)

    draw.rectangle([x, y, x + total_w, y + total_h], fill=PAPER,
                   outline=GRID, width=1)
    if head_cells is not None:
        draw.rectangle([x, y, x + total_w, y + head_h], fill=HEAD_BG,
                       outline=GRID, width=1)

    def put_cell(cx, cy, cw, lines, f, align):
        block_h = len(lines) * line_h
        ty = cy + (row_cell_h - block_h) // 2 + pad // 2
        for line in lines:
            tw = draw.textlength(line, font=f)
            if align == "center":
                tx = cx + (cw - tw) / 2
            elif align == "right":
                tx = cx + cw - pad - tw
            else:
                tx = cx + pad
            draw.text((int(tx), int(ty)), line, font=f, fill=INK)
            ty += line_h

    yy = y
    if head_cells is not None:
        for i, lines in enumerate(head_cells):
            row_cell_h = head_h
            put_cell(x + sum(widths[:i]), y, widths[i], lines, hf, "center")
    for ri, cells in enumerate(body_cells):
        row_cell_h = row_hs[ri]
        ry = y + head_h + sum(row_hs[:ri])
        for i, lines in enumerate(cells):
            put_cell(x + sum(widths[:i]), ry, widths[i], lines, bf,
                     aligns[i])

    yy = y
    draw.line([(x, yy), (x + total_w, yy)], fill=GRID, width=1)
    for rh in ([head_h] if head_cells is not None else []) + row_hs:
        yy += rh
        draw.line([(x, yy), (x + total_w, yy)], fill=GRID, width=1)
    xx = x
    for w in widths:
        draw.line([(xx, y), (xx, y + total_h)], fill=GRID, width=1)
        xx += w
    draw.line([(x + total_w, y), (x + total_w, y + total_h)],
              fill=GRID, width=1)
    return y + total_h + 22


def draw_caption(draw, y, text):
    return draw_par(draw, MARGIN, y, text, size=18, fill=INK_SOFT,
                    leading=1.45)


def draw_running_header(draw):
    f = font(17)
    draw.text((MARGIN, 32), f"{ORG_NAME} {ORG_PARENT}", font=f,
              fill=INK_SOFT)
    right = f"เลขที่รายงาน: {REPORT_NO}"
    w = draw.textlength(right, font=f)
    draw.text((PAGE_W - MARGIN - int(w), 32), right, font=f, fill=INK_SOFT)
    draw.line([(MARGIN, 58), (PAGE_W - MARGIN, 58)], fill=GRID, width=1)


def draw_footer(draw, page_no):
    y = PAGE_H - 74
    draw.line([(MARGIN, y), (PAGE_W - MARGIN, y)], fill=GRID, width=1)
    f = font(17)
    draw.text((MARGIN, y + 10), f"ใบรับรองการสอบเทียบ เลขที่ {REPORT_NO}",
              font=f, fill=INK_SOFT)
    text = f"หน้า {page_no} จาก {TOTAL_PAGES}"
    w = draw.textlength(text, font=f)
    draw.text((int((PAGE_W - w) / 2), y + 10), text, font=f, fill=INK_SOFT)


def new_page():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    return img, ImageDraw.Draw(img)


def render_error_plot():
    """Error-vs-point plot with uncertainty bars, drawn with matplotlib
    using the same Thai font as the page text."""
    font_manager.fontManager.addfont(_FONT_PATH)
    family = font_manager.FontProperties(fname=_FONT_PATH).get_name()
    old = plt.rcParams["font.family"]
    plt.rcParams["font.family"] = family
    try:
        fig, ax = plt.subplots(figsize=(6.6, 3.0), dpi=200)
        ax.errorbar(POINTS, ERRORS, yerr=UNCERTS, fmt="o-",
                    color="#1a4f8a", ecolor="#9a9aa2", elinewidth=1.1,
                    capsize=3, ms=4.5, linewidth=1.2)
        ax.axhline(0.10, color="#b23a2f", linestyle="--", linewidth=1.0)
        ax.axhline(-0.10, color="#b23a2f", linestyle="--", linewidth=1.0)
        ax.text(5, 0.115, "เกณฑ์การยอมรับ ± 0.10 °C", fontsize=9,
                color="#b23a2f")
        ax.set_xlabel("จุดทดสอบ (°C)", fontsize=10)
        ax.set_ylabel("ข้อผิดพลาด (°C)", fontsize=10)
        ax.set_title("ข้อผิดพลาดของการอ่านค่าเทียบกับจุดทดสอบ",
                     fontsize=11)
        ax.set_xticks(POINTS)
        ax.set_ylim(-0.25, 0.25)
        ax.grid(alpha=0.3)
        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format="png", facecolor="white")
        plt.close(fig)
    finally:
        plt.rcParams["font.family"] = old
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def build_page_1():
    """Letterhead, report/tool identity, reference-standard table."""
    img, d = new_page()
    y = draw_centered(d, 78, ORG_NAME, 34, bold=True)
    y = draw_centered(d, y - 6, ORG_PARENT, 26, bold=True)
    y = draw_centered(d, y + 2, ORG_ADDR, 18, fill=INK_SOFT)
    y = draw_centered(d, y - 6, ORG_CONTACT, 18, fill=INK_SOFT)
    y += 10
    d.line([(MARGIN, y), (PAGE_W - MARGIN, y)], fill=INK, width=3)
    d.line([(MARGIN, y + 5), (PAGE_W - MARGIN, y + 5)], fill=INK, width=1)
    y += 30
    y = draw_centered(d, y, "ใบรับรองการสอบเทียบ", 28, bold=True)
    y = draw_centered(d, y - 8, "CERTIFICATE OF CALIBRATION", 19,
                      fill=INK_SOFT)
    y += 16
    d.line([(MARGIN, y), (PAGE_W - MARGIN, y)], fill=GRID, width=1)
    y += 26

    y = draw_table(
        d, MARGIN, y, None,
        [["เลขที่รายงานการสอบเทียบ", REPORT_NO],
         ["วันที่ออกรายงาน", REPORT_ISSUED],
         ["วันหมดอายุการรับรอง", REPORT_EXPIRY],
         ["ผู้ส่งตรวจ", "บริษัท วิศวกรรมตัวอย่าง จำกัด"]],
        [400, 700], aligns=["left", "left"], size=20)

    y = draw_section(d, MARGIN, y, "ข้อมูลเครื่องมือที่ส่งมอบสอบเทียบ")
    y = draw_table(
        d, MARGIN, y, None,
        [["ชื่อเครื่องมือ", "เครื่องวัดอุณหภูมิแบบดิจิทัล"],
         ["รุ่น / Model", "TM-946"],
         ["หมายเลขประจำเครื่อง / Serial No.", "SN-2024-08817"],
         ["ผู้ผลิต", "Example Instruments Co., Ltd."],
         ["ช่วงการใช้งาน", "-50 ถึง 200 °C"],
         ["ความละเอียดในการอ่านค่า", "0.01 °C"]],
        [400, 700], aligns=["left", "left"], size=20)

    y = draw_section(d, MARGIN, y,
                     "รายละเอียดเครื่องมือมาตรฐานอ้างอิง")
    y = draw_table(
        d, MARGIN, y,
        ["อุปกรณ์อ้างอิง", "เลขประจำเครื่อง", "การสอบเทียบล่าสุด",
         "หน่วยงานที่สอบเทียบ"],
        [["เทอร์มิสเตอร์มาตรฐาน", "RT-90375", "3 มิถุนายน 2567",
          "ห้องปฏิบัติการตัวอย่าง ก"],
         ["โพรเบอร์อุณหภูมิแบบจุ่ม", "PT-11842", "21 กรกฎาคม 2567",
          "ห้องปฏิบัติการตัวอย่าง ข"],
         ["เครื่องอ่านค่าความต้านทาน", "BR-55210", "9 กันยายน 2567",
          "ห้องปฏิบัติการตัวอย่าง ก"]],
        [300, 190, 300, 310], size=19)
    draw_caption(d, y, "ตารางที่ 1 รายการเครื่องมือมาตรฐานอ้างอิงที่ใช้"
                       "ในการสอบเทียบครั้งนี้")
    draw_footer(d, 1)
    return img


def build_page_2():
    """Ambient conditions table + numbered test-method paragraphs."""
    img, d = new_page()
    draw_running_header(d)
    y = 96

    y = draw_section(d, MARGIN, y, "สภาพแวดล้อมระหว่างการทดสอบ")
    y = draw_table(
        d, MARGIN, y,
        ["พารามิเตอร์", "ค่าระหว่างการทดสอบ", "ช่วงที่ควบคุมไว้"],
        [["อุณหภูมิ (°C)", "24.6", "23 ± 2"],
         ["ความชื้นสัมพัทธ์ (%RH)", "52", "45 - 60"],
         ["ความดันบรรยากาศ (hPa)", "1008.2", "ไม่ได้ควบคุม"]],
        [420, 340, 340],
        aligns=["left", "center", "center"], size=20)
    y = draw_caption(d, y, "ตารางที่ 2 สภาพแวดล้อมขณะดำเนินการทดสอบ"
                           " วัดโดยเครื่องบันทึกสภาพแวดล้อมของห้อง"
                           "ปฏิบัติการ")
    y += 16

    y = draw_section(d, MARGIN, y, "วิธีการทดสอบ")
    items = [
        "1. เครื่องมือที่ส่งมอบตรวจได้รับการตรวจสอบสภาพภายนอกแล้ว พบว่า"
        "อยู่ในสภาพสมบูรณ์ ไม่มีร่องรอยความเสียหายที่ส่งผลต่อการใช้งาน"
        "หรือผลการสอบเทียบ",
        "2. การสอบเทียบดำเนินการโดยวิธีเปรียบเทียบโดยตรง คือเทียบค่า"
        "การอ่านของเครื่องมือกับค่าที่ได้จากเทอร์มิสเตอร์มาตรฐานในอ่าง"
        "อุณหภูมิคงที่ ณ จุดทดสอบตามที่ปรากฏในตารางผลการสอบเทียบ",
        "3. ก่อนเริ่มการทดสอบ เครื่องมือได้รับการปรับสภาพภายในห้อง"
        "ปฏิบัติการอย่างน้อย 2 ชั่วโมง เพื่อให้เข้าสู่สมดุลทางความร้อน"
        "กับสภาพแวดล้อมของห้อง",
        "4. ณ จุดทดสอบแต่ละจุด ระบบจะคงตัวจนค่าอุณหภูมิเปลี่ยนแปลง"
        "น้อยกว่า 0.01 °C ต่อนาที จึงบันทึกค่าการอ่านซ้ำ 3 ครั้ง แล้ว"
        "ใช้ค่าเฉลี่ยในการคำนวณข้อผิดพลาดที่รายงาน",
        "5. ความไม่แน่นอนที่รายงานเป็นความไม่แน่นอนส่วนขยายที่ระดับ"
        "ความเชื่อมั่นประมาณ 95 เปอร์เซ็นต์ โดยใช้ตัวคูณความไม่แน่นอน"
        " k = 2 ตามแนวทางการแสดงความไม่แน่นอนของผลการวัด (GUM)",
    ]
    for item in items:
        y = draw_par(d, MARGIN, y, item, size=20, leading=1.6)
        y += 8
    draw_footer(d, 2)
    return img


def build_page_3():
    """Calibration results table (10 points, numeric columns)."""
    img, d = new_page()
    draw_running_header(d)
    y = 96

    y = draw_section(d, MARGIN, y, "ผลการสอบเทียบ")
    rows = []
    for std, err, unc in zip(STD_VALS, ERRORS, UNCERTS):
        rows.append([
            f"{std:.2f}",          # ค่ามาตรฐาน
            f"{std + err:.2f}",    # ค่าอ่านได้
            f"{err:+.2f}",         # ข้อผิดพลาด
            f"± {unc:.2f}",        # ความไม่แน่นอน k = 2
        ])
    y = draw_table(
        d, MARGIN, y,
        ["จุดทดสอบ (°C)", "ค่ามาตรฐาน (°C)", "ค่าอ่านได้ (°C)",
         "ข้อผิดพลาด (°C)", "ความไม่แน่นอน (°C), k = 2"],
        [[str(p)] + r for p, r in zip(POINTS, rows)],
        [200, 210, 210, 220, 260],
        aligns=["center"] * 5, size=20)
    y = draw_caption(
        d, y, "ตารางที่ 3 ผลการสอบเทียบเครื่องวัดอุณหภูมิแบบดิจิทัล "
              "รุ่น TM-946 เลขประจำเครื่อง SN-2024-08817 ณ จุดทดสอบ "
              "แต่ละจุด (ค่าข้อผิดพลาด = ค่าอ่านได้ - ค่ามาตรฐาน)")
    y += 16
    y = draw_par(
        d, MARGIN, y,
        "หมายเหตุ: ค่ามาตรฐานในตารางคือค่าอ้างอิงจากเทอร์มิสเตอร์"
        "มาตรฐานหลังการแก้ค่าการอ่านและการปรับค่าอุณหภูมิของหลอด"
        "มาตรฐานแล้ว ค่าการอ่านที่รายงานเป็นค่าเฉลี่ยจากการอ่านซ้ำ "
        "3 ครั้ง ณ สภาวะคงตัว รายละเอียดการอ่านซ้ำแสดงในภาคผนวด ก "
        "ท้ายรายงานฉบับนี้",
        size=20, leading=1.6)
    draw_footer(d, 3)
    return img


def build_page_4():
    """Assessment table + error-curve plot + note."""
    img, d = new_page()
    draw_running_header(d)
    y = 96

    y = draw_section(d, MARGIN, y, "ตารางผลการประเมินการสอบเทียบ")
    max_err = max(abs(e) for e in ERRORS)
    max_unc = max(UNCERTS)
    y = draw_table(
        d, MARGIN, y,
        ["รายการประเมิน", "ค่าที่ประเมินได้", "เกณฑ์การยอมรับ",
         "ผลการประเมิน"],
        [["ค่าเบี่ยงเบนสูงสุด (ข้อผิดพลาดสัมบูรณ์สูงสุด)",
          f"{max_err:.2f} °C", "ไม่เกิน ± 0.10 °C", "ผ่าน"],
         ["ความไม่แน่นอนสูงสุดที่รายงาน (k = 2)",
          f"± {max_unc:.2f} °C", "ไม่เกิน ± 0.10 °C", "ผ่าน"],
         ["การเปลี่ยนแปลงของค่าการอ่านซ้ำ (ค่าเบี่ยงเบนมาตรฐาน)",
          "0.02 °C", "ไม่เกิน 0.05 °C", "ผ่าน"],
         ["สรุปผลการประเมินรวม", "-", "-", "ผ่าน"]],
        [430, 210, 240, 220],
        aligns=["left", "center", "center", "center"], size=19)
    y = draw_caption(d, y, "ตารางที่ 4 ผลการประเมินผลการสอบเทียบ"
                           "เทียบกับเกณฑ์การยอมรับที่ผู้ส่งตรวจกำหนด")
    y += 14

    plot = render_error_plot()
    scale = CONTENT_W / plot.width
    plot = plot.resize((CONTENT_W, int(plot.height * scale)),
                       Image.LANCZOS)
    img.paste(plot, (MARGIN, int(y)))
    y += plot.height + 12
    y = draw_caption(
        d, y, "ภาพที่ 1 กราฟแสดงข้อผิดพลาดของเครื่องมือที่แต่ละจุดทดสอบ "
              "แท่งแนวตั้งแสดงความไม่แน่นอนส่วนขยาย ณ ระดับ k = 2 "
              "เส้นประแนวนอนแสดงเกณฑ์การยอมรับ ± 0.10 °C")
    y += 14
    draw_par(
        d, MARGIN, y,
        "หมายเหตุ: ทุกจุดทดสอบมีช่วงความไม่แน่นอน (ค่าอ่านได้บวกลบ "
        "ความไม่แน่นอน) ตั้งอยู่ภายในเขตเกณฑ์การยอมรับ จึงสรุปได้ว่า"
        "ผลการสอบเทียบจุดทดสอบทั้งหมดเป็นไปตามเกณฑ์ที่กำหนด ค่าใน"
        "ภาพและตารางข้างต้นแสดงจากข้อมูลชุดเดียวกันกับตารางที่ 3",
        size=20, leading=1.6)
    draw_footer(d, 4)
    return img


def draw_signature_block(d, y):
    col_w = (CONTENT_W - 60) / 2
    for i, (title, name, pos) in enumerate([
        ("ผู้ปฏิบัติการ", "นายสมชาย วงศ์ตัวอย่าง",
         "ตำแหน่ง นักวิชาการเทคนิค"),
        ("ผู้อนุมัติ", "นางสาวปิยะรัตน์ ใจตัวอย่าง",
         "ตำแหน่ง หัวหน้าห้องปฏิบัติการ"),
    ]):
        x = MARGIN + i * (col_w + 60)
        y0 = y
        y0 = draw_par(d, x, y0, title, size=21, bold=True,
                      width=col_w, leading=1.4)
        y0 += 74
        d.line([(x, y0), (x + col_w - 40, y0)], fill=INK, width=1)
        y0 += 12
        y0 = draw_par(d, x, y0, f"( {name} )", size=20, width=col_w,
                      leading=1.45)
        y0 = draw_par(d, x, y0, pos, size=19, width=col_w, fill=INK_SOFT,
                      leading=1.45)
        y0 = draw_par(d, x, y0, f"วันที่ {REPORT_ISSUED}", size=19,
                      width=col_w, fill=INK_SOFT, leading=1.45)
    return max(y0, y) + 10


def build_page_5():
    """Summary, pass result, signatures, disclaimer."""
    img, d = new_page()
    draw_running_header(d)
    y = 96

    y = draw_section(d, MARGIN, y, "สรุปผลการสอบเทียบ")
    y = draw_par(
        d, MARGIN, y,
        "จากผลการทดสอบตามที่ปรากฏในตารางผลการสอบเทียบ และผลการประเมิน"
        "เทียบกับเกณฑ์การยอมรับที่ผู้ส่งตรวจกำหนด ห้องปฏิบัติการขอ"
        "รับรองว่าเครื่องมือรายการนี้มีค่าเบี่ยงเบนอยู่ภายในเกณฑ์ที่"
        "กำหนดทุกจุดทดสอบ และมีความไม่แน่นอนที่รายงานดังปรากฏใน"
        "ตารางผลการสอบเทียบ",
        size=21, leading=1.65)
    y += 18

    box_h = 64
    d.rectangle([MARGIN, y, MARGIN + CONTENT_W, y + box_h],
                outline=INK, width=2)
    f = font(24, bold=True)
    text = "ผลการสอบเทียบ: ผ่าน (PASS)"
    tw = d.textlength(text, font=f)
    d.text((int((PAGE_W - tw) / 2), int(y + (box_h - 34) / 2)), text,
           font=f, fill=INK)
    y += box_h + 26
    y = draw_par(
        d, MARGIN, y,
        "หมายเหตุ: ค่าความไม่แน่นอนที่รายงานนี้ไม่รวมความไม่แน่นอน"
        "จากการนำเครื่องมือไปใช้งานโดยผู้ใช้ปลายทาง และผลการสอบเทียบ"
        "มีผลเฉพาะสภาวะแห่งการทดสอบตามที่ระบุไว้ในรายงานฉบับนี้",
        size=20, leading=1.6)
    y += 40

    y = draw_signature_block(d, y)
    y += 30
    y = draw_section(d, MARGIN, y, "ข้อความแจ้งเตือน")
    draw_par(
        d, MARGIN, y,
        "ใบรับรองฉบับนี้จัดทำขึ้นเพื่อรายงานผลการสอบเทียบของเครื่องมือ"
        "ที่ระบุเท่านั้น มิใช่การรับรองการผลิตหรือการตรวจรับตัวอย่าง"
        "อื่นใด ห้ามทำสำเนาบางส่วนโดยไม่ได้รับความยินยอมเป็นลายลักษณ์"
        "อักษรจากห้องปฏิบัติการ เว้นแต่จะทำสำเนาฉบับสมบูรณ์ทุกหน้า "
        "ห้องปฏิบัติการไม่รับผิดชอบต่อการนำเครื่องมือไปใช้งานนอกเหนือ"
        "จากช่วงการใช้งานที่ระบุไว้ในเอกสารฉบับนี้ หากพบข้อสงสัย"
        "กรุณาติดต่องานบริการลูกค้าตามที่อยู่ด้านบนของเอกสาร",
        size=19, leading=1.6)
    draw_footer(d, 5)
    return img


def build_page_6():
    """Annex: repeated-reading record (numeric, for OCR digit tests)."""
    img, d = new_page()
    draw_running_header(d)
    y = 96

    y = draw_section(d, MARGIN, y, "ภาคผนวด ก: บันทึกค่าการอ่านซ้ำ")
    y = draw_par(
        d, MARGIN, y,
        "บันทึกค่าการอ่านซ้ำ 3 ครั้ง ณ จุดทดสอบที่เลือก พร้อมค่าเฉลี่ย"
        "และค่าเบี่ยงเบนมาตรฐานของการอ่าน (ใช้สำหรับประเมินความซ้ำได้"
        "ของเครื่องมือ)",
        size=20, leading=1.6)
    y += 14

    rows = []
    for std, reads in zip(REPEAT_POINTS, REPEAT_READS):
        mean = sum(reads) / len(reads)
        var = sum((r - mean) ** 2 for r in reads) / (len(reads) - 1)
        sd = var ** 0.5
        rows.append([f"{std:.2f}"] + [f"{r:.2f}" for r in reads]
                    + [f"{mean:.2f}", f"{sd:.2f}"])
    y = draw_table(
        d, MARGIN, y,
        ["ค่ามาตรฐาน (°C)", "ครั้งที่ 1 (°C)", "ครั้งที่ 2 (°C)",
         "ครั้งที่ 3 (°C)", "ค่าเฉลี่ย (°C)", "ส่วนเบี่ยงเบน (°C)"],
        rows,
        [180, 185, 185, 185, 185, 180],
        aligns=["center"] * 6, size=19)
    y = draw_caption(d, y, "ตาราง ก.1 บันทึกค่าการอ่านซ้ำของเครื่องมือ"
                           " ณ จุดทดสอบที่เลือก")
    y += 14
    y = draw_par(
        d, MARGIN, y,
        "หมายเหตุ: ค่าเบี่ยงเบนมาตรฐานของการอ่านซ้ำถูกนำไปรวมในการ"
        "ประเมินความไม่แน่นอนของผลการสอบเทียบตามตารางที่ 3 ค่าที่"
        "แสดงในภาคผนวดนี้เป็นข้อมูลดิบก่อนการคำนวณข้อผิดพลาด",
        size=20, leading=1.6)
    draw_footer(d, 6)
    return img


def apply_scan_effects(img, seed):
    """Subtle scan realism: slight rotation, faint noise, light margin
    shading and one soft gray band. Kept gentle so OCR stays feasible."""
    rng = np.random.default_rng(seed)
    angle = rng.uniform(-0.4, 0.4)
    img = img.rotate(angle, resample=Image.BICUBIC,
                     fillcolor=(252, 252, 251))
    arr = np.asarray(img).astype(np.float32)
    h, w = arr.shape[:2]

    arr += rng.normal(0.0, 2.0, (h, w, 1))

    col = np.arange(w, dtype=np.float32)
    shade = 1.0 - 0.02 * np.exp(-((col - 34.0) / 55.0) ** 2)
    shade -= 0.02 * np.exp(-((col - (w - 34.0)) / 55.0) ** 2)
    arr *= shade[np.newaxis, :, np.newaxis]

    band_y = int(rng.integers(int(h * 0.15), int(h * 0.85)))
    band_h = int(rng.integers(60, 120))
    arr[band_y:band_y + band_h, :, :] -= 4.0

    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def main():
    parser = argparse.ArgumentParser(
        description="Generate synthetic Thai calibration-report pages.")
    parser.add_argument("--outdir", default=None,
                        help="output directory (default: "
                             "<repo>/datasets/measurement_reports)")
    parser.add_argument("--seed", type=int, default=27,
                        help="random seed for scan realism (default: 27)")
    args = parser.parse_args()

    font_path = resolve_font()
    repo_root = find_repo_root()
    outdir = (Path(args.outdir) if args.outdir
              else repo_root / "datasets" / "measurement_reports")
    outdir.mkdir(parents=True, exist_ok=True)

    # Clean overwrite: remove pages from a previous run only.
    for old in sorted(outdir.glob("page*.png")):
        old.unlink()

    builders = [build_page_1, build_page_2, build_page_3,
                build_page_4, build_page_5, build_page_6]
    written = []
    for i, build in enumerate(builders, start=1):
        page = apply_scan_effects(build(), args.seed * 100 + i)
        out = outdir / f"page{i:02d}.png"
        page.save(out, "PNG")
        written.append(out)

    print(f"Thai font used: {font_path} "
          f"(body face index {_FONT_BODY}, bold face index {_FONT_BOLD})")
    print(f"Generated {len(written)} pages in {outdir}:")
    for path in written:
        print(f"  {path.name}  {path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
