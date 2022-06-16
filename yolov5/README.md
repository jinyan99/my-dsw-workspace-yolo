python train.py --img 640 --batch 16 --epochs 100 --data CustomDataSets/data/data.yaml --weights yolov5s.pt


python detect.py --weights runs/train/exp5/weights/best.pt --source CustomDataSets/data/test/images/1648546392313.jpg