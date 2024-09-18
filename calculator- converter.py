print("1. calculator ")
print("2. unit converter ")
print(" 3. quit ")
selection=int(input("enter choice :"))
if selection==1:
    from tkinter import Tk
    from tkinter import StringVar,Entry,Button
    from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor


    class scientific_calculator:
            def __init__(self_value):
                window=Tk()
                window.title('Scientific Calculator')
                window.configure(background="white")
                self_value.string=StringVar()
                entry_window=Entry(window,textvariable=self_value.string)
                entry_window.grid(row=0,column=0,columnspan=6)
                entry_window.configure(background="white")
                entry_window.focus()
              
                main_values=["7","8","9","/","%","clear","AC",
                        "4","5","6","*","(",")","**",
                        "1","2","3","-","=",",","0",".","min","+","sin","asin","cos","acos","tan()",
                        "pow","log10","max","abs","floor","pi","e","log","ceil","degrees","radians"]
                text_values=1
                j=0
                row=1
                col=0
                for i in main_values:
                    padx=10
                    pady=10
                    if(j==7):
                        row=2
                        col=0
                    if(j==14):
                        row=3
                        col=0
                    if(j==19):
                        row=4
                        col=0
                    if(j==26):
                        row=5
                        col=0
                    if(j==33):
                        row=6
                        col=0
                    if(i=='='):
                        value_btn=Button(window,height=2,width=4,padx=70,pady=pady,text=i,command=lambda i=i:self_value.equal_values())
                        value_btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                        value_btn.configure(background="Red")

                    elif(i=='clear'):
                        value_btn=Button(window,height=2,width=4,padx=padx,pady=pady, text=i ,command=lambda i=i:self_value.delete_values())
                        value_btn.grid(row=row,column=col,padx=1,pady=1)
                        value_btn.configure(background="Yellow")
                    elif(i=='AC'):
                        value_btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=i,command=lambda i=i:self_value.clear_all_values())
                        value_btn.grid(row=row,column=col,padx=1,pady=1)
                        value_btn.configure(background="blue")
                    else:
                        value_btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=i ,command=lambda i=i:self_value.add_Char_values(i))
                        value_btn.grid(row=row,column=col,padx=1,pady=1)
                        value_btn.configure(background="cyan")

                    col=col+1
                    j=j+1
                window.mainloop()
              
              
            def add_Char_values(self_value,char):
                self_value.string.set(self_value.string.get()+(str(char)))
              
            def delete_values(self_value):
                self_value.string.set(self_value.string.get()[0:-1])

            def clear_all_values(self_value):
                self_value.string.set("")

            def equal_values(self_value):
                result=""
                try:
                    result=eval(self_value.string.get())
                    self_value.string.set(result)
                except:
                    result="INVALID INPUT"
                self_value.string.set(result)
                 
    scientific_calculator()


              

    from tkinter import Tk
    from tkinter import StringVar,Entry,Button
    from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor


    class scientific_calculator:
        def __init__(self_value):
            window=Tk()
            window.title('Scientific Calculator')
            window.configure(background="white")
            self_value.string=StringVar()
            entry_window=Entry(window,textvariable=self_value.string)
            entry_window.grid(row=0,column=0,columnspan=6)
            entry_window.configure(background="white")
            entry_window.focus()
          
            main_values=["7","8","9","/","%","clear","AC",
                    "4","5","6","*","(",")","**",
                    "1","2","3","-","=",",","0",".","min","+","sin","asin","cos","acos","tan()",
                    "pow","log10","max","abs","floor","pi","e","log","ceil","degrees","radians"]
            text_values=1
            j=0
            row=1
            col=0
            for i in main_values:
                padx=10
                pady=10
                if(j==7):
                    row=2
                    col=0
                if(j==14):
                    row=3
                    col=0
                if(j==19):
                    row=4
                    col=0
                if(j==26):
                    row=5
                    col=0
                if(j==33):
                    row=6
                    col=0
                if(i=='='):
                    value_btn=Button(window,height=2,width=4,padx=70,pady=pady,text=i,command=lambda i=i:self_value.equal_values())
                    value_btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                    value_btn.configure(background="Red")

                elif(i=='clear'):
                    value_btn=Button(window,height=2,width=4,padx=padx,pady=pady, text=i ,command=lambda i=i:self_value.delete_values())
                    value_btn.grid(row=row,column=col,padx=1,pady=1)
                    value_btn.configure(background="Yellow")
                elif(i=='AC'):
                    value_btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=i,command=lambda i=i:self_value.clear_all_values())
                    value_btn.grid(row=row,column=col,padx=1,pady=1)
                    value_btn.configure(background="blue")
                else:
                    value_btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=i ,command=lambda i=i:self_value.add_Char_values(i))
                    value_btn.grid(row=row,column=col,padx=1,pady=1)
                    value_btn.configure(background="cyan")

                col=col+1
                j=j+1
            window.mainloop()
              
              
            def add_Char_values(self_value,char):
                self_value.string.set(self_value.string.get()+(str(char)))
              
            def delete_values(self_value):
                self_value.string.set(self_value.string.get()[0:-1])

            def clear_all_values(self_value):
                self_value.string.set("")

            def equal_values(self_value):
                result_value=""
                try:
                    result_value=eval(self_value.string.get())
                    self_value.string.set(result_value)
                except:
                    result_value="INVALID INPUTS"
                self_value.string.set(result_value)
                 
        scientific_calculator()


elif selection==2:
    print("1. temperature converter ")
    print("2. length converter ")
    selection=int(input("enter choice :"))
    if selection==1:
        from tkinter import *

        def convert_fahr():
            words = fbtext.get()
            ftemp = float(words)
            celbox.delete(0, END)
            celbox.insert(0, '%.2f' % (tocel(ftemp)))
            kelbox.delete(0, END)
            kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp))))
            return

        def convert_cel():
            words = cbtext.get()
            ctemp = float(words)
            fahrbox.delete(0, END)
            fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
            kelbox.delete(0, END)
            kelbox.insert(0, '%.2f' % (tokel(ctemp)))

        def convert_kel():
            words = kbtext.get()
            ktemp = float(words)
            fahrbox.delete(0, END)
            fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
            celbox.delete(0, END)
            celbox.insert(0, '%.2f' % (ktoc(ktemp)))

        def tocel(fahr):
            return (fahr-32) * 5.0 / 9.0

        def tofahr(cel):
            return cel * 9.0 / 5.0 + 32

        def ktoc(kel):
            return kel - 273.15

        def tokel(cel):
            return cel + 273.15

        app = Tk()
        app.title('Temperature converter')

        fahrlabel = Label(app, text = 'Fahrenheit')
        fahrlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

        cellabel = Label(app, text = 'Celsius')
        cellabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

        kellabel = Label(app, text = 'Kelvin')
        kellabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

        fbtext = StringVar()
        fbtext.set('')
        fahrbox = Entry(app, textvariable=fbtext)
        fahrbox.grid(row = 0, column = 1, padx = 5, pady = 5)

        cbtext = StringVar()
        cbtext.set('')
        celbox = Entry(app, textvariable=cbtext)
        celbox.grid(row = 1, column = 1, padx = 5, pady = 5)

        kbtext = StringVar()
        kbtext.set('')
        kelbox = Entry(app, textvariable=kbtext)
        kelbox.grid(row = 2, column = 1, padx = 5, pady = 5)

        fgobutton = Button(app, text = 'Go', command = convert_fahr)
        fgobutton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

        cgobutton = Button(app, text = 'Go', command = convert_cel)
        cgobutton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

        kgobutton = Button(app, text = 'Go', command = convert_kel)
        kgobutton.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

        exitbutton = Button(app, text = 'Exit', command = quit)
        exitbutton.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = N+S+E+W, columnspan = 3)

        app.mainloop()

    if selection==2:
        from tkinter import *

window = Tk()
window.title("Basic Converter")

window.geometry("500x300+500+350")

#globally declare measurement variables
measurement1 = ""
measurement2 = ""

def convert_SI(val, unit_in, unit_out):     #based on unitconverters.net
    SI = {'Meter':1, 'Kilometer':1000, 'Centimeter':0.01, 'Millimeter':0.001,
          'Micrometer':0.000001, 'Mile':1609.35, 'Yard':0.9144, 'Foot':0.3048,
          'Inch':0.0254}
    return val*SI[unit_in]/SI[unit_out]

def helpsection():
    pass    #put helpful info text here (e.g. no entering in right entry box else error)

def selectedInput():
    global measurement1
    measurement1 = listbox.get(listbox.curselection())#whatever is currently selected

def selectedOutput():
    global measurement2
    measurement2 = listbox1.get(listbox1.curselection()) #whatever is currently selected

def converter():
    try:
        global measurement1, measurement2
        result.set(str(convert_SI(float(inputEntry.get()), measurement1, measurement2)))

    except:
        result.set("Error")

title = Label(window, text="Basic Converter", font="Calibri 16")
title.grid(columnspan=3)
result = StringVar()    #initalize dispalyed output variable
#create a top-level menu
filemenu = Menu(window)
filemenu.add_command(label='Help', command=helpsection)
window.config(menu=filemenu)    #displays menu
#input and output entry fields
inputEntry = Entry(window)
inputEntry.grid(row=1, column=0)
arrow = Label(window, text="--->", font="Calibri 20").grid(row=1, column=1)
outputEntry = Entry(window, textvariable=result).grid(row=1, column=2)

convertButton = Button(window, text='Convert!', command=converter).grid(row=2, column=1)

#if nonetype error, because .grid needs to be called on their own line since it always returns None
scrollbar = Scrollbar(window)   #left scrollbar
scrollbar.grid(row=2, column=0, sticky = NE + SE)
listbox = Listbox(window, exportselection=False)   #left listbox
#exportselection option in order to select 2 different listbox at same time
listbox.grid(row=2, column=0)

measurement_list = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter',
                    'Micrometer', 'Mile', 'Yard', 'Foot', 'Inch']
for measurement in measurement_list:
    listbox.insert(END, measurement)
listbox.bind("<<ListboxSelect>>", lambda x: selectedInput())   #this instead of command= option
# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


scrollbar1 = Scrollbar(window)   #right scrollbar
scrollbar1.grid(row=2, column=2, sticky = NE + SE)   #add sticky if scrollbar not showing
listbox1 = Listbox(window, exportselection=False)   #right listbox
listbox1.grid(row=2, column=2)

for measurement in measurement_list:
    listbox1.insert(END, measurement)
listbox1.bind("<<ListboxSelect>>", lambda x: selectedOutput())
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

#configure grid layout to adjust whenever window dimensions change
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
       
if selection==3:
    exit
else:
    print("invalid choice ")


