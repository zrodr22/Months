import tkinter as tk
import os
from VerticalScrollFrame import VerticalScrolledFrame

class Application(tk.Frame):
    def __init__(self, documents_path, master=None):
        super().__init__(master)
        self.documents_path = documents_path
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Use this for deployment
        # self.background_image = tk.PhotoImage(file='../../background_four.png')

        # Use the next comment for development
        # self.background_image = tk.PhotoImage(file='background_four.png')

        # This used to be used for a background. Need to implement with scrolling
        # backgound_label = tk.Label(self.master, image=self.background_image)
        # backgound_label.place(relwidth=1, relheight=1)
        # backgound_label.pack()
        # frame = tk.Frame(root, bg='#000000', bd=5)
        # frame.place(relx=0.5, rely=0.1, relwidth=.5, relheight=.75, anchor='n')

        # May have to use this frame stuff to put buttons on
        frame = tk.Frame(self.master)

        entries = os.listdir(self.documents_path)
        valid_entries = []

        for entry in entries:
            if entry[0] is not '~' and entry[-4:] == 'docx':
                valid_entries.append(entry)

        months = {"January": 0, "February": 1, "March": 2,"April": 3,"May": 4,"June": 5,"July": 6,"August": 7,"September": 8,"October": 9,"November": 10,"December": 11,}

        for i in range(len(valid_entries)):
            month_entry_i = valid_entries[i].split('_')[0]
            year_entry_i = int(valid_entries[i].split('_')[1][0:4])
            for j in range(len(valid_entries)):
                month_entry_j = valid_entries[j].split('_')[0]
                year_entry_j = int(valid_entries[j].split('_')[1][0:4])
                if i != j:
                    if year_entry_i > year_entry_j and i > j:
                        switch = valid_entries[j]
                        valid_entries[j] = valid_entries[i]
                        valid_entries[i] = switch
                    if year_entry_i == year_entry_j:
                        if months[month_entry_i] > months[month_entry_j] and i > j:
                            switch = valid_entries[j]
                            valid_entries[j] = valid_entries[i]
                            valid_entries[i] = switch

        scframe = VerticalScrolledFrame(root)
        scframe.pack()

        for entry in valid_entries:
            if entry[0] is not '~' and entry[-4:] == 'docx':
                btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT, 
                    bg="gray99", fg="black",
                    font="Dosis", text= entry,
                    command=lambda e=entry: self.open_doc(e))
                btn.pack(padx=10, pady=5, side=tk.TOP)

        self.quit = tk.Button(frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_doc(self,doc_name):
        path = self.documents_path + "\\" + doc_name
        os.startfile(path)
        self.master.destroy()

root = tk.Tk()