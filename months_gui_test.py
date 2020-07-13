import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.background_image = tk.PhotoImage(file='../../background_four.png')
        #background_image = ImageTk.PhotoImage(Image.open('background.png'))
        backgound_label = tk.Label(self.master, image=self.background_image)
        backgound_label.place(relwidth=1, relheight=1)
        backgound_label.pack()
        
        # May have to use this frame stuff to put buttons on
        #frame = tk.Frame(self.master)
        frame = tk.Frame(root, bg='#000000', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=.5, relheight=.75, anchor='n')

        entries = os.listdir("\\Users\\zrodr\\Documents\\ThoughtJourneys\\months")
        for entry in entries:
            if entry[0] is not '~' and entry[-4:] == 'docx':
                tk.Button(frame, text=entry, command= lambda e=entry: self.open_doc(e)).pack()

        self.quit = tk.Button(frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_doc(self,doc_name):
        path = "\\Users\\zrodr\\Documents\\ThoughtJourneys\\months\\" + doc_name
        os.startfile(path)
        self.master.destroy()

root = tk.Tk()