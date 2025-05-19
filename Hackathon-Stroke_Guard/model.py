!git clone http://github.com/ultralytics/ultralytics.git # 욜로 다운 

model = YOLO("yolo11s.pt")

# Yolo에 필요한 라이브러리 

!pip install tqdm
# yolov8 프로젝트 제작에 필요한 라이브러리 설치
!pip install torch torchvision numpy matplotlib
!pip install ultralytics
!pip install -r requirements.txt
!pip install ultralytics opencv-python
