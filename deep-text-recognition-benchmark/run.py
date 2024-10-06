import subprocess

# gt.txt 경로
# 예시 C:\TRDG2DTRB\output\gt.txt
gt_path = r"TRDG2DTRB에서 생성된 gt.txt 파일 경로를 여기다 넣으세요"

# LMDB 데이터셋 생성
commands = [
    f"python deep-text-recognition-benchmark/create_lmdb_dataset.py --inputPath TRDG2DTRB/output/ --gtFile {gt_path} --outputPath C:\\data_lmdb\\train",
    f"python deep-text-recognition-benchmark/create_lmdb_dataset.py --inputPath TRDG2DTRB/output/ --gtFile {gt_path} --outputPath C:\\data_lmdb\\validation",
    # f"python deep-text-recognition-benchmark/create_lmdb_dataset.py --inputPath TRDG2DTRB/output/ --gtFile {gt_path} --outputPath C:\\data_lmdb\\MJ-ST 구분시 추가",
    # f"python deep-text-recognition-benchmark/create_lmdb_dataset.py --inputPath TRDG2DTRB/output/ --gtFile {gt_path} --outputPath C:\\data_lmdb\\MJ-ST 구분시 추가",

]

# 각 명령어 실행
for command in commands:
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)

    print("Moving to next command.\n")
