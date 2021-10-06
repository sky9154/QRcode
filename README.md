# QRcode 產生器
**利用 Python 當中的 MyQR module 來建立一款可變更 QRcode 背景圖片的程式**

背景圖支援市面上常見的圖檔格式，且支援 git 動態圖檔，並且利用 Eel 來建立 GUI 桌面應用程式，而圖檔的來源不侷限於本地端的檔案，還支援線上的圖檔，以作為 QRcode 的背景使用。
## 前置作業
### 1.安裝 Python
在使用 QRcode 產生器之前你要先安裝 Python
* [這是 Python 下載頁面的鏈接](https://www.python.org/downloads)
* [這是在各個操作系統上安裝 Python 的指南](https://wiki.python.org/moin/BeginnersGuide/Download)
### 2.確認是否安裝軟體包管理系統（pip）
於命令列中輸入 `python -m pip --version` 進行確認是否已安裝 pip ，如果輸入後有顯示 pip 版本訊息代表已經安裝好 pip 了，可跳過此步驟，如果還未安裝，請先下載 [get-pip.py](https://bootstrap.pypa.io/get-pip.py) 以進行後續的步驟。
開啟 cmd 命令視窗，輸入`cd "get-pip.py 目前所在的資料夾"` ，將 cmd 的所在目錄移至 get-pip.py下載的資料夾位置，然後執行 `python get-pip.py` 來進行安裝 pip。
最後一樣使用 `python -m pip --version` 確認 pip 是否已安裝完畢。
[pip 官方說明](https://pip.pypa.io/en/stable/)
### 3.安裝必要項目
此程式利用到了 4 款 Python 的第三方 module ，可以透過命令列來安裝，使應用程式可以正常運作
[MyQR](https://github.com/x-hw/amazing-qr)（用來生成 QRcode 並且將圖片與之結合）：
```
pip install myqr
```
[requests](https://github.com/psf/requests)（將線上的圖片儲存到本地端來執行）：
```
pip install requests
```
[Eel](https://github.com/ChrisKnott/Eel)（將 Python 的程式以網頁方式呈現）：
```
pip install eel
```
[OpenCV](https://github.com/opencv/opencv-python)（將合成後的圖片顯示出來）：
```
pip install opencv-python
```
### 4.安裝 QRcode 產生器
從 [Github](https://github.com/sky9154/QRcode) 上進行手動下載，或是使用 git 下載完整程式碼：
```
git clone https://github.com/sky9154/QRcode.git
```
## 如何使用
### 1. 開啟程式：
使用 CMD 視窗輸入下列指令：
```
cd 程式所在的資料夾
python3 build.py
```
### 2. 輸入需儲存到 QRcode 的網址：
![](https://i.imgur.com/uyVYfwG.png)

### 3. 輸入背景圖片的位置（本地端、線上皆可）：
![](https://i.imgur.com/OCLFeEE.png)
### 4. 輸入儲存後的檔案名稱（如果背景圖使用 gif 的話，副檔名也需設為 gif 格式）：
![](https://i.imgur.com/a8rkr7e.png)
### 5. 最後點擊 **Build** 產生 QRcode（如果副檔名為 gif 格式的話，將不會顯示預覽，其餘則反之）：
![](https://i.imgur.com/qnY6ts6.gif)
### 完整程式執行過程
![](https://github.com/sky0966548546/QRcode/blob/main/assets/images/demo.gif)