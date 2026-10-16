# metavillab-colab

메타빌랩 학습 플랫폼(learn.metavillab.com) "파이썬 (Python) - 코랩 활동" 과목의 **노트북 원본**과 **샘플 파일** 저장소입니다.

- 학생은 이 저장소를 직접 보지 않습니다. 학습 화면의 "코랩에서 열기" 링크가 여기 노트북을 구글 코랩으로 엽니다.
- 설명, 순서도, 캡처, 확인 문제는 learnX 플랫폼(Firestore `content_markdown`)에 있습니다. 이 저장소에는 **코랩에서 실행되는 것**만 둡니다.
- 설계 기준 문서: learnX 저장소 `client/public/content/_templates/코랩활동_설계.md`

## 구조

```
notebooks/
  u01/a01_first_run.ipynb        01. 코랩 첫걸음 · 활동 1 코랩 열고 첫 셀 실행하기
  u01/a02_notebook_basics.ipynb  01. 코랩 첫걸음 · 활동 2 노트북 다루기
  u01/a03_qrcode.ipynb           01. 코랩 첫걸음 · 활동 3 라이브러리 설치하고 QR코드 만들기
  u02/a04_ocr.ipynb              02. 사진 속 글자 · 활동 4 사진에서 글자 뽑기 (OCR)
  u02/a05_ocr_cleanup.ipynb      02. 사진 속 글자 · 활동 5 뽑은 글자 다듬기
  u02/a06_ocr_boxes.ipynb        02. 사진 속 글자 · 활동 6 글자 영역에 상자 그리기
  u02/a07_ocr_translate.ipynb    02. 사진 속 글자 · 활동 7 사진 속 글자 번역하기
samples/
  u01/upload_me.png              활동 2 파일 올리기 연습 그림 (학습 화면에서도 내려받음)
  u02/menu_ko.png                OCR 연습용 가짜 분식집 메뉴판 (직접 제작)
  u02/sign_en.jpg                OCR 연습용 영어 안내판 (직접 제작)
  u02/sign_ko.png                번역 연습용 한국어 안내문 (직접 제작, 활동 7)
tools/
  build_notebooks.py             노트북 .ipynb 파일을 만드는 스크립트 (셀 내용의 원본)
  make_samples.py                샘플 이미지를 만드는 스크립트
```

## 코랩에서 여는 주소

```
https://colab.research.google.com/github/Kimjooan/metavillab-colab/blob/main/notebooks/u02/a04_ocr.ipynb
```

저장소가 **공개(public)** 여야 로그인 없이 열립니다. 노트북 안에서 샘플 파일은 다음 주소로 받습니다.

```
https://raw.githubusercontent.com/Kimjooan/metavillab-colab/main/samples/u02/menu_ko.png
```

## 노트북 고치는 방법

노트북은 `tools/build_notebooks.py` 안의 셀 목록에서 만들어집니다. 코랩에서 직접 고쳐 저장하지 말고 이 스크립트를 고친 뒤 다시 실행합니다.

```
python tools/build_notebooks.py
python tools/make_samples.py
```

## 셀 규칙 (요약)

1. 셀 0은 글 셀. 활동 제목과 "위에서 아래로 순서대로 실행" 안내.
2. 셀 1은 준비 셀. `pip install`, 모델 다운로드, 샘플 받기를 전부 모은다. 마지막 줄은 `print("준비 끝")`.
3. 셀 2부터는 한 셀이 순서도의 한 칸. 첫 줄 주석은 `# [셀 2] 하는 일`.
4. 모든 코드 셀은 눈에 보이는 출력으로 끝난다.
5. 마지막 글 셀은 학습 화면으로 돌아가라는 안내, 그 아래 바꿔 보기용 빈 셀.
6. 글은 해요체. 줄표(—)·화살표(→) 금지.
