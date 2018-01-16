#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。

# Tkinter
# 梳理一下概念：
# 我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
# 所以，我们的代码只需要调用Tkinter提供的接口就可以了。


from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='Hello, world!')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    # 加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)



# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。
# 设置窗口标题:
app = Application()

app.master.title('Hello World')
# 主消息循环:
app.mainloop()

# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
# 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
