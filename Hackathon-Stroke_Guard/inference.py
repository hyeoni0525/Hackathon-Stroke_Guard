from ultralytics import YOLO
import cv2

try:
    # YOLO 모델 로드
    model = YOLO('/kaggle/working/runs/detect/train/weights/best.pt')
    class_names = model.names  # 모델 클래스 이름 로드

    # 비디오 파일 열기
    video = cv2.VideoCapture('/kaggle/input/test-video/KakaoTalk_20241201_102813405.mp4')
    if not video.isOpened():
        raise IOError("비디오 파일을 열 수 없습니다.")

    # 출력 비디오 설정
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('/kaggle/working//Stroke_Video(2).avi', fourcc, fps, (width, height))

    # 클래스별 고유 색상 정의
    colors = {
        
        'Normal_Eyes': (0, 0, 0), 
        'Normal_Mouth': (255, 0, 0),  # 파란색 
        'Unnormal_Eyes': (0, 255, 0), # 초록색
        'Unnormal_Mouth': (0, 0, 255) # 빨간색 
    }

    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # YOLO로 감지 수행
        results = model(frame)

        # 감지된 객체 처리
        for box, cls, conf in zip(results[0].boxes.xyxy, results[0].boxes.cls, results[0].boxes.conf):
            x1, y1, x2, y2 = map(int, box)  # 바운딩 박스 좌표
            class_id = int(cls)  # 클래스 ID
            class_name = class_names[class_id]  # 클래스 이름
            confidence = float(conf)  # 신뢰도

            # 클래스 이름에 따른 색상 선택
            color = colors.get(class_name, (255, 255, 255))  # 기본값은 흰색

            # 바운딩 박스와 클래스 이름 그리기
            label = f"{class_name}: {confidence:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)  # 테두리 두께를 1로 설정
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)  # 글자 크기를 0.5, 두께를 1로 설정


        # 결과 저장
        out.write(frame)

        # 100번째 프레임마다 처리 진행 상황 출력
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"{frame_count} 프레임 처리 완료")

    print("비디오 처리 완료 및 저장 완료")

except Exception as e:
    print(f"오류 발생: {str(e)}")

finally:
    # 비디오 객체 해제
    video.release()
    out.release()
