# Hackathon-Stroke_Guard

2024 빅데이터/AI 글로벌 해커톤 본선 진출 내용 정리

----------
# Contents
1. Overview

2. Tech Stack

3. Dataset

4. Experiment

5. Results

6. Conclusion

7. Reference

-------
# Overview
<h2>StrokeGuard: 얼굴 표정을 통한 뇌졸중 전조 증상 감지 시스템</h2>
YOLO 기반 얼굴 표정 인식 기술을 활용하여 뇌졸중 전조 증상을 실시간으로 감지하는 AI 헬스케어 시스템

:arrow_forward: 고령자 및 1인 가구의 건강 위험을 줄이고, 돌봄 공백을 메우기 위한 솔루션으로 개발 진행<br>
<br>
<p align=center><img src="https://github.com/user-attachments/assets/84812323-e068-4c65-86f6-f8d2f95dd5bb" width="400" height="400"/></p>

- FAST 법칙 중 F (Face drooping)에 주목 :arrow_forward: 얼굴 표정의 이상 징후(마비, 비대칭, 떨림) 자동 감지

- YOLOv11 기반 객체 탐지 모델을 사용한 실시간 분석

- 스마트폰 카메라 기반 서비스로 고령자도 쉽게 접근 가능

- 고령층, 독거노인, 1인 가구의 생명 안전 확보를 목표

------
# Tech Stack
|기능|설명|
|--------------|------------|
|얼굴 표정 감지 및 분석|마비, 입꼬리 비대칭, 안면 떨림 등의 징후 탐지|
|스마트 기기 연동|앱 기반 서비스로 접근성 향상|
|실시간 알림|이상 감지 시 보호자/기관에 즉시 경고 전송|
|맞춤형 데이터 기반 학습|인종, 나이, 성별에 따른 편향 최소화|

-------
# Dataset
데이터 출처:

[Kaggle Stroke Face Dataset](https://www.kaggle.com/datasets/danish003/face-images-of-acute-stroke-and-non-acute-stroke)

[Roboflow Stroke Face Dataset](https://universe.roboflow.com/search?q=stroke+face)

데이터 특성: 다양한 연령·인종·성별을 고려한 균형 잡힌 구성

모델 아키텍처: YOLOv11 기반 얼굴 표정 탐지

데이터 처리 방식
1. 얼굴 비대칭, 미소의 불균형, 안면 떨림 등 표정 변화 특성 추출

2. 데이터 증강 적용, 피드백 루프 기반 정확도 향상
   적용 증강 : GrayScale, Brightness Control, Left-Right Flip, Gaussian Filter, Crop

-------
# Experiment
간단 구현 : Streamlit 프레임워크, OpenCV 및 PIL

YOLOv11 기반 얼굴 표정 탐지 모델 사용

경량화 알고리즘 적용 → 스마트폰에서 실시간 처리 가능

카메라 앱 연동 → 사용자 얼굴 실시간 분석 및 알림 전송

노인 Hackathon-Stroke_Guard

2024 빅데이터/AI 글로벌 해커톤 본선 진출 내용 정리

----------
# Contents
1. Overview

2. Tech Stack

3. Dataset

4. Experiment

5. Results

6. Conclusion


-------
# Overview
<h2>StrokeGuard: 얼굴 표정을 통한 뇌졸중 전조 증상 감지 시스템</h2>
YOLO 기반 얼굴 표정 인식 기술을 활용하여 뇌졸중 전조 증상을 실시간으로 감지하는 AI 헬스케어 시스템

:arrow_forward: 고령자 및 1인 가구의 건강 위험을 줄이고, 돌봄 공백을 메우기 위한 솔루션으로 개발 진행<br>
<br>
<p align=center><img src="https://github.com/user-attachments/assets/84812323-e068-4c65-86f6-f8d2f95dd5bb" width="400" height="400"/></p>

- FAST 법칙 중 F (Face drooping)에 주목 :arrow_forward: 얼굴 표정의 이상 징후(마비, 비대칭, 떨림) 자동 감지

- YOLOv11 기반 객체 탐지 모델을 사용한 실시간 분석

- 스마트폰 카메라 기반 서비스로 고령자도 쉽게 접근 가능

- 고령층, 독거노인, 1인 가구의 생명 안전 확보를 목표

------
# Tech Stack
|기능|설명|
|--------------|------------|
|얼굴 표정 감지 및 분석|마비, 입꼬리 비대칭, 안면 떨림 등의 징후 탐지|
|스마트 기기 연동|앱 기반 서비스로 접근성 향상|
|실시간 알림|이상 감지 시 보호자/기관에 즉시 경고 전송|
|맞춤형 데이터 기반 학습|인종, 나이, 성별에 따른 편향 최소화|

-------
# Dataset
데이터 출처:

[Kaggle Stroke Face Dataset](https://www.kaggle.com/datasets/danish003/face-images-of-acute-stroke-and-non-acute-stroke)

[Roboflow Stroke Face Dataset](https://universe.roboflow.com/search?q=stroke+face)

데이터 특성: 다양한 연령·인종·성별을 고려한 균형 잡힌 구성

모델 아키텍처: YOLOv11 기반 얼굴 표정 탐지

데이터 처리 방식
1. 얼굴 비대칭, 미소의 불균형, 안면 떨림 등 표정 변화 특성 추출

2. 데이터 증강 적용, 피드백 루프 기반 정확도 향상
   적용 증강 : GrayScale, Brightness Control, Left-Right Flip, Gaussian Filter, Crop

-------
# Experiment
- 간단 구현 : Streamlit 프레임워크, OpenCV 및 PIL

- YOLOv11 기반 얼굴 표정 탐지 모델 사용

- 경량화 알고리즘 적용 → 스마트폰에서 실시간 처리 가능

- 카메라 앱 연동 → 사용자 얼굴 실시간 분석 및 알림 전송

- 시니어 친화적 UI/UX 설계 → 접근성과 편의성 강화

------
# Results
<img src="" width="400" height="400"/>
<img src="https://github.com/user-attachments/assets/861e20dd-8bf2-4db0-8661-a87727c79012" width="400" height="400"/>

-------
# Conclusion
뇌졸중 피해 감소 :arrow_forward: 조기 발견 및 신속 대응으로 사망률 및 후유증 감소
사회적 비용 절감 및 삶의 질 향상 :arrow_forward: 돌봄 인력 부족 문제, 의료 자원 한계 극복 
범용성과 신뢰성 강화 :arrow_forward: 스마트 기기와 연동해 의료 기술 접근성과 편의성 향상
