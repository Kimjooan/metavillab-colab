# -*- coding: utf-8 -*-
"""코랩 활동 노트북(.ipynb) 생성기.

셀 내용의 원본은 이 파일이다. 노트북을 고칠 때는 여기를 고치고 다시 실행한다.

  python tools/build_notebooks.py
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER_REPO = "Kimjooan/metavillab-colab"
RAW = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(keepends=True)}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.strip("\n").splitlines(keepends=True),
    }


def notebook(cells, title):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "colab": {"name": title, "provenance": []},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"},
        },
        "cells": cells,
    }


# ─────────────────────────────────────────────────────────────
# 활동 1 · 코랩 열고 첫 셀 실행하기  (py_colab_u01_a01)
# ─────────────────────────────────────────────────────────────
A01 = notebook([
    md("""
# 활동 1 · 코랩 열고 첫 셀 실행하기

첫 노트북이에요. 셀을 **위에서 아래로 하나씩** 실행해요.
셀 왼쪽의 ▶ 버튼을 누르거나, 셀을 고른 뒤 `Shift + Enter`를 눌러요.

이 노트북은 learnX 학습 화면과 같이 봐요. 학습 화면의 캡처를 보며 따라 해요.
"""),
    code("""
# [셀 1] 인사하기
print("안녕, 코랩!")
"""),
    code("""
# [셀 2] 지금 시각 보기
import datetime
print(datetime.datetime.now())
"""),
    code("""
# [셀 3] 이 컴퓨터는 어디 있을까
import platform
print(platform.node())
print(platform.system())
"""),
    code("""
# [셀 4] 내 이름으로 인사
name = "메타빌"
print(name + ", 반가워요!")
"""),
    md("""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 1 · 코랩 열고 첫 셀 실행하기")


# ─────────────────────────────────────────────────────────────
# 활동 2 · 노트북 다루기  (py_colab_u01_a02)
# ─────────────────────────────────────────────────────────────
A02 = notebook([
    md("""
# 활동 2 · 노트북 다루기

이 칸이 **글 셀**이에요. 두 번 누르면 안에 쓴 글이 보이고, 다른 곳을 누르면 다시 이렇게 보여요.

아래의 코드 셀을 **위에서 아래로 하나씩** 실행해요. 셀 3은 일부러 틀리게 써 두었어요.
이 노트북은 learnX 학습 화면과 같이 봐요.
"""),
    code("""
# [셀 1] 점수 만들기
score = 80
print("점수:", score)
"""),
    code("""
# [셀 2] 점수 올리기  ※ 한 번 더 실행해 봐요
score = score + 10
print("점수:", score)
"""),
    code("""
# [셀 3] 오류 읽기  ※ 일부러 틀리게 썼어요. 오류를 읽고 고쳐요
print("최종 점수:", scroe)
"""),
    code("""
# [셀 4] 다시 시작해도 남을까
print("점수:", score)
"""),
    code("""
# [셀 5] 올린 파일 찾기  ※ 먼저 왼쪽 파일 보기에서 upload_me.png를 올려요
import os
print(os.listdir())
"""),
    code("""
# [셀 6] 올린 그림 보기
from IPython.display import Image, display
print("upload_me.png", os.path.getsize("upload_me.png"), "바이트")
display(Image("upload_me.png", width=320))
"""),
    md("""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 2 · 노트북 다루기")


# ─────────────────────────────────────────────────────────────
# 활동 3 · 라이브러리 설치하고 QR코드 만들기  (py_colab_u01_a03)
# ─────────────────────────────────────────────────────────────
A03 = notebook([
    md("""
# 활동 3 · 라이브러리 설치하고 QR코드 만들기

QR코드를 만드는 라이브러리를 설치하고, 내 이름이 담긴 QR코드 그림을 만들어 내 PC로 내려받아요.
셀을 **위에서 아래로 하나씩** 실행해요.

이 노트북은 learnX 학습 화면과 같이 봐요.
"""),
    code("""
# [준비] qrcode 라이브러리를 설치해요. 10초쯤 걸려요.
!pip install -q --progress-bar off qrcode
print("준비 끝")
"""),
    code("""
# [셀 2] QR에 담을 글 정하기
message = "이름: 메타빌"
print("QR에 담을 글:", message)
"""),
    code("""
# [셀 3] QR코드 만들기
import qrcode
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(message)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
print("가로세로", qr.modules_count, "칸짜리 QR코드를 만들었어요")
"""),
    code("""
# [셀 4] QR코드 그림으로 저장하고 보기
from IPython.display import Image, display
img.save("my_qr.png")
display(Image("my_qr.png", width=260))
"""),
    code("""
# [셀 5] 내 PC로 내려받기
from google.colab import files
files.download("my_qr.png")
print("my_qr.png 내려받기를 시작했어요")
"""),
    md("""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 3 · 라이브러리 설치하고 QR코드 만들기")


# ─────────────────────────────────────────────────────────────
# 활동 4 · 사진에서 글자 뽑기 (OCR)  (py_colab_u02_a04)
# ─────────────────────────────────────────────────────────────
A04 = notebook([
    md("""
# 활동 4 · 사진에서 글자 뽑기 (OCR)

사진 속 글자를 컴퓨터가 읽어 목록으로 만들어요.
셀을 **위에서 아래로 하나씩** 실행해요. 준비 셀과 셀 3은 조금 기다려야 해요.

이 노트북은 learnX 학습 화면과 같이 봐요.
"""),
    code(f"""
# [준비] 1~3분 걸려요. 기다리는 동안 학습 화면의 "이해하기"를 읽어요.
!pip install -q --progress-bar off easyocr
!wget -q {RAW}/samples/u02/menu_ko.png
import warnings, logging
warnings.filterwarnings("ignore")
logging.getLogger("easyocr").setLevel(logging.ERROR)
print("준비 끝")
"""),
    code("""
# [셀 2] 사진 보기
from IPython.display import Image, display
display(Image("menu_ko.png", width=480))
"""),
    code("""
# [셀 3] 글자 읽는 도구 준비 (한국어 + 영어)  ※ 처음 한 번은 1~2분 기다려요
import easyocr
reader = easyocr.Reader(["ko", "en"], gpu=False)
print("도구 준비 끝")
"""),
    code("""
# [셀 4] 사진에서 글자 읽기
results = reader.readtext("menu_ko.png")
print(len(results), "개를 찾았어요")
"""),
    code("""
# [셀 5] 찾은 글자를 한 줄씩 보기
for box, text, conf in results:
    print(text, round(conf, 2))
"""),
    code("""
# [셀 6] 글자만 모아 한 문장으로
words = []
for box, text, conf in results:
    words.append(text)
print(" ".join(words))
"""),
    md(f"""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
영어 안내판 사진이 필요하면 이 한 줄을 준비 셀에 더해요.

```
!wget -q {RAW}/samples/u02/sign_en.jpg
```
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 4 · 사진에서 글자 뽑기 (OCR)")


# ─────────────────────────────────────────────────────────────
# 활동 5 · 뽑은 글자 다듬기  (py_colab_u02_a05)
# ─────────────────────────────────────────────────────────────
A05 = notebook([
    md("""
# 활동 5 · 뽑은 글자 다듬기

활동 4에서 뽑은 메뉴판 글자를 반복문과 조건문으로 다듬어요.
믿기 어려운 글자는 거르고, 가격과 메뉴 이름을 나누고, 원하는 단어를 찾고, 텍스트 파일로 저장해요.
셀을 **위에서 아래로 하나씩** 실행해요. 준비 셀과 셀 2는 조금 기다려야 해요.

이 노트북은 learnX 학습 화면과 같이 봐요.
"""),
    code(f"""
# [준비] 1~3분 걸려요. 기다리는 동안 학습 화면의 "이해하기"를 읽어요.
!pip install -q --progress-bar off easyocr
!wget -q {RAW}/samples/u02/menu_ko.png
import warnings, logging
warnings.filterwarnings("ignore")
logging.getLogger("easyocr").setLevel(logging.ERROR)
print("준비 끝")
"""),
    code("""
# [셀 2] 메뉴판 읽기 (활동 4와 같아요)  ※ 1분쯤 기다려요
import easyocr
reader = easyocr.Reader(["ko", "en"], gpu=False)
results = reader.readtext("menu_ko.png")
print("\\n찾은 글자:", len(results), "개")
"""),
    code("""
# [셀 3] 확신 정도로 거르기
words = []
for box, text, conf in results:
    if conf >= 0.6:
        words.append(text)
    else:
        print("버린 글자:", text, round(conf, 2))
print("남긴 글자:", len(words), "개")
"""),
    code("""
# [셀 4] 가격과 메뉴 이름 나누기
prices = []
names = []
for text in words:
    if "원" in text:
        prices.append(text)
    else:
        names.append(text)
print("가격:", prices)
print("이름:", names)
"""),
    code("""
# [셀 5] 단어 찾기
keyword = "김밥"
for i in range(len(words)):
    if keyword in words[i]:
        print("찾았어요:", words[i], "/ 순서", i)
        print("바로 다음 글자:", words[i + 1])
"""),
    code("""
# [셀 6] 텍스트 파일로 저장하기
with open("menu.txt", "w", encoding="utf-8") as f:
    for text in words:
        f.write(text + "\\n")
with open("menu.txt", encoding="utf-8") as f:
    print(f.read())
"""),
    md("""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 5 · 뽑은 글자 다듬기")


# ─────────────────────────────────────────────────────────────
# 활동 6 · 글자 영역에 상자 그리기  (py_colab_u02_a06)
# ─────────────────────────────────────────────────────────────
A06 = notebook([
    md("""
# 활동 6 · 글자 영역에 상자 그리기

OCR이 찾은 글자의 위치(box)를 써서 메뉴판 사진 위에 상자를 그리고, 상자 위에 읽은 글자를 써요.
셀을 **위에서 아래로 하나씩** 실행해요. 준비 셀과 셀 2는 조금 기다려야 해요.

이 노트북은 learnX 학습 화면과 같이 봐요.
"""),
    code(f"""
# [준비] 1~3분 걸려요. 기다리는 동안 학습 화면의 "이해하기"를 읽어요.
!pip install -q --progress-bar off easyocr
!apt-get -qq install -y fonts-nanum > /dev/null
!wget -q {RAW}/samples/u02/menu_ko.png
import warnings, logging
warnings.filterwarnings("ignore")
logging.getLogger("easyocr").setLevel(logging.ERROR)
print("준비 끝")
"""),
    code("""
# [셀 2] 메뉴판 읽기 (활동 4와 같아요)  ※ 1분쯤 기다려요
import easyocr
reader = easyocr.Reader(["ko", "en"], gpu=False)
results = reader.readtext("menu_ko.png")
print("\\n찾은 글자:", len(results), "개")
"""),
    code("""
# [셀 3] 상자 하나 살펴보기
box, text, conf = results[2]
print("글자:", text)
corners = ["왼쪽 위", "오른쪽 위", "오른쪽 아래", "왼쪽 아래"]
for i in range(4):
    print(corners[i], int(box[i][0]), int(box[i][1]))
"""),
    code("""
# [셀 4] 사진에 상자 그리기 (OpenCV)
import cv2
from IPython.display import Image, display
img = cv2.imread("menu_ko.png")
for box, text, conf in results:
    top_left = (int(box[0][0]), int(box[0][1]))
    bottom_right = (int(box[2][0]), int(box[2][1]))
    if conf >= 0.8:
        color = (0, 170, 0)    # 초록 (OpenCV는 파랑, 초록, 빨강 순서로 써요)
    else:
        color = (0, 0, 255)    # 빨강
    cv2.rectangle(img, top_left, bottom_right, color, 3)
cv2.imwrite("boxes.png", img)
display(Image("boxes.png", width=420))
"""),
    code("""
# [셀 5] OpenCV로 글자 쓰기  ※ 한글이 어떻게 나오는지 봐요
for box, text, conf in results:
    x, y = int(box[0][0]), int(box[0][1])
    cv2.putText(img, text, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)
cv2.imwrite("boxes_cv_text.png", img)
display(Image("boxes_cv_text.png", width=420))
"""),
    code("""
# [셀 6] 한글은 PIL과 나눔 글꼴로 쓰기
import PIL.Image
from PIL import ImageDraw, ImageFont
pic = PIL.Image.open("boxes.png")
draw = ImageDraw.Draw(pic)
font = ImageFont.truetype("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf", 30)
for box, text, conf in results:
    x, y = int(box[0][0]), int(box[0][1])
    draw.text((x, y - 36), text, font=font, fill=(30, 60, 200))
pic.save("boxes_text.png")
display(Image("boxes_text.png", width=420))
"""),
    md("""
---
여기까지 됐으면 학습 화면으로 돌아가 **결과 확인**을 눌러요.

아래 빈 셀은 **바꿔 보기** 미션에서 써요.
"""),
    code("""
# [바꿔 보기] 여기에 써요

"""),
], "활동 6 · 글자 영역에 상자 그리기")


TARGETS = {
    "notebooks/u01/a01_first_run.ipynb": A01,
    "notebooks/u01/a02_notebook_basics.ipynb": A02,
    "notebooks/u01/a03_qrcode.ipynb": A03,
    "notebooks/u02/a04_ocr.ipynb": A04,
    "notebooks/u02/a05_ocr_cleanup.ipynb": A05,
    "notebooks/u02/a06_ocr_boxes.ipynb": A06,
}

if __name__ == "__main__":
    for rel, nb in TARGETS.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_code = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
        print(f"wrote {rel}  (cells={len(nb['cells'])}, code={n_code})")
