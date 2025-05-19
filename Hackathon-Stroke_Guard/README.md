# Hackathon finals-Stroke_Guard

**해커톤 본선 진출 내용 정리**

---

# StrokeGuard: 얼굴 표정을 통한 뇌졸중 전조 증상 감지 시스템

:arrow_forward: **StrokeGuard** 

YOLO 기반 얼굴 표정 인식 기술을 활용하여 뇌졸중 전조 증상을 실시간으로 감지하는 AI 헬스케어 시스템

:arrow_right: 고령자 및 1인 가구의 건강 위험을 줄이고, 돌봄 공백을 메우기 위한 솔루션으로 개발 진행

---

# CONTENTS
1. 프로젝트 개요
2. 발상 배경 및 문제 정의
3. 핵심 기능
4. 데이터 및 모델
5. 기술 구현 방식
6. 프로젝트 결과
7. 기대 효과

---

# 프로젝트 개요
<div align="center" style="height: 100vh;">
  <img src="https://github.com/user-attachments/assets/939b1d6a-c013-43ef-a12e-27a29ae50220" width="500" height="480" style="margin-right: 10px;" />
  <img src="https://github.com/user-attachments/assets/d7f6d247-459b-4a57-9fcf-5030b7c770fe" width="500" height="480" style="margin-left: 10px" />
</div>

- FAST 법칙 중 F (Face drooping)에 주목 :arrow_right: 얼굴 표정의 이상 징후(마비, 비대칭, 떨림) 자동 감지
- YOLOv11 기반 객체 탐지 모델을 사용한 실시간 분석
- 스마트폰 카메라 기반 서비스로 고령자도 쉽게 접근 가능
- 고령층, 독거노인, 1인 가구의 생명 안전 확보를 목표

---

# 발상 배경 및 문제 정의

- 뇌졸중은 치료 시기(4시간 반 이내)가 생명과 직결되며, 조기 대응이 중요
- 고령화 사회 및 1인 가구 증가 → 돌봄 공백 확산
- 의료기관 접근이 어려운 상황에서 기술 기반의 예측·대응 시스템 필요

---

# 핵심 기능

| 기능 | 설명 |
|------|------|
| 얼굴 표정 감지 및 분석 | 마비, 입꼬리 비대칭, 안면 떨림 등의 징후 탐지 |
| 스마트 기기 연동 | 앱 기반 서비스로 접근성 향상 |
| 실시간 알림 | 이상 감지 시 보호자/기관에 즉시 경고 전송 |
| 맞춤형 데이터 기반 학습 | 인종, 나이, 성별에 따른 편향 최소화 |

---

#  데이터 및 학습 모델

<div align="center" style="height: 100vh;">
  <img src="https://github.com/user-attachments/assets/c6f92f83-f0ee-448a-a9fc-12b7919daecb" width="440" height="440" style="margin-right: 10px;" />
  <img src="https://github.com/user-attachments/assets/1539d7e5-b612-4834-bfd8-58048170cbba" width="440" height="440" style="margin-left: 10px" />
</div>

- **데이터 출처**:
  - [Kaggle Stroke Face Dataset](https://www.kaggle.com/datasets/danish003/face-images-of-acute-stroke-and-non-acute-stroke)
  - [Roboflow Stroke Face Dataset](https://universe.roboflow.com/search?q=stroke+face)
- **데이터 특성**: 다양한 연령·인종·성별을 고려한 균형 잡힌 구성
- **모델 아키텍처**: YOLOv11 기반 얼굴 표정 탐지
- **데이터 처리 방식**
  - 얼굴 비대칭, 미소의 불균형, 안면 떨림 등 표정 변화 특성 추출
  - 데이터 증강 적용, 피드백 루프 기반 정확도 향상
  - 적용 증강 : GrayScale, Brightness Control, Left-Right Flip, Gaussian Filter, Crop

---

# 기술 구현 방식 및 향후 개발 계획

- 간단 구현 : Streamlit 프레임워크, OpenCV 및 PIL

- YOLOv11 기반 얼굴 표정 탐지 모델 사용
- 경량화 알고리즘 적용 → 스마트폰에서 실시간 처리 가능
- 카메라 앱 연동 → 사용자 얼굴 실시간 분석 및 알림 전송
- 노인 친화적 UI/UX 설계 → 접근성과 편의성 강화

# 프로젝트 결과

<div align="center" style="height: 100vh;">
  <img src="https://github.com/user-attachments/assets/e7a41cf0-dd2f-42a9-b137-d1d309a2c94e" width="400" height="400" style="margin-right: 10px;" />
  <img src="https://github.com/user-attachments/assets/5b1d6260-1397-40f3-b461-f18b941f05a0" width="400" height="400" style="margin-left: 10px" />
</div>

---

# 기대 효과 

-  **조기 진단** :arrow_right: 골든타임 확보 → 후유증 및 사망률 감소  
-  **노인 돌봄 보조** :arrow_right: 1인 가구 및 요양원 내 돌봄 공백 해소  
-  **사회적 비용 절감** :arrow_right: 재활·입원 비용 절감 및 응급 대응 부담 완화  
-  **데이터 융합 확장성** :arrow_right: 웨어러블·심박센서 등과 연동하여 정밀도 향상  

![image](https://github.com/user-attachments/assets/a9b5fecd-bfb4-4c26-ba36-590c819853da)




