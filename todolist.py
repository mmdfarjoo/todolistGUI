from tkinter import *
from tkinter import messagebox


def AddItem (entry: Entry,listbox:Listbox):
    new_task = entry.get()
    listbox.insert(END,new_task)
    
    with open ('tasks.txt','a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')

def DelItem (listbox:Listbox):
    listbox.delete(ACTIVE)
    with open ('tasks.txt','r+')as tasks_list_file:
        lines = tasks_list_file.readlines()
        
        tasks_list_file.truncate()
        for line in lines :
            if listbox.get(ACTIVE) == line [:-2]:
                lines.remove(line)
            tasks_list_file.write(line)
        tasks_list_file.close()

def info ():
    messagebox.showinfo("info","With this program, you can write down your work so that you don't forget :)) Just write in the small box below and hit add, use delete to delete.")
def github ():
    messagebox.showinfo("github","github.com//mmdfarjoo       pelase star me in github and follow thanks :D")
#light mood 
def light ():
    
    win['background']="silver"
    tasks.config(fg='black',bg="white")
    addbtn.config(fg='white',bg="black")
    delbtn.config(fg='white',bg="black")

    

#dark mood
def dark ():
    win['background']="gray"
    tasks.config(fg='black',bg="silver")
    addbtn.config(fg='black',bg="silver")
    delbtn.config(fg='black',bg="silver")



#main

win= Tk()
win.title("ToDo List GUI")
win.geometry("300x400")
win.resizable(False,False)
win['background']='silver'


#head label 
Label(win,text="ToDo List Tkinter Python",font="Times 15 ",bg="white",fg="black",width=35,height=2).place(x=0,y=1)

tasks = Listbox (win,selectbackground="Gold", bg="white",font="Bnazanin 12 bold",height=13,width=20)
scroller=Scrollbar(win,orient=VERTICAL,command=tasks.yview)
scroller.place(x=260,y=50,height=250)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=50,y=50)

NewItem=Entry(win,width=27,bg="white")
NewItem.place(x=48,y=306)



addbtn = Button(win,text="Add Task",fg="white",bg="black",font="Times 15",width=7,height=0,command=lambda:AddItem(NewItem,tasks))
addbtn.place(x=50,y=345)



delbtn= Button(win,text="Delet Task",fg="white",bg="black",font="Times 15",width=7,height=0,command=lambda:DelItem(tasks))
delbtn . place(x=165,y=345)





menubar= Menu(win)
menuin = Menu(menubar, tearoff=0)
menuin.add_command(label='Light mood',command=light)
menuin.add_command(label='Dark mood',command=dark)
menubar.add_cascade(label='Theme',menu= menuin)


menuin = Menu(menubar,tearoff=0)
menubar.add_cascade(label="info",menu= menuin)
menuin.add_command(label='help',command=info)
menuin.add_command(label='github :)',command=github)

win.config(menu=menubar)





win.update()
win.mainloop()
