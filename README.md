# Overview
To recognize crack on road ,building and other civil-structure, 
using deeplearning ,especially semantic-segmentation tech of computer vision to recognize crack is a better way.

But establish of dataset is the first step of whole work.
To accomplish this mission, I build a semantic-segmentation dataset of rock crack and CT rock slice crack . 
 

# How to download 

## for rock-crack and concrete-crack

[rock-crack and concrete-crack dataset](http://47.94.192.51/static/files/images.tar.gz)

```bash
wget -c http://47.94.192.51/static/files/images.tar.gz
```

## for CT-slice-crack 


[CT-slice-crack  dataset](http://47.94.192.51/static/files/CT_images.tar.gz)

```bash
wget -c  http://47.94.192.51/static/files/CT_images.tar.gz
```

# Example

## rock crack

![](example/rock.jpg)
![](example/rock_gt.jpg)

## concrete crack
![](example/concrete.jpg)
![](example/concrete_gt.jpg)

## CT-slice crack

![](example/CT.jpg)
![](example/CT_gt.jpg)



# dataset-kit

├── dataset-kit

│   ├── `amplifyData-16.py`  (for data enhancement)

│   ├── `amplifyData.py`   (for data enhancement)

│   └── `calc-mean.py`    (for data preprocess)


# Thanks

Thanks for ZhangLiao（张辽） and WangAo （王傲）'s help

# TODO

[amplifyData-16.py](dataset-kit/amplifyData-16.py) have some problem, I need time to refactor it.