from tkinter import *
import requests
import pyotp
from tkinter import messagebox
import time
from threading import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

window = Tk()
window.title("Authenticator")
window.geometry("400x400")
window.config(padx=40, pady=40)
totp= pyotp.TOTP("JBSWY3DPEHPK3PXP")
print(totp.now())
def t1():
    t1= Thread(target=sub)
    t1.start()

def sub():
    r1=in1.get()
    r2=in2.get()
    r3=in3.get()
    p1=f"https://www.authenticatorApi.com/pair.aspx?AppName={r1}"
    p2=f"&AppInfo={r2}"
    p3=f"&SecretCode={r3}"
    q1=p1+p2+p3
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(q1)
    time.sleep(12)

    n1 = Toplevel(window)
    n1.title("Authenticator")
    n1.geometry("400x400")
    n1.config(padx=40, pady=40)

    def t2():
        tz2 = Thread(target=reg)
        tz2.start()

    def reg():
        po1 = pin1.get()
        po2 = sec1.get()
        re_end = f"https://www.authenticatorApi.com/Validate.aspx?Pin={po1}&SecretCode={po2}"
        response = requests.get(re_end)
        ab = (response.text)
        messagebox.showinfo('information', f'{ab} is ypur response code')
    pin = Label(n1, text="Pin")
    pin.grid(column=0, row=1)

    secret_key = Label(n1, text="Secret key")
    secret_key.grid(column=0, row=2)

    auth = Label(n1, text="Authenticator")
    auth.grid(column=1, row=0)

    pin1 = Entry(n1)
    pin1.grid(column=1, row=1)

    sec1 = Entry(n1)
    sec1.grid(column=1, row=2)

    ba12 = Button(n1, text="Submit", command=t2)
    ba12.grid(column=1, row=3)

app_name = Label(text="App name")
app_name.grid(column=0, row=1)

app_info =Label(text="App info")
app_info.grid(column=0, row=2)

secret_code=Label(text="Secret code")
secret_code.grid(column=0, row=3)

authenticator=Label(text="Authenticator")
authenticator.grid(column=1, row=0)

in1=Entry()
in1.grid(column=1, row=1)

in2=Entry()
in2.grid(column=1, row=2)

in3=Entry()
in3.grid(column=1, row=3)

b1 =Button(text="Submit", command=t1)
b1.grid(column=1, row=4)

window.mainloop()