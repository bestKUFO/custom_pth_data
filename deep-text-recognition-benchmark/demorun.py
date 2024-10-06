import os

def run_demo():
    command = (
        "python deep-text-recognition-benchmark/demo.py "
        "--Transformation None "
        "--FeatureExtraction VGG "
        "--SequenceModeling BiLSTM "
        "--Prediction CTC "
        "--image_folder deep-text-recognition-benchmark/demo_image/ "
        "--saved_model ./deep-text-recognition-benchmark/model/None-VGG-BiLSTM-CTC.pth"
    )
    os.system(command)

if __name__ == "__main__":
    run_demo()
