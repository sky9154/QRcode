# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from MyQR import myqr
import os
kirito = myqr
img = input("將背景圖案放到這裡:")
names = input("請輸入QR Code名稱:")
url = input("請輸入需轉換的網址:")

version, level, qr_name = kirito.run(
    words=url,                  # 網址
    version=1,                  # 通關率
    level='H',                  # 調整圖片方位
    picture=img,                # 設定背景
    colorized=True,             # 是否為彩色
    contrast=2.0,               # 對比
    brightness=1.0,             # 亮度
    save_name=names+'.gif',     # 檔案名稱
    save_dir=os.getcwd()        # 儲存在當前路徑
)
