import time  # 导入time模块，用于控制时间
import keyboard  # 导入keyboard模块，用于监听键盘按键
import pyautogui  # 导入pyautogui模块，用于实现鼠标点击操作
import threading  # 导入threading模块，用于多线程操作
from tkinter import Tk, Label, Entry, Button, BOTTOM  # 导入tkinter模块，用于创建图形用户界面


clickThreadState = False  # 点击线程初始化为None


# 获取用户输入的内容
def getInput():
    clicks = clicksEntry.get() if clicksEntry.get() else 100  # 获取输入的点击次数，如果没有输入则使用默认值
    speed = speedEntry.get() if speedEntry.get() else 0.01  # 获取输入的点击间隔，如果没有输入则使用默认值
    delay = delayEntry.get() if delayEntry.get() else 1  # 获取输入的延迟执行时间，如果没有输入则使用默认值
    return int(clicks), float(speed), int(delay)  # 返回点击次数、点击间隔、延迟执行时间


# 点击器
def clicker():
    global clickThreadState  # 声明全局变量clickThreadState
    clicks, speed, delay = getInput()  # 获取用户输入的内容
    pyautogui.PAUSE = speed  # 设置pyautogui的点击间隔

    for _ in range(delay): 
        if not clickThreadState: break  # 如果点击线程存在且正在运行中则跳出循环
        countdownLabel['text'] = f"倒计时 {delay - _} 秒"  # 显示倒计时
        time.sleep(1)  # 倒计时1秒

    countdownLabel['text'] = ""  # 倒计时结束，清空倒计时标签

    for _ in range(clicks): # 循环执行指定次数的点击操作
        if not clickThreadState: break  # 如果点击线程存在且正在运行中则跳出循环
        pyautogui.click() # 循环执行指定次数的点击操作

    clickThreadState = False  # 点击线程状态设置为None，以结束点击操作
    clickButton['text'] = "开始点击"  # 更改按钮文本为"开始点击"


# 运行点击器
def runClicker():
    global clickThreadState  # 声明全局变量clickThreadState

    if clickThreadState: # 如果点击线程正在运行中
        clickThreadState = False  # 设置点击线程状态为False，以停止点击操作
        return  # 如果点击线程正在运行中则直接返回
    
    clickThreadState = True  # 设置点击线程状态为False，以停止点击操作
    clickButton['text'] = "停止点击"  # 更改按钮文本为"停止点击"

    clickThread = threading.Thread(target=clicker)  # 创建一个新的线程来执行clicker方法
    clickThread.start()  # 启动线程

 
# 键盘按键事件处理方法
def onKeyPressed(event): 
    if event.name == "f4": runClicker()


# 创建窗口
window = Tk()  # 创建一个窗口对象
window.title("连点器")  # 设置窗口标题为"连点器"
window.geometry("250x300")  # 设置窗口大小为250x280
window.resizable(False, False)  # 设置窗口大小不可变
window.attributes("-topmost", True)  # 窗口置顶

clicksLabel = Label(window, text="点击次数(默认100):")  # 创建一个标签显示文本"点击次数(默认100):"
clicksLabel.pack(pady=5)  # 将标签添加到窗口，并设置垂直外边距为5
clicksEntry = Entry(window)  # 创建一个文本输入框
clicksEntry.pack(pady=5)  # 将文本输入框添加到窗口，并设置垂直外边距为5

speedLabel = Label(window, text="点击间隔(默认0.01)(s):")  # 创建一个标签显示文本"点击间隔(默认0.01)(s):"
speedLabel.pack(pady=5)  # 将标签添加到窗口，并设置垂直外边距为5
speedEntry = Entry(window)  # 创建一个文本输入框
speedEntry.pack(pady=5)  # 将文本输入框添加到窗口，并设置垂直外边距为5

delayLabel = Label(window, text="延迟执行(默认1)(s):")  # 创建一个标签显示文本"延迟执行(默认0)(s):"
delayLabel.pack(pady=5)  # 将标签添加到窗口，并设置垂直外边距为5
delayEntry = Entry(window)  # 创建一个文本输入框
delayEntry.pack(pady=5)  # 将文本输入框添加到窗口，并设置垂直外边距为5

clickButton = Button(window, text="开始点击", command=runClicker)  # 创建一个按钮，点击后调用clicker的startClicks方法
clickButton.pack(pady=10)  # 将按钮添加到窗口，并设置垂直外边距为10
statusLabel = Label(window, text="(按 “F4” 开始或停止执行程序)")  # 创建一个标签显示文本"(F6:开始执行, F7:停止执行)"
statusLabel.pack(side=BOTTOM)  # 将标签添加到窗口底部

countdownLabel = Label(window, text="") # 倒计时标签
countdownLabel.pack(pady=5)  # 将标签添加到窗口，并设置垂直外边距为5
countdownEntry = Entry(window)  # 创建一个文本输入框
countdownEntry.pack(pady=5)  # 将文本输入框添加到窗口，并设置垂直外边距为5

keyboard.on_press(onKeyPressed)  # 监听键盘按键事件，调用onKeyPressed方法进行处理

window.mainloop()  # 运行窗口主循环
