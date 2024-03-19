import tkinter as tk
from tkinter import ttk
import tkinterDnD 
from tkinter import messagebox

root = tkinterDnD.Tk()  
root.title("Cif rebuilder")

address_stringvar = tk.StringVar()
address_stringvar.set('Drop cif here to rebuild!')

def drop(event):
    address_stringvar.set(event.data)
    #cif_file=address_stringvar.get()

def rebuild():
    file=address_stringvar.get()
    cif_data=[]
    reduilder_signal=False
    with open(file) as raw_data:
        lines=raw_data.readlines()
        for i in lines:    
            if reduilder_signal==True:
                rebuild_i=i.split(' ')
                del rebuild_i[0]
                output_i=''
                for j in rebuild_i:
                    output_i+=j
                cif_data.append(output_i)
            if reduilder_signal==False:
                cif_data.append(i)
            if '_space_group_symop_operation_xyz'in i:
                reduilder_signal=True
            elif 'loop_' in i:
                reduilder_signal=False
    with open(file[0:-4]+'-rebuild'+'.cif','w') as file:
        for i in cif_data:
            file.writelines(i)
    messagebox.showinfo("Note","All Done! cif has been rebuilded.")      

label_1 = ttk.Label(root, 
                    ondrop=drop, 
                    #ondragstart=drag_command,
                    textvar=address_stringvar, 
                    padding=50, 
                    relief="solid")
label_1.pack(fill="both", expand=True, padx=10, pady=10)

button_1=tk.Button(root, 
                   text="rebuild cif",
                   command=rebuild,
                   padx=10, 
                   pady=10)
button_1.pack()

root.mainloop()