I used these GitHub repositories. Thank you for your contributions!
>ocr_kor(https://github.com/parksunwoo/ocr_kor)

>TextRecognitionDataGenerator(https://github.com/Belval/TextRecognitionDataGenerator)

>TRDG2DTRB(https://github.com/DaveLogs/TRDG2DTRB)

>deep-text-recognition-benchmark(https://github.com/clovaai/deep-text-recognition-benchmark)

---

## 환경 가이드
python 3.6.13 버전 사용했음(anaconda 가상환경으로 생성했음)

+ pip list는 requirements.txt 참고
 
     pip install -r requirements.txt

+ PyTorch 1.8.1 + CUDA 11.1 설치
 
     pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 --extra-index-url https://download.pytorch.org/whl/cu111



## 실행 가이드

**1. ocr_dtrb -> generate_run.py**
   
   os.system(f"python {runpy} -c 4500 -w 1 -f 64 -l ko --output_dir ./out")
   
   -c 생성 이미지 갯수 -w 길이 -f 높이 -l 언어 --output_dir "{생성할 이미지 경로}" 로 수정 후 사용
   
   이외 기타 및 자세한 사항은 ocr_dtrb\data\generator\TextRecognitionDataGenerator\run.py의 def parse_arguments() 참고

#
**2. TRDG2DTRB -> convertrun.py**
   
   input_path와 output_path를 확인한 후 실행.
   
   실행 시 결과로 images의 이미지들(image_00000.jpg, image_00001.jpg, image_00002.jpg ...)와 gt.txt가 생성이 됨

#
**3. deep-text-recognition-benchmark -> run.py**
   
   gt_path에 gt.txt 파일 경로를 넣고
   
   commands 에서 --inputPath와 --outputPath의 경로를 확인한 뒤 실행 하면 LMDB 데이터 셋이 생성이 됨.
   
   만약 lmdb 사이즈를 조절하고 싶으면 deep-text-recognition-benchmark\create_lmdb_dataset.py에서 def createDataset의 env = lmdb.open(outputPath, map_size=104857600) map_size를 수정해주면 됨.(현재 100mb로 설정됨)
   
#
**4. deep-text-recognition-benchmark -> trainrun.py**
   
   --train_data 와 --valid_data의 경로를 확인하고 --num_iter (반복 횟수)를 조정해서 실행하면
   
   saved_models/None-VGG-BiLSTM-CTC-Seed1111 폴더 안에 pth파일들과 txt파일들이 생성된 것을 볼 수 있음
   
   여기서 EasyOCR에 사용할 pth파일은 best_accuracy.pth를 custom할 이미지 이름에 맞춰서 수정해주면 됨(ex. custom.py, custom.yaml, custom.pth)
   

   ### **!!! 만약 학습이 너무 느리다면 cuda가 설치됐는지 GPU가 작동중인지 확인하길 바람 !!!**
   
     import torch
   
     print(torch.cuda.is_available())  # True여야 함
   
     print(torch.cuda.get_device_name(0))  # GPU 이름 출력
   

### deep-text-recognition-benchmark\train.py 파일 내 수정된 사항
     parser.add_argument('--select_data', default='/'
     
     parser.add_argument('--batch_ratio', default='1'
     
     parser.add_argument('--character'  # 여기 default에 한글을 추가함. default 값을 빼고 trainrun.py의 command로 옮겨줘도 됨)
     
     parser.add_argument('--data_filtering_off', default=True
