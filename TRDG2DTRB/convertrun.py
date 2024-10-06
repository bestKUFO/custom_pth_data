import os

# 경로 설정
input_path = r"generate_run.py에서 생성된 이미지 파일 경로지정" # 예시 "C:\out"
output_path = "./TRDG2DTRB/output" # convert된 이미지 파일 생성경로

# convert.py 실행
os.system(f"python TRDG2DTRB/convert.py --input_path {input_path} --output_path {output_path}")
