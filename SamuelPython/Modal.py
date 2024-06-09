import tkinter as tk
from ai import GPT
import pyperclip

class Modal:
    def __init__(self, app):
        self.app = app
        self.window = app.window
    
    
    def showNonBlockingPopup(self, title, label):
        
        popup = tk.Toplevel(self.window)
        popup.geometry("300x200")
        popup.title(title)
        
        # Add a label to the popup window
        label = tk.Label(popup, text=label)
        label.pack(pady=20) 

        # Add a button to close the popup window
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=20)

    def showBlockingPopup(self, title, label):
        
        popup = tk.Toplevel(self.window)
        popup.geometry("300x200")
        popup.title(title)
        
        # Add a label to the popup window
        label = tk.Label(popup, text=label)
        label.pack(pady=20)
        
        # Add a button to close the popup window
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=20)
        
        popup.transient(self.window)
        popup.grab_set()
        self.window.wait_window(popup)
        
    def returnAndDestroy(self):
        text = self.inputEntry.get()
        self.app.modalReturn = text
        self.popup.destroy()
        
    def showInputPopup(self, title, label):
        
        
        self.popup = tk.Toplevel(self.window)
        self.popup.geometry("300x200")
        self.popup.title(title)
        
        # Add a label to the popup window
        label = tk.Label(self.popup, text=label)
        label.pack(pady=20)
        
        self.inputEntry = tk.Entry(self.popup)
        self.inputEntry.pack(pady=20)
        
        # Add a button to close the popup window
        close_button = tk.Button(self.popup, text="Close", command=self.returnAndDestroy)
        close_button.pack(pady=20)
        
        
        self.popup.transient(self.window)
        self.popup.grab_set()
        self.window.wait_window(self.popup)
    
    
    def applySelectedThenDestroy(self, text, pop):
        selectedtext = ''
        
        try:
            selectedtext = text.get(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            print('nothing selected')
        self.app.modalReturn = selectedtext
        pyperclip.copy(selectedtext)
        pop.destroy()
        
    def sendMessage(self, text, gpt):
        message = self.get_last_line(text)
        response = ''
        
        if gpt.new:
            response = gpt.newChat("new chat", message)
            gpt.new = False
        else:
            response = gpt.continueChat("new chat", message)
    
        text.insert(tk.END, "\nGPT> \n" +response + "\n")
        
    def get_last_line(self, text):
        last_line_index = text.index('end-1c').split('.')[0]
        last_line = text.get(f"{last_line_index}.0", tk.END)
        return last_line
    
    def showChatPopup(self, title):
        
        gpt = GPT(model='gpt-3.5-turbo')
        gpt.new = True
        
        popup = tk.Toplevel(self.window)
        popup.geometry("600x400")
        popup.title(title)
        
        # Add a label to the popup window
        label = tk.Label(popup, text='GPT-3.5-turbo')
        label.pack(pady=20)
        
        # add a text area for our conversation
        text = tk.Text(popup, width=30)
        text.pack(pady=20)
        
        # Add a button to apply selected conversation to your chapter
        close_button = tk.Button(popup, text="Send", command= lambda t = text, g = gpt: self.sendMessage(t, g))
        close_button.pack(pady=20)
        
        # Add a button to apply selected conversation to your chapter
        close_button = tk.Button(popup, text="Apply Selection", command= lambda t=text, x=popup: self.applySelectedThenDestroy(t, x))
        close_button.pack(pady=20)
        
        popup.transient(self.window)
        popup.grab_set()
        self.window.wait_window(popup)