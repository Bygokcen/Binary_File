import tkinter as tk
from tkinter import ttk
from create_database_ui import CreateTableUI
from tables_operations import get_table_names
class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DBMS")
        self.geometry("800x600")

        self.notebook= ttk.Notebook(self)
        self.notebook.pack(fill='both',expand=True)

        self.create_table_frame = tk.Frame(self.notebook)
        self.notebook.add(self.create_table_frame, text="Create Table")
        self.create_table_ui = CreateTableUI(self.create_table_frame)
        


         # Tables sekmesi
        self.tables_frame = tk.Frame(self.notebook)
        self.notebook.add(self.tables_frame, text='Tables')

        self.tables_listbox=tk.Listbox(self.tables_frame)
        self.tables_listbox.pack(fill='both',expand=True)
        self.update_table_list()

        # Search sekmesi
        self.search_frame = tk.Frame(self.notebook)
        self.notebook.add(self.search_frame, text='Search')
    
    def update_table_list(self):
        table_names=get_table_names()
        self.tables_listbox.delete(0,tk.END)
        for table_name in table_names:
            self.tables_listbox.insert(tk.END,table_name)

if __name__=='__main__':
    app=MainUI()
    app.mainloop()     



       
   
