    !pwd
    !yolo task=detect mode=train model=/kaggle/working/yolo11n.pt data=/kaggle/input/stroke-dataset-2/data.yaml epochs=40 lr0=0.0001 batch=64 device=0 patience=10 

