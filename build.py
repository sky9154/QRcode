# -*- coding: utf-8 -*-
from MyQR import myqr
import requests
import eel
import cv2
eel.init("gui") # eel.init (網頁的資料夾)

@eel.expose
def buildQRcode(url, img, name):
    kirito = myqr
    if "https" in img or "http" in img:   # 使用in運算子檢查
        imgURL = img
        img_data = requests.get(imgURL).content
        if ".gif" in img or ".GIF" in img:
            img = "./picData.gif"
        else:
            img = "./picData.png"
        with open(img, "wb") as f:
            f.write(img_data)
        f.close()
    version, level, qr_name = kirito.run(
        words = url,                  # 網址
        version = 1,                  # 二維碼的邊長
        picture = img,                # 二維碼的背景圖片
        colorized = True,             # 背景圖片是否採用彩色
        save_name = name,     # 檔案名稱
    )
    print("產生成功！！！")
    if ".gif" in name or ".GIF" in name:
        print("目前不支援 gif 顯示")
    else:
        name = cv2.imread(name)
        cv2.imshow("Finsh !!!", name)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

eel.start("index.html",size = (600,400), post = 8763) #eel.start(html名稱, size=(起始大小))