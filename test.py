from tkinter  import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

lang=[]
for i in LANGUAGES.items():
	lang.append(i[1])
root=Tk(className='Translator')
root.geometry("580x560")
root.resizable(0,0)
root.config(bg='blue')

input_text=Text(root,wrap=WORD,bd=20,bg='cyan',font=("Javanese Text",18, "bold"))
input_text.place(x=0,y=0,height=250,width=580)


output_text=Text(root,wrap=WORD,bd=20,bg='light blue',font=("Javanese Text",18, "bold"))
output_text.place(x=0,y=310,height=250,width=580)

src_lang=ttk.Combobox(root,values=lang,font=("Consolas",15, "bold"))
src_lang.place(x=0,y=255,height=50,width=180)

dest_lang=ttk.Combobox(root,values=lang,font=("Consolas",15, "bold"))
dest_lang.place(x=400,y=255,height=50,width=180)

def translate():
	output_text.delete(0.0,END)
	x=Translator().translate(input_text.get(1.0,END),src=src_lang.get(),dest=dest_lang.get()).text
	output_text.insert(END,x)

bt=Button(root,text="Translate",font=("Javanese Text",18, "bold"),bd=8,command=translate)
bt.place(x=200,y=255,height=50,width=180)

root.mainloop()