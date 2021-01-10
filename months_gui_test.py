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
        # self.background_image = tk.PhotoImage(file='background_four.png')
        # background_image = ImageTk.PhotoImage(Image.open('background.png'))
        backgound_label = tk.Label(self.master, image=self.background_image)
        backgound_label.place(relwidth=1, relheight=1)
        backgound_label.pack()
        
        # May have to use this frame stuff to put buttons on
        #frame = tk.Frame(self.master)
        frame = tk.Frame(root, bg='#000000', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=.5, relheight=.75, anchor='n')

        entries = os.listdir("\\Users\\zrodr\\Documents\\ThoughtJourneys\\months")
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

        for entry in valid_entries:
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