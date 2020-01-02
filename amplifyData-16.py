import os,shutil
import numpy as np
import pylab as plt
import cv2
import datetime
import random

global pos
global lst
pos=0
output='放大数据集'
test_output='测试与验证集'

pArr=np.zeros([16],'int32')
pArr.fill(-1)

def build_shuffle_list(length):
    lst=np.arange(length)
    np.random.shuffle(lst)
    return lst

def imgPlus( a, b):
    ans = a.copy()
    x, y = b.shape[:2]
    for i in range(0, x):
        for j in range(0, y):
            if b[i, j] == 255:
                ans[i, j, 0] = 255
                ans[i, j, 1] = 0
                ans[i, j, 2] = 0
    return ans

def notLegal(img,x,y,axis=3):
    if axis==3:
        for i in range(0,3):
            if img[x,y,i]!=0:
                return False
    else:
        if img[x, y] != 0:
            return False
    return True

def getP(ans,index,axis):
    if pArr[index]>=0:
        return pArr[index]
    p=0
    for i in range(0,500):
        if not notLegal(ans,i,i,axis):
            p=i
            break
    pArr[index]=p
    return p

def imgRotate(img,data):
    for i in range(0,16):
        t_img=cv2.resize(process(img,i,3),(500,500),interpolation=cv2.INTER_LINEAR)
        t_data=cv2.resize(process(data,i,1),(500,500),interpolation=cv2.INTER_LINEAR)
        # plus=imgPlus(t_img,t_data)
        global pos
        global lst
        name='%05d'%(lst[pos])
        print(pos,name)
        imgDir = output + '/标注图片/' + name + '.jpg'
        dataDir = output + '/标注数据/' + name
        # plusDir = output + '/叠加效果/' + name + '.jpg'
        pos+=1
        plt.imsave(imgDir,t_img)
        np.save(dataDir,t_data)
        # plt.imsave(plusDir, plus)
        # plt.imshow(plus)
        # plt.show()

def process(img,index,axis=3):
    ans = cv2.getRotationMatrix2D((250, 250), 22.5 * index, 1)
    ans = cv2.warpAffine(img, ans, (500, 500))
    if axis == 3:
        ans = np.delete(ans, 3, 2)  # 所在索引，轴
    p = getP(ans, index, axis)
    ans = ans[p:500 - p, p:500 - p]
    return ans

def buildDir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def add_log(Str):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    with open('log.txt','a+') as f:
        f.writelines(Str+str(nowTime)+'\n')

def build_test_set(test_file):
    buildDir(test_output)
    buildDir(test_output+'/X')
    buildDir(test_output+'/Y')
    i=0
    for s in test_file:
        o_name=s.split('.')[0]
        o_imgDir='./标注图片/'+o_name+'.jpg'
        o_dataDir = './标注数据/' + o_name + '.npy'
        name='%05d'%(i)
        print(i,name)
        imgDir = test_output + '/X/' + name + '.jpg'
        dataDir = test_output + '/Y/' + name + '.npy'
        shutil.copy(o_imgDir,imgDir)
        shutil.copy(o_dataDir,dataDir)
        i+=1

if __name__ == '__main__':
    add_log('开始时间：')
    buildDir(output)
    buildDir(output+'/标注图片')
    buildDir(output+'/标注数据')
    # buildDir(output+'/叠加效果')
    myFiles=None
    for (root, dirs, files) in os.walk('标注数据'):
        myFiles=files
        break
    random.shuffle(myFiles)
    train_file=myFiles[:400] #截取前400张作为训练集
    test_file=myFiles[400:]  #截取后136张作为测试集
    build_test_set(test_file)
    length=len(train_file)*16  #旋转16个角度
    global lst
    lst=build_shuffle_list(length)
    for s in train_file:
        name=os.path.splitext(s)[0]
        # print(name)
        imgName='标注图片/'+name+'.jpg'
        dataName='标注数据/'+name+'.npy'
        img=plt.imread(imgName)
        data=np.load(dataName)
        imgRotate(img,data)
    add_log('结束时间：')
    # os.system('shutdown -s')

