from Application import Application

app = Application()
app.setup()

# 这是一个无限循环，只要app的窗口打开，它就会不停的听window的事件
app.update()



