#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 12:50:15
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os
import io

from PIL import Image

def open_img(img_path) -> list:
    """Open img by path

    Args:
        img_path: path/s of img/s

    Returns:
        ret: list of img
    """
    ret = None
    return ret

def subtile_concat(imgs:list, sub_range:tuple) -> Image:
    """

    Args:
        imgs: 顺序化的图片对象
        sub_range: (high, low) 字幕范围

    Returns:
        ret: 
    """
    ret = None
    return ret

img_path = ["./1.png", "./2.png"] # 按照图片顺序

imgs = []
for _path in img_path:
    _img = Image.open(_path)
    imgs.append(_img)

sub_range = (630, 700) # 定义字幕的顶部和底部坐标


x = 0
y = sub_range[0]
w, h = imgs[0].size
crop_h = sub_range[1] - sub_range[0]


crops = []
for i in range(1, len(imgs)):
    region = imgs[i].crop((x, y, x+w, y+crop_h))
    crops.append(region)


target = Image.new('RGB',(w, h + crop_h*( len(imgs)-1 )))
target.paste(imgs[0],(0, 0, w, h))

left = 0 + h
right = crop_h + h


for image in crops:
    target.paste(image,(0, left, w, right))
    left += crop_h #从上往下拼接，左上角的纵坐标递增
    right += crop_h #左下角的纵坐标也递增

target.save("./test.png")

