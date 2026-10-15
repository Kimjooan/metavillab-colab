# -*- coding: utf-8 -*-
"""OCR 연습용 샘플 이미지 생성기 (직접 제작, 저작권 문제 없음).

  python tools/make_samples.py

- samples/u02/menu_ko.png : 가짜 분식집 메뉴판. 흰 바탕, 큰 글씨, 한글 메뉴와 가격.
- samples/u02/sign_en.jpg : 영어 안내판. 짙은 바탕에 흰 글씨.
글씨가 크고 깨끗해야 첫 OCR 활동에서 결과가 안정적이다.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "samples", "u02")

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\NanumGothic-Bold.ttf",
    r"C:\Windows\Fonts\malgunbd.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
]
FONT_REG_CANDIDATES = [
    r"C:\Windows\Fonts\NanumGothic-Regular.ttf",
    r"C:\Windows\Fonts\malgun.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
]
NAVY = (34, 49, 92)
YELLOW = (255, 212, 59)
INK = (27, 36, 64)


def font(candidates, size):
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    raise SystemExit("한글 글꼴을 찾지 못했어요: " + ", ".join(candidates))


def menu_ko():
    W, H = 900, 1200
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    title_f = font(FONT_CANDIDATES, 84)
    item_f = font(FONT_REG_CANDIDATES, 60)
    price_f = font(FONT_CANDIDATES, 60)
    small_f = font(FONT_REG_CANDIDATES, 36)

    # 머리띠
    d.rectangle([0, 0, W, 200], fill=NAVY)
    d.text((W // 2, 100), "메타 분식", font=title_f, fill=YELLOW, anchor="mm")
    d.text((W // 2, 250), "오늘의 메뉴", font=small_f, fill=INK, anchor="mm")

    items = [
        ("떡볶이", "4000원"),
        ("김밥", "3500원"),
        ("라면", "4500원"),
        ("순대", "5000원"),
        ("튀김", "3000원"),
        ("어묵", "1000원"),
    ]
    y = 340
    for name, price in items:
        d.text((90, y), name, font=item_f, fill=INK, anchor="lm")
        d.text((W - 90, y), price, font=price_f, fill=NAVY, anchor="rm")
        d.line([90, y + 55, W - 90, y + 55], fill=(226, 231, 240), width=3)
        y += 120

    d.rectangle([0, H - 110, W, H], fill=YELLOW)
    d.text((W // 2, H - 55), "포장 됩니다", font=small_f, fill=INK, anchor="mm")
    return img


def sign_en():
    W, H = 1000, 600
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    big = font(FONT_CANDIDATES, 110)
    mid = font(FONT_REG_CANDIDATES, 56)
    d.rectangle([30, 30, W - 30, H - 30], outline=YELLOW, width=8)
    d.text((W // 2, 200), "WELCOME", font=big, fill="white", anchor="mm")
    d.text((W // 2, 330), "METAVIL LAB", font=mid, fill=YELLOW, anchor="mm")
    d.text((W // 2, 440), "OPEN 10:00 - 18:00", font=mid, fill="white", anchor="mm")
    return img


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p1 = os.path.join(OUT, "menu_ko.png")
    menu_ko().save(p1, optimize=True)
    p2 = os.path.join(OUT, "sign_en.jpg")
    sign_en().convert("RGB").save(p2, quality=92)
    for p in (p1, p2):
        print(p, os.path.getsize(p), "bytes")
