import eel
eel.init("gui") # eel.init (網頁的資料夾)
def build(x):
    print(x)
eel.goPython()(build)
eel.start("index.html",size = (600,400)) #eel.start(html名稱, size=(起始大小))