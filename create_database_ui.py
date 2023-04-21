import tkinter as tk
import pickle
import os
from tkinter import messagebox
from tkinter import simpledialog
TABLE_NAME='tables/table_name.pickle'

if not os.path.exists('tables'):
    os.makedirs('tables')

class CreateTableUI:

    def __init__(self, master):
        self.master = master
        self.Columns=[]
        
        self.label1=tk.Label(self.master,text="Table Name:")
        self.label1.grid(row=0,column=0)
        self.entry1=tk.Entry(self.master)
        self.entry1.grid(row=0,column=1)

        self.label2=tk.Label(self.master,text="Column Adding: First choose type *")
        self.label2.grid(row=1,column=1)
        
       
        self.label3=tk.Label(self.master,text="Column Data Type:")
        self.label3.grid(row=2,column=0)
        self.columns_type_var= tk.StringVar(value="str")
        self.columns_type_option=tk.OptionMenu(self.master,self.columns_type_var,"int","str")
        self.columns_type_option.grid(row=2,column=1)
        self.add_column_button=tk.Button(self.master,text="+ Add Column",command=self.add_column)
        self.add_column_button.grid(row=3,column=0)
        
        self.label4=tk.Label(self.master,text="Columns:")
        self.label4.grid(row=4,column=0)
        self.columns_listbox=tk.Listbox(self.master)
        self.columns_listbox.grid(row=4,column=1)

        self.label5=tk.Label(self.master,text="Max Rows:")
        self.label5.grid(row=5,column=0)
        self.entry5=tk.Entry(self.master)
        self.entry5.grid(row=5,column=1)

        self.submit_button = tk.Button(master, text="Create Table", command=self.create_table)
        self.submit_button.grid(row=6,column=0)

    def add_column(self):
        column_name=simpledialog.askstring("Add Column","Column Name:")
        column_data_type=self.columns_type_var.get()
        if column_data_type=="str":
            column_max_length=simpledialog.askinteger("Add Column","Column Max Length:")
        else:
            column_max_value=simpledialog.askinteger("Add Column","Column Max Value:")
        if column_name:
            if column_data_type=="str":
                column_constraints={
                    "max_length":column_max_length
                }
            else:
                column_constraints={
                "max_value":column_max_value
            }
            
            self.Columns.append([column_name,column_data_type,column_constraints])

            if column_data_type=="str":
                self.columns_listbox.insert(tk.END,column_name + " (" + column_data_type + "," +str(column_max_length) + " chars)")
            else :
                self.columns_listbox.insert(tk.END, column_name +" (" + column_data_type + "," + str(column_max_value) + ")")
    
    def create_table(self):
        # burada girilen bilgileri kullanarak veritabanı oluştur
        table_name = self.entry1.get()
        primary_key = self.entry1.get()
        try:
            max_row = int(self.entry5.get())
        except ValueError:
            messagebox.showerror("Error","Please enter  a valid integer for Max Rows.")
            return

        # ön kontroller ilk kayıt için
        if os.path.exists(TABLE_NAME):
            with open(TABLE_NAME,'rb') as f:
                try:
                    existing_table_names=pickle.load(f)
                except EOFError:
                    existing_table_names=[]       
        else:
            existing_table_names=[]
        
        # tablo ismi bensersiz olmalı
        if table_name in existing_table_names:
            tk.messagebox.showerror("Error","Table name already exists.")
            return
        #tablo ismini dosyaya ekle
        existing_table_names.append(table_name)
        with open(TABLE_NAME,'wb') as f:
            pickle.dump(existing_table_names,f)
        

        # verilerin dosyaya yazılması ve veritabanı oluşturma işlemleri 
        table_data={
            "table_name":table_name,
            "primary_key":primary_key,
            "max_row":max_row,
            "columns":self.Columns
        }
        table_file_path=f'tables/{table_name}.pickle'
        with open(table_file_path,'wb') as table_file:
            pickle.dump(table_data,table_file)
        
        messagebox.showinfo("Success","Table created successfully.")

        #temizlik imandan ve python'dan gelir :)
        self.Columns.clear()
        self.columns_listbox.delete(0,tk.END)
        self.entry1.delete(0,tk.END)
        self.entry5.delete(0,tk.END)

if __name__=='__main__':    
    root = tk.Tk()
    app = CreateTableUI(root)
    root.mainloop()
