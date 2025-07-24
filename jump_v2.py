import pyautogui
import time
import tkinter as tk
import keyboard

xs=0
ys=0
xe=0
ye=0
length=0

# 起点
def start_point():
    global xs,ys
    s_p=pyautogui.position()
    xs=s_p.x
    ys=s_p.y
    sp.config(text=f"起点({xs},{ys})")
# 终点
def end_point():
    global xe,ye
    e_p=pyautogui.position()
    xe=e_p.x
    ye=e_p.y
    ep.config(text=f"终点({xe},{ye})")
    global length
    # 3.计算距离和时间
    dx=abs(xe-xs)/100
    length=dx
    length_label.config(text=f"两点距离{length}")
    if length<=0.72:k=0.27
    elif (length>=0.73)&(length<=0.83):k=0.28
    elif (length>=0.84)&(length<=1.04):k=0.29
    elif (length>=1.05)&(length<=1.17):k=0.30
    elif (length>=1.18)&(length<=1.24):k=0.31
    elif (length>=1.25)&(length<=1.32):k=0.32
    elif (length>=1.33)&(length<=1.57):k=0.33
    elif (length>=1.58)&(length<=1.77):k=0.34
    elif (length>=1.78)&(length<=2.09):k=0.35
    elif (length>=2.1)&(length<=2.27):k=0.36
    elif (length>=2.28)&(length<=2.54):k=0.37
    else:k=0.38
    start_jump(k)

# 开始跳跃
def start_jump(k):
    # 4.执行跳跃
    duration=length*k # 需要慢慢试出来
    length_label.config(text=f"两点距离{length}\n蓄力时间{duration}")
    # moveto()
    pyautogui.moveTo(xe,ye)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

root=tk.Tk()
root.geometry("300x400")
root.title("跳一跳")

tk.Label(root,text="确定起点(Q)和终点(F)").pack(pady=10)

tk.Button(root,text="起点",command=start_point).pack()
sp=tk.Label(root,text="起点坐标")
sp.pack()
keyboard.add_hotkey('q', start_point)

tk.Button(root,text="终点",command=end_point).pack()
ep=tk.Label(root,text="终点坐标")
ep.pack()
keyboard.add_hotkey('f', end_point)

length_label=tk.Label(root,text=f"两点间的距离\n蓄力所需时间")
length_label.pack()

# 确保程序结束时清除热键
def on_closing():
    keyboard.unhook_all_hotkeys()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()



