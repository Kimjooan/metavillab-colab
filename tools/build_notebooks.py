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
!pip install -q easyocr
!wget -q {RAW}/samples/u02/menu_ko.png
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


TARGETS = {
    "notebooks/u01/a01_first_run.ipynb": A01,
    "notebooks/u02/a04_ocr.ipynb": A04,
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
