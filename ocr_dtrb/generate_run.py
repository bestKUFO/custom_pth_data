import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# run.py 경로 지정
runpy = os.path.join(script_dir, 'data/generator/TextRecognitionDataGenerator/run.py')

# basic
os.system(f"python {runpy} -c 4500 -w 1 -f 64 -l ko --output_dir ./out")

# train_skew
os.system(f"python {runpy} -c 2250 -w 1 -f 64 -k 5 -rk -l ko --output_dir ./out")
os.system(f"python {runpy} -c 2250 -w 1 -f 64 -k 15 -rk -l ko --output_dir ./out")

# val_distortion
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -d 3 -do 0 -l ko --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -d 3 -do 1 -l ko --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -d 3 -do 2 -l ko --output_dir ./out")

# val_blur
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -bl 1 --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -bl 2 --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -bl 3 --output_dir ./out")

# val_background
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -b 0 --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -b 1 --output_dir ./out")
os.system(f"python {runpy} -c 1500 -w 1 -f 64 -l ko -b 2 --output_dir ./out")