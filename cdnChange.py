from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msgbox
from tkinter import font
import os
import shutil
import subprocess
import time
import subprocess

from tkinterweb import HtmlFrame #import the HTML browser

import random

root = Tk()
root.geometry("400x430")
root.title(" ************ CDN Changer ")
root.resizable(False, False)

style = ttk.Style()
style.configure("TRadiobutton",foreground="black", font="Arial 10")

# 3열 frame : copyright 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------
# separator bar with copyright
# sp = ttk.Separator(root, orient="horizontal")
# sp.pack(side="bottom", fill="both")
frame3 = LabelFrame(root, width=400, height=20, relief="flat", bd=1)
frame3.pack(side="bottom", padx=10, pady=(10,10), fill="both")
mediumFont = font.Font(size=8, family="Arial")
copyrightLabel = Label(frame3, text='Copyright 2024. YOONSEO All Rights Reserved.', font=mediumFont)
copyrightLabel.pack(side="bottom")
# 3열 frame 끝 : copyright 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------


# 2열 frame : Check My Status 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------
# frame2 = LabelFrame(root, width=400, height=20, text="Check My Status" ,relief="groove", bd=3)
frame2 = LabelFrame(root, width=400, height=50, text="Check My Status" ,relief="solid", bd=1)
frame2.pack(side="bottom", padx=10, pady=(10,10), fill="both")

def open_url(countryName):
    randomInt = random.randint(0, 100)
    v = str(randomInt)
    TW_cdn_check_url = "http://************/Images/which.html?v="+v
    JP_cdn_check_url = "http://************/Images/which.html?v="+v
    KR_cdn_check_url = "http://************/Images/which.html?v="+v
    
    # open_url = TW_cdn_check_url if countryName == "TW" else JP_cdn_check_url
    if countryName == "TW":
        open_url=TW_cdn_check_url
    elif countryName == "JP":
        open_url=JP_cdn_check_url
    elif countryName == "KR":
        open_url=KR_cdn_check_url         
    
    # countryName = "[TW]" if countryName == "TW" else "[JP]"
    if countryName == "TW":
        countryName = "[TW]"
    elif countryName == "JP":
        countryName = "[JP]"
    elif countryName == "KR":
        countryName = "[KR]"

    # old version : webview >> can't open popup webview issue at windows11 
    # webview.create_window( countryName+"  Which CDN ? ", open_url, width=300, height=150)
    # webview.start()

    # new test code 
    top = Toplevel(root)
    top.geometry("350x150")
    top.title(countryName + " Which CDN server ? ")
    view = HtmlFrame(top)
    view.clear_visited_links()
    view.enable_caches(enabled=False)
    view.load_url(open_url)
    view.pack(fill="both", expand=True)

tw_frame = Frame(frame2, width=13, height=1, relief="solid", bd=1)
tw_frame.pack(side="left", padx=(20, 5), pady=13)
TW_status_btn = Button(tw_frame, width=13, height=1, text="TW Status", command=lambda:open_url("TW"))
TW_status_btn.pack(side="left", fill="both")

jp_frame = Frame(frame2, width=13, height=1, relief="solid", bd=1)
jp_frame.pack(side="left", padx=(10, 5), pady=13)
JP_status_btn = Button(jp_frame, width=13, height=1, text="JP Status", command=lambda:open_url("JP"))
JP_status_btn.pack(side="left", fill="both")

kr_frame = Frame(frame2, width=13, height=1, relief="solid", bd=1)
kr_frame.pack(side="left", padx=(10, 20), pady=13)
KR_status_btn = Button(kr_frame, width=13, height=1, text="KR Status", command=lambda:open_url("KR"))
KR_status_btn.pack(side="left", fill="both")

# 2열 frame 끝 : Check My Status 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------


# 1열 frame : 나라, QA,LIVE 선택 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------
# frame1 = Frame(root, width=400, height=150, relief="ridge", bd=5)
frame1 = Frame(root, width=400, height=800, relief="solid", bd=1)
frame1.pack(side="top", padx=10, pady=(20,1))
mainFont = font.Font(size=11, family="Arial")
size10 = font.Font(size=10, family="Arial")
size11 = font.Font(size=11, family="Arial")
# 1열 하단 change 버튼
def changeCdnServer():
    selectedCountry = whichCountry.get()
    # countryName = "TW" if selectedCountry == 0 else "JP"
    if selectedCountry == 0:
        countryName = "TW"
    elif selectedCountry == 1:
        countryName = "JP"
    elif selectedCountry == 2:
        countryName = "KR"     
    selectedSever = whichCdn.get()
    p_var.set(0)
    progressBar.update()
    time.sleep(0.2)

    hostPath = r"C:\Windows\System32\drivers\etc"
    fullPath = r"C:\Windows\System32\drivers\etc\hosts"
    TW_TARGET_LIST =["************.com","************.com","************.com"]
    JP_TARGET_LIST =["************.co.jp", "************.co.jp", "************.co.jp"]
    KR_TARGET_LIST =["************.co.kr", "************.co.kr", "************.co.kr"]
    
    # selected_target_list = TW_TARGET_LIST if selectedCountry == 0 else JP_TARGET_LIST
    if selectedCountry == 0:
        selected_target_list = TW_TARGET_LIST
    elif selectedCountry == 1:
        selected_target_list = JP_TARGET_LIST
    elif selectedCountry == 2:
        selected_target_list = KR_TARGET_LIST     

    TW_QA_CDN = "************.net"
    JP_QA_CDN = "************.net"
    KR_QA_CDN = "************.net"
    # selected_target_cdn = TW_QA_CDN if selectedCountry == 0 else JP_QA_CDN
    if selectedCountry == 0:
        selected_target_cdn = TW_QA_CDN
    elif selectedCountry == 1:
        selected_target_cdn = JP_QA_CDN
    elif selectedCountry == 2:
        selected_target_cdn = KR_QA_CDN
    needRegister = True

    try:
        if os.path.exists(fullPath):
            # timeNow = datetime.now().strftime("%Y%m%d_%H_%M_%S")    
            # shutil.copy(hostPath+"\hosts",hostPath+"\hosts_bk_python_"+timeNow)
            shutil.copy2(fullPath,hostPath+r"\hosts_backup_by_cdnChanger")
        else:
            print("파일 미존재!!!")
            msgbox.showerror(title="Warning", message="[ERROR] There is no hosts file.")

    except Exception as err:
            print("hosts 파일 복사 중 에러 발생 : " + str(err))
            msgbox.showerror(title="Warning", message="[ERROR] can't copy hosts file.")

    try:
        with open(r"C:\Windows\System32\drivers\etc\hosts","r", encoding="utf-8") as fileObj:
            lines = fileObj.readlines()
            with open(r"C:\Windows\System32\drivers\etc\hosts","w", encoding="utf-8") as newFile:
                    # raise Exception(" !! force an error to occur !!  ")
                    if selectedSever == 1:
                        for index, li in enumerate(lines):
                            p_var.set((index/len(lines)) * 100)
                            progressBar.update()
                            
                            li = li.rstrip("\n")
                            if any(target in li for target in selected_target_list):
                                if li.startswith("#"):
                                    replaceString = li
                                else:
                                    replaceString = li.replace(li, "#"+li)
                                newFile.write(replaceString+"\n")

                            else:
                                newFile.write(li+"\n")   

                    elif selectedSever == 0:
                        result = subprocess.run(['ping', '-n', '1', selected_target_cdn], capture_output=True, text=True, check=True)
                        newIp = result.stdout.split("[")[1].split("]")[0]
                        
                        for index, li in enumerate(lines):
                            p_var.set((index/len(lines)) * 100)
                            progressBar.update()
                            
                            li = li.rstrip("\n")
                            if any(target in li for target in selected_target_list):
                                # Already registered >> just change ip to new one
                                needRegister = False
                                replaceString = li.split(" ")[1]
                                newFile.write(newIp + " " + replaceString+"\n")
                            else:
                                # Existing hosts file contents + register new qa cdn ip at the end of file.
                                if (index == len(lines) - 1) and needRegister:
                                    newFile.write(li+"\n\n")
                                    newFile.write("# [************ CDN Changer] Register for "+countryName+"\n")
                                    for domain in selected_target_list:
                                        newFile.write(newIp + " " +domain+"\n")        
                                else:
                                    newFile.write(li+"\n")
                    msgbox.showinfo(title="Complete", message="CDN Changed !")     
                            
    except Exception as e:
        # fileObj.close()
        # newFile.close()
        print("hosts 파일 읽기 및 쓰기 에러 발생 " + str(e))
        msgbox.showwarning(title="Warning", message="[ERROR] can't read and write hosts file.")
        try:
            shutil.copy2(hostPath+r"\hosts_backup_by_cdnChanger",fullPath)
        except Exception as e2:   
            print("hosts rollback copy error 발생 " + str(e2))
            msgbox.showwarning(title="Warning", message="[ERROR] can't rollback hosts file.")

# 1 의 1-1 하단 프레임 (change 버튼)
bottom_frame = Frame(frame1, width=45, height=10, relief="solid", bd=1)
bottom_frame.pack(side="bottom", padx=(250,18), pady=(4,10))
changeBtn = Button(bottom_frame, width=45, height=1, text=" Change ", command=changeCdnServer)
changeBtn.pack(side="right", fill="both")
# 1열 Progress Bar Frame
progressFrame = LabelFrame(frame1, width=380, height=300, text="Progress Bar", relief="flat", bd=3, font=size10)
progressFrame.pack(side="bottom", padx=(20,20) , pady=(5,10), fill="both")
p_var = DoubleVar()
progressBar = ttk.Progressbar(progressFrame, length=380 ,maximum=100, variable=p_var, mode="determinate")
# progressBar.pack(padx=10, pady=(5,5), fill="both")
progressBar.pack(fill="both")
# 1열 좌측 LabelFrame
left_label_frame = LabelFrame(frame1, width=200, height=600, text=" Country ", font=mainFont, relief="solid", bd=1)
left_label_frame.pack(side="left", padx=(20,10), pady=10, fill="both")
whichCountry = IntVar()
radio1 = ttk.Radiobutton(left_label_frame, text="TW", value="0", variable=whichCountry)
radio1.pack(side="top", pady=(15,5))
radio2 = ttk.Radiobutton(left_label_frame, text="JP", value="1", variable=whichCountry)
radio2.pack(side="top", pady=(5,5))
radio3 = ttk.Radiobutton(left_label_frame, text="KR", value="2", variable=whichCountry)
radio3.pack(side="top", pady=(5,15))
# 1열 우측 LabelFrame
right_label_frame = LabelFrame(frame1,width=200, height=600, text=" Which CDN you want to connect ? ", font=mainFont, relief="solid", bd=1)
right_label_frame.pack(side="right", padx=(10,20), pady=10, fill="both")
whichCdn = IntVar()
radio1 = ttk.Radiobutton(right_label_frame, text="QA CDN", value="0", variable=whichCdn)
radio1.pack(side="top", pady=(15,1))
radio2 = ttk.Radiobutton(right_label_frame, text="Live CDN", value="1", variable=whichCdn)
radio2.pack(side="top", pady=(25,15))
# 1열 frame 끝 : 나라, QA,LIVE 선택 영역 -----------------------------------------------------------------------------------------------------------------------------------------------------------





root.mainloop()