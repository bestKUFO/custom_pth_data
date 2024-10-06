import os

def run_training():
    command = (
        "python deep-text-recognition-benchmark/train.py "
        "--train_data data_lmdb/train "
        "--valid_data data_lmdb/validation "
        # "--select_data / "
        # "--batch_ratio 1 "
        "--Transformation None "
        "--FeatureExtraction VGG "
        "--SequenceModeling BiLSTM "
        "--Prediction CTC "
        "--workers 0 "
        "--num_iter 10000 "
        
    )


    os.system(command)

if __name__ == "__main__":
    run_training()
