#!/bin/bash
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
# Download COCO128 dataset https://www.kaggle.com/ultralytics/coco128 (first 128 images from COCO train2017)
# Example usage: bash data/scripts/get_coco128.sh
# parent
# ├── yolov5
# └── datasets
#     └── coco128  ← downloads here

# Download/unzip images and labels
d='../datasets' # unzip directory
url=https://person-img1.oss-cn-hangzhou.aliyuncs.com/Datasets/comps-data.zip?Expires=1655344294&OSSAccessKeyId=TMP.3KjVpVeBuCF2MyKr4TZ3Tm9xyvdW5xEW8DkzxLdGgsDTLLDQrRNNiRfXc3rBEE6ZkVLysGmJLYxscnWVb8NxbWCRHpzSQA&Signature=maZA06oyMHqvF9mfLIlmCX5Wjz4%3D
f='comps-data.zip' # or 'coco128-segments.zip', 68 MB
echo 'Downloading' $url$f ' ...'
curl -L $url -o $f && unzip -q $f -d $d && rm $f &

wait # finish background tasks
