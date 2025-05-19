
import os
import cv2
import numpy as np
import random

def augment_and_save_images(dataset_path, labels_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(dataset_path):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            continue  # 이미지 파일만 처리

        file_path = os.path.join(dataset_path, filename)
        label_file_path = os.path.join(labels_path, filename.replace('.jpg', '.txt'))  # 라벨 파일 경로
        if not os.path.exists(label_file_path):
            continue  # 라벨 파일이 없으면 건너뛰기

        # 이미지 읽기
        image = cv2.imread(file_path)
        if image is None:
            continue  # 이미지 읽기 실패 시 건너뛰기

        # 라벨 읽기
        with open(label_file_path, 'r') as f:
            labels = []
            for line in f.readlines():
                parts = line.strip().split()
                if len(parts) >= 5:  # 다섯 개 이상의 값을 가지는 경우만 처리
                    # 클래스와 x_center, y_center, width, height를 가져옴
                    cls = int(parts[0])
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    width = float(parts[3])
                    height = float(parts[4])
                    labels.append([cls, x_center, y_center, width, height])

        # 랜덤 변환 선택
        transformation = random.choice(['flip', 'rotate_30', 'rotate_60'])

        if transformation == 'flip':
            augmented_image = cv2.flip(image, 1)  # 좌우 반전
            augmented_labels = flip_labels(labels, image.shape[1])
        elif transformation == 'rotate_30':
            augmented_image = rotate_image(image, 30)
            augmented_labels = rotate_labels(labels, image, 30)
        elif transformation == 'rotate_60':
            augmented_image = rotate_image(image, 60)
            augmented_labels = rotate_labels(labels, image, 60)

        # 저장 경로 설정
        base_name, ext = os.path.splitext(filename)
        new_filename = f"{base_name}_{transformation}{ext}"
        new_label_filename = f"{base_name}_{transformation}.txt"
        save_image_path = os.path.join(output_path, new_filename)
        save_label_path = os.path.join(output_path, new_label_filename)

        # 이미지 저장
        cv2.imwrite(save_image_path, augmented_image)

        # 라벨 저장
        with open(save_label_path, 'w') as f:
            for label in augmented_labels:
                f.write(' '.join(map(str, label)) + '\n')

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

def rotate_labels(labels, image, angle):
    # 회전 변환은 다소 복잡하므로 이 부분은 단순히 패스하도록 함 (추후 정확한 회전 로직 필요)
    return labels

def flip_labels(labels, image_width):
    flipped_labels = []
    for label in labels:
        cls, x_center, y_center, width, height = label
        x_center = 1.0 - x_center  # 좌우 반전
        flipped_labels.append([cls, x_center, y_center, width, height])
    return flipped_labels

# 사용 예제
dataset_path = "/kaggle/input/stroke-dataset-2/train/images"  # 원본 이미지 경로
labels_path = "/kaggle/input/stroke-dataset-2/train/labels"  # 원본 라벨 경로
output_path = "/kaggle/working/preview3"   # 변환 이미지 저장 경로
augment_and_save_images(dataset_path, labels_path, output_path)
