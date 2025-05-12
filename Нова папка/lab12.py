from tkinter import*
import messagebox
from PIL import Image, ImageTk
def show():
    new_window = Toplevel(root)
    new_window.title("Фото")
    new_window.geometry("400x400")

    image = Image.open("11.jpg")
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()


def inf():
    s=edit4.get()
    if s=="111":
        messagebox.showinfo("Про спеціальність",edit4.get()+"\nСпеціальність 111 Математика\nОсвітня програма Комп'ютерна математика")
    elif s=="СОМ"or"014":
        messagebox.showinfo("Про спеціальність",edit4.get()+"\nСпеціальність 014 Середня освіта\nОсвітня програма Середня освіта. Математика, інформатика")
    else:
        messagebox.showinfo("Про спеціальність",edit4.get()+"\nТакої спеціальності на факультеті немає")
root=Tk()
root.geometry('300x550+500+100')
root.configure(bg="lightblue")
root.title("Анкета")
label1=Label(root,text="Прізвище:", justify=CENTER)
label1.pack()
edit1=Entry(root,width=25)
edit1.pack()
label2=Label(root,text="Ім'я:",justify=CENTER)
label2.pack()
entry2=Entry(root,width=25)
entry2.pack()
label3=Label(root,text="По батькові:",justify=CENTER)
label3.pack()
entry3=Entry(root,width=25)
entry3.pack()
checkbutton1=Checkbutton(root,text='ч')
checkbutton1.pack()
checkbutton2=Checkbutton(root,text='ж')
checkbutton2.pack()
label4=Label(root,text="Виберіть курс:")
label4.pack()
result1=IntVar()
result1.set(1)
Radiobutton1=Radiobutton(root,text=1,variable=result1,value=1).pack()
Radiobutton2=Radiobutton(root,text=2,variable=result1,value=2).pack()
Radiobutton3=Radiobutton(root,text=3,variable=result1,value=3).pack()
Radiobutton4=Radiobutton(root,text=4,variable=result1,value=4).pack()
label5=Label(text="Спеціальність")
label5.pack()
edit4=Entry(root,width=25)
edit4.pack()
button1=Button(root,text="Про спеціальність",width=20,command=inf).pack()
label6=Label().pack
button2=Button(root,text="Фото",width=20,command=show).pack()
root.mainloop()