import bs4
import requests
from io import BytesIO
import win32clipboard
from PIL import Image
import pyperclip
import pyautogui
import time
import os

#写入剪贴板文本
def copy_data(text_data):

    time.sleep(2)
    # pyautogui.moveTo(x=1023, y=831,duration=2,)
    # pyautogui.click()

    pyperclip.copy(text_data)
    text = pyperclip.paste()
    print("获取剪切板内容：" + text)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(3)


#剪贴板设置
def send_to_clipboard(clip_type, data):

    time.sleep(2)

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(3)

#读取本地图片
def read_img(image_path):

    image = Image.open(image_path)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)

# 获取图片并保存
def get_img(url,file_name):

    res = requests.get(url)
    with open('./img/'+file_name+'.png','wb') as f:
        f.write(res.content)

    #将图片复制进入剪贴板
    read_img('./img/'+file_name+'.png')
    time.sleep(1)

# 获取html的文本
def get_conent(path):

    with open(path,'r',encoding='utf-8') as f:
        res = f.read()

    bs = bs4.BeautifulSoup(res,"html.parser")
    soup = bs.find('div',class_='content-wrapper')

    file_name = 0
    for con in soup.contents:

        if bs4.BeautifulSoup(str(con),"html.parser").find('img') != None:
            con = bs4.BeautifulSoup(str(con),"html.parser")
            get_img(con.find('img')['src'],str(file_name))
            file_name +=1

        #空值判断
        elif bs4.BeautifulSoup(str(con),"html.parser") == None:
            continue
        else:
            con = bs4.BeautifulSoup(str(con),"html.parser")
            if con.text == '\n':
                pass
            else:
                copy_data(con.text)
                # print([con.text])
if __name__ == '__main__':
    
    # #通过交互输入选择文件
    # file_list = os.listdir('./分享物料')
    # for file in file_list:
    #     if '.md' in file:
    #         file_list.remove(file)
    # for file in file_list:
    #     print('序号：',file_list.index(file),'文件名：',file)
    # num = input('请输入要分享的文件序号：')

    # path = "./分享物料/" + file_list[int(num)]

    path = "./分享物料/OA高效办公复习资料.html"
    get_conent(path)