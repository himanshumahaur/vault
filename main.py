from tkinter import *
from tkinter import font
import pandas as pd
from PIL import ImageTk, Image

cpgval=0

def getuserlist():
    maindata = pd.read_csv('./img/data.csv')
    userlist = maindata['u'].values.tolist()
    return userlist

def getpasslist():
    maindata = pd.read_csv('./img/data.csv')
    passlist = maindata['p'].values.tolist()
    return passlist

def savenew():
    global addWindow, userEntry, passEntry

    username = userEntry.get()
    password = passEntry.get()

    newdata = pd.DataFrame({'user':[username], 'pass':[password]})
    newdata.to_csv('./img/data.csv', mode='a', index=False, header=False)

    
    addWindow.destroy()

    manageWindow.destroy()
    managepass()

def addcancel():
    addWindow.destroy()

def updatecancel():
    updateWindow.destroy()

def addpass():
    global addWindow, userEntry, passEntry

    addWindow = Toplevel()
    addWindow.config(background='#48d1cc')
    addWindow.geometry('350x220')
    addWindow.geometry("+{}+{}".format(590, 307))
    

    cpilabel = Label(addWindow, image=createpassimage,bg='#48d1cc')
    cpilabel.grid(row=1, column=1, columnspan=5)
    
    addLabel = Label(addWindow, fg='white', bg='#004953', height=2, text='Create New Password', padx=(111))
    addLabel.grid(row=0, column=1, columnspan=5)

    userLabel = Label(addWindow, bg='#48d1cc', text='Username')
    userLabel.grid(row=2, column=1, columnspan=1)

    userEntry = Entry(addWindow, width=43, bg='#c9ffe5', borderwidth=0.5, relief="solid")
    userEntry.grid(row=2, column=2, columnspan=3)

    passLabel = Label(addWindow, bg='#48d1cc', text='Password')
    passLabel.grid(row=3, column=1, columnspan=1, pady=(5,20))

    passEntry = Entry(addWindow, width=43, bg='#c9ffe5', borderwidth=0.5, relief="solid")
    passEntry.grid(row=3, column=2, columnspan=3, pady=(5,20))

    savenewButton = Button(addWindow, padx=17, bg='#004953', fg='white', text='Save', command=savenew, borderwidth=0.5, relief="solid")
    savenewButton.grid(row=4, column=1, columnspan=2)

    canceladdButton = Button(addWindow, padx=10, bg='#004953', fg='white', text='Cancel', command=addcancel, borderwidth=0.5, relief="solid")
    canceladdButton.grid(row=4, column=4, columnspan=2)

    addWindow.grab_set()


def saveold(pindex):

    global updateWindow, userEntry, passEntry

    username = userEntry.get()
    password = passEntry.get()

    maindata = pd.read_csv('./img/data.csv')
    maindata.iloc[pindex,0]=username
    maindata.iloc[pindex,1]=password
    maindata.to_csv('./img/data.csv', index=False)

    updateWindow.destroy()

    manageWindow.destroy()
    managepass()
    

def delpass(passindex):
    maindata = pd.read_csv('./img/data.csv')
    maindata.drop(labels=[passindex], axis=0, inplace=True)
    maindata.to_csv('./img/data.csv', index=False)
    manageWindow.destroy()
    managepass()


def updatepass(pindex):
    global updateWindow, userEntry, passEntry

    userlist = getuserlist()
    passlist = getpasslist()

    seluser = StringVar()
    seluser.set(userlist[pindex])
    selpass = StringVar()
    selpass.set(passlist[pindex])

    updateWindow = Toplevel()
    updateWindow.config(background='#48d1cc')
    updateWindow.geometry('350x220')
    updateWindow.geometry("+{}+{}".format(590, 307))

    upilabel = Label(updateWindow, image=updatepassimage,bg='#48d1cc')
    upilabel.grid(row=1, column=1, columnspan=5)

    updateLabel = Label(updateWindow, fg='white', bg='#004953', height=2, text='Update Old Password', padx=(113))
    updateLabel.grid(row=0, column=1, columnspan=5)

    userLabel = Label(updateWindow, bg='#48d1cc', text='Username')
    userLabel.grid(row=2, column=1, columnspan=1)

    userEntry = Entry(updateWindow, text=seluser, width=43, bg='#c9ffe5', borderwidth=0.5, relief="solid")
    userEntry.grid(row=2, column=2, columnspan=3)

    passLabel = Label(updateWindow, bg='#48d1cc', text='Password')
    passLabel.grid(row=3, column=1, columnspan=1, pady=(5,20))

    passEntry = Entry(updateWindow, text=selpass, width=43, bg='#c9ffe5', borderwidth=0.5, relief="solid")
    passEntry.grid(row=3, column=2, columnspan=3, pady=(5,20))

    saveoldButton = Button(updateWindow, padx=17, bg='#004953', fg='white', text='Save', command=lambda: saveold(pindex), borderwidth=0.5, relief="solid")
    saveoldButton.grid(row=4, column=1, columnspan=2)

    cancelupdateButton = Button(updateWindow, padx=10, bg='#004953', fg='white', text='Cancel', command=updatecancel, borderwidth=0.5, relief="solid")
    cancelupdateButton.grid(row=4, column=4, columnspan=2)

    updateWindow.grab_set()

def copypass(passindex):
    passlist = getpasslist()
    root.clipboard_clear()
    root.clipboard_append(passlist[passindex])

def prevpass():
    global manageWindow, frameloop, cpgval, pagelabel

    pagelist = getpagelist()

    if cpgval > 0:
        frameloop[cpgval].grid_forget()
        cpgval = cpgval-1
        frameloop[cpgval].grid(row=3, column=0, columnspan=4)

        pagelabel.config(text=str(cpgval+1)+'/'+str(len(pagelist)))


def nextpass():
    global manageWindow, frameloop, cpgval, pagelabel

    pagelist = getpagelist()

    if cpgval+1 < len(pagelist):
        frameloop[cpgval].grid_forget()
        cpgval = cpgval+1
        frameloop[cpgval].grid(row=3, column=0, columnspan=4)

        pagelabel.config(text=str(cpgval+1)+'/'+str(len(pagelist)))
    




def getpagelist():
    ulist = getuserlist()

    list123=[]
    for i in range(len(ulist)):
        list123.append(i)

    pagelist = []
    templist = []

    for i in list123:
        if len(templist) < 7:
            templist.append(i)
        else:
            pagelist.append(templist)
            templist = []
            templist.append(i)
    pagelist.append(templist)

    return pagelist


def managepass():
    global manageWindow, cleyeimage, opeyeimage, frameloop, pagelabel

    manageWindow = Toplevel()
    manageWindow.config(bg='#48d1cc')
    manageWindow.geometry('642x450')
    manageWindow.maxsize(642, 450)
    manageWindow.minsize(642, 450)

    manageWindow.geometry("+{}+{}".format(445, 180))

    userlist = getuserlist()
    passlist = getpasslist()

    passindex = IntVar()

    frameloop = []
    updateloop = []
    userloop = []
    passloop = []
    viewloop = []

    #next
    pagelist = getpagelist()


    userLabel = Label(manageWindow, fg='white', bg='#004953', height=2, width=45, text='Username')
    userLabel.grid(row=1, column=0, columnspan=2, pady=(0, 25))

    passLabel = Label(manageWindow, fg='white', bg='#004953', height=2, width=45, text='Password')
    passLabel.grid(row=1, column=2, columnspan=2, pady=(0, 25))

    
    emptyframe = Frame(manageWindow, bg='#009a9a')
    emptyframe.grid(row=0, column=0, columnspan=4)
    emptylabel = Label(emptyframe, bg='#009a9a', padx=318, pady=15)
    emptylabel.pack()

    addButton = Button(manageWindow, fg='white', bg='#009a9a', activebackground='#009a9a', borderwidth=0, image=addimage, command=addpass)
    addButton.place(rely=0.1, relx=0.2, x=0, y=0, anchor=S)

    updateButton = Button(manageWindow, fg='white', bg='#009a9a', activebackground='#009a9a', borderwidth=0, image=updateimage, command=lambda: updatepass(passindex.get()))
    updateButton.place(rely=0.1, relx=0.75, x=0, y=0, anchor=S)

    delButton = Button(manageWindow, fg='white', bg='#009a9a', activebackground='#009a9a', borderwidth=0, image=delimage, command=lambda: delpass(passindex.get()))
    delButton.place(rely=0.1, relx=0.85, x=0, y=0, anchor=S)

    prevButton = Button(manageWindow, fg='white', bg='#48d1cc', activebackground='#48d1cc', image=previmage, borderwidth=0, command=lambda: prevpass())
    prevButton.place(rely=0.98, relx=0.4, x=0, y=0, anchor=S)

    nextButton = Button(manageWindow, fg='white', bg='#48d1cc', activebackground='#48d1cc', image=nextimage, borderwidth=0, command=lambda: nextpass())
    nextButton.place(rely=0.98, relx=0.6, x=0, y=0, anchor=S)
    

    for j in range(len(pagelist)):
        frameloop.append(Frame(manageWindow, background='#48d1cc'))
        

        for i in pagelist[j]:
            updateloop.append(Radiobutton(frameloop[j], bg='#48d1cc', variable=passindex, value=int(i)))
            updateloop[i].grid(row=i+2, column=0)

            userloop.append(Label(frameloop[j], width=35, fg='black', bg='#48d1cc', height=2, anchor='w', text=userlist[i]))
            userloop[i].grid(row=i+2, column=1)

            passloop.append(Button(frameloop[j], width=35, fg='#c9ffe5', bg='#c9ffe5', activeforeground='#c9ffe5', activebackground='#c9ffe5', borderwidth=0.5, anchor='w', text=passlist[i], relief="solid", command=lambda i=i:copypass(i)))
            passloop[i].grid(row=i+2, column=2, padx=20)

            viewloop.append(Button(frameloop[j], fg='black', bg='#48d1cc', activebackground='#48d1cc', border=0, image=cleyeimage, command=lambda i=i:visible(userloop[i], passloop[i], viewloop[i], i)))
            viewloop[i].grid(row=i+2, column=3, padx=5)

    frameloop[0].grid(row=3, column=0, columnspan=4)

    pagelabel = Label(manageWindow, bg='#48d1cc', text='1/'+str(len(pagelist)))
    pagelabel.place(rely=0.95, relx=0.5, x=0, y=0, anchor=S)
    
    root.withdraw()


def visible(userLabel, passButton, viewButton, i):
    global opeyeimage, cleyeimage

    if passButton['fg']=='#c9ffe5':
        passButton.config(fg="black")
        viewButton.config(image=opeyeimage)
    else:
        passButton.config(fg="#c9ffe5")
        viewButton.config(image=cleyeimage)



root = Tk()

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family='Arial', size=9)

root.config(bg='#48d1cc')
root.geometry('500x500')

##########################
root.geometry("+{}+{}".format(525, 200))
##########################

opeyeimage = PhotoImage(file='./img/opeye.png')
cleyeimage = PhotoImage(file='./img/cleye.png')
previmage = PhotoImage(file='./img/p1.png')
nextimage = PhotoImage(file='./img/n1.png')
delimage = PhotoImage(file='./img/del.png')
updateimage = PhotoImage(file='./img/update.png')
addimage = PhotoImage(file='./img/add.png')
createpassimage = PhotoImage(file='./img/cpi.png')
updatepassimage = PhotoImage(file='./img/upi.png')

oldButton = Button(text='Log in', command=managepass)
oldButton.pack(pady=50)


root.mainloop()