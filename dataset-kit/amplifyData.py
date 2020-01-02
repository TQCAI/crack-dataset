import os,shutil
import numpy as np
import pylab as plt
import cv2
import datetime
import random
from scipy.misc import imsave
import scipy
from skimage import io

global pos
global lst
pos=0
input='images'
output='amplify'
test_output='测试与验证集'

pArr=np.zeros([16],'int32')
pArr.fill(-1)

def build_shuffle_list(length):
    lst=np.arange(length)
    np.random.shuffle(lst)
    return lst


def buildDir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def add_log(Str):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    with open('log.txt','a+') as f:
        f.writelines(Str+str(nowTime)+'\n')


def RotateClockWise90(img):
    trans_img = cv2.transpose( img )
    new_img = cv2.flip(trans_img, 1)
    return new_img

def saveFiles(img,data,lst):
    pos=lst[0]
    del lst[0]
    img=img[:,:,:3]
    # imsave(f'{output}/{pos:04d}.jpg',img)
    # imsave(f'{output}/{pos:04d}_gt.jpg',data)
    io.imsave(f'{output}/{pos:04d}.jpg',img)
    io.imsave(f'{output}/{pos:04d}_gt.jpg', data)


if __name__ == '__main__':
    add_log('开始时间：')
    buildDir(output)
    myFiles=[]
    for (root, dirs, files) in os.walk(input):
        for file in files:
            if file.find("_gt")<0 and file.find('.jpg')>=0:
                myFiles.append(file)
        break
    random.shuffle(myFiles)
    length=len(myFiles)*4  #旋转4个角度
    lst=build_shuffle_list(length)
    lst=list(lst)
    for i,s in enumerate(myFiles):
        name=os.path.splitext(s)[0]
        print(i,name)
        imgName=f'{input}/'+name+'.jpg'
        dataName=f'{input}/'+name+'_gt.jpg'
        img=plt.imread(imgName)
        data=plt.imread(dataName)
        saveFiles(img,data,lst)
        for j in range(3):
            img=RotateClockWise90(img)
            data=RotateClockWise90(data)
            saveFiles(img, data, lst)
            # plt.imshow(img)
            # plt.show()
            # plt.imshow(data)
            # plt.show()
        # break
    add_log('结束时间：')
    # os.system('shutdown -s')

