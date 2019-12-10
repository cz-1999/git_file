import win32gui

import win32con

import win32clipboard as w

# 发送的消息

msg = "hello world"

# 窗口名字

name = "1802_驻马店_冀春霖"

# 将测试消息复制到剪切板中

w.OpenClipboard()

w.EmptyClipboard()

w.SetClipboardData(win32con.CF_UNICODETEXT, msg)

w.CloseClipboard()

# 获取窗口句柄

handle = win32gui.FindWindow(None, name)
i=0
while True:

#if True:
    # 填充消息

    win32gui.SendMessage(handle, 770, 0, 0)

    # 回车发送消息

    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    i+=1
    if i >= 98:
        break
