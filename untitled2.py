from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.title("HTML")
root.geometry("650x650")

open_image=ImageTk.PhotoImage(Image.open("folder.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))
close_image=ImageTk.PhotoImage(Image.open("play.png"))

file_name_label=Label(root,text="File Name")
file_name_label.place(relx=0.4,rely=0.1,anchor=CENTER)
input_file=Entry(root)
input_file.place(relx=0.6,rely=0.1,anchor=CENTER)

input_textArea=Text(root,height=35,width=150)
input_textArea.place(relx=0.1,rely=0.2)

root.mainloop()