import os,shutil
import numpy as np
import pylab as plt
import cv2
import datetime
import random
from scipy.misc import imsave
import scipy
from skimage import io

input='images'

if __name__ == '__main__':
    myFiles=[]
    for (root, dirs, files) in os.walk(input):
        for file in files:
            if file.find("_gt")<0 and file.find('.jpg')>=0:
                myFiles.append(file)
        break
    sum = []
    for i,s in enumerate(myFiles):
        # if i>100:
        #     break
        name=os.path.splitext(s)[0]
        print(i,name)
        imgName=f'{input}/'+name+'.jpg'
        # dataName=f'{input}/'+name+'_gt.jpg'
        img=plt.imread(imgName)
        # data=plt.imread(dataName)
        c=[0]*3
        mean=[0]*3

        for j in range(3):
            c[j]=img[:,:,j].squeeze()
            mean[j]=np.mean(c[j])
        sum.append(mean)

    sum=np.array(sum)
    ans=np.mean(sum, axis=0)
    print(ans)
    
