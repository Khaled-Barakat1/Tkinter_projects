import pytube
import time
from pytube import YouTube 
from tkinter import *

root = Tk()
root.geometry('200x100')

dow_path = "C:/Users/khale/Downloads"


def main_fun(): 
    choose_q = qulity.get()

    qulityes = {
    "1080": 37 ,
    "720": 22 ,
    "480": 44 ,
    "360": 18 ,
    "audio": 141 ,
    "choose qulity":'valed'
    }
    

    qul = qulityes[choose_q]
    url = 'https://youtu.be/Fywq065U7-E?t=44'

    if qul == 'valed':
        qulity_choose_label = Label(lower_frame, text = 'choose the qulity ', fg='red')
        qulity_choose_label.place(width=200, height= 35)
    elif url == '' :
        url_choose_label = Label(lower_frame, text = 'enter the video url ', fg='red')
        url_choose_label.place(width=200, height= 35)
    else:

        url_check_label = Label(lower_frame, text = 'the video url is : '+url, fg='green')
        url_check_label.place(width=200, height= 35)
        time.sleep(2)
        qulity_check_label = Label(lower_frame, text = 'the video qulity is : '+ choose_q, fg='green')
        qulity_check_label.place(width=200, height= 35)
        time.sleep(2)
        yt = pytube.YouTube(url)
        title_check_label = Label(lower_frame, text = 'the video is found and the title is : '+ yt.title, fg='green')
        stream = yt.streams.get_by_itag(qul)
        stream.download(dow_path)
        done_label= Label(lower_frame,text='done', fg='green')
        done_label.place(width=200, height= 35)

    
   


uper_frame = Frame(root)
uper_frame.place(width=200, height= 65)

lower_frame = Frame(root)
lower_frame.place(width=200, height= 35, rely= 0.65)

url_label = Label(uper_frame, text="URL :")
url_label.place(relwidth= 0.25,relheight=0.33, rely= 0.05)

url_entry = Entry(uper_frame)
url_entry.place(relwidth= 0.72,relheight=0.33, relx=0.23, rely=0.05)

D_button = Button(uper_frame, text="download",command= main_fun )
D_button.place(relwidth= 0.4,relheight=0.50, rely=0.45, relx=0.6)

qulity = StringVar()
qulity.set('choose qulity')
qulity_box = OptionMenu(uper_frame, qulity, '1080', '720', '480', '360', 'audio')
qulity_box.place(relwidth= 0.6,relheight=0.53,rely=0.45)



root.mainloop()