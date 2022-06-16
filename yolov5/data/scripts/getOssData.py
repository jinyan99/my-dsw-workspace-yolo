# ········ 鉴权初始化·············#
import oss2
# 解压用
import os
import shutil
import time

auth = oss2.Auth('LTAI5tGe3jvtyb1JR9eDUvkB', 'Ml9uq6GadTKwqqIKwDGckafP4PizUd')
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'person-img1')

# 公共代码
def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = os.path.join('.',folder_name)
    os.makedirs(target_path)
    shutil.unpack_archive(f,target_path)

def delete(f):
    os.remove(f)
    time.sleep(2)

# ········ 读取数据·············#
#读取一个完整文件。
# result = bucket.get_object('Datasets/comps-data.zip')
# print(result.read())

# 填写Object完整路径，完整路径中不包含Bucket名称，例如testfolder/exampleobject.txt。
# 下载Object到本地文件，并保存到指定的本地路径D:\\localpath\\examplefile.txt。如果指定的本地文件存在会覆盖，不存在则新建。
bucket.get_object_to_file('Datasets/comps-data.zip', './CustomDataSets.zip')
unzip_it('CustomDataSets.zip')
delete('CustomDataSets.zip')