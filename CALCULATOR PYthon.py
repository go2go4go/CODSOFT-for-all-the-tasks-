
from tkinter import *
root=Tk()
root.title("My calculator")
root.geometry("300x400")
root.resizable(width=0,height=0)
root.configure(bg="black")
e=Entry(root,bd=10,width=30,font="Arial 21",bg="lightGrey")
e.pack()
def click(number):
    e.insert(index=32,string=number)
def Add():
    e.insert(index=32,string="+")
def clear():
    e.delete(first=0,last=END) 
def Equal():
    current=e.get()
    list=current.split("+")
    result=int(list[0]) + int(list[1])
    clear()
    e.insert(index=32,string=result)

btn1=Button(root,text="7",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(7))
btn1.place(x=10,y=60)
btn2=Button(root,text="8",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(8))
btn2.place(x=85,y=60)
btn3=Button(root,text="9",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(9))
btn3.place(x=160,y=60)
btn4=Button(root,text="4",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(4))
btn4.place(x=10,y=145)
btn5=Button(root,text="5",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(5))
btn5.place(x=85,y=145)
btn6=Button(root,text="6",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(6))
btn6.place(x=160,y=145)
btn7=Button(root,text="1",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(1))
btn7.place(x=10,y=230)
btn8=Button(root,text="2",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(2))
btn8.place(x=85,y=230)
btn9=Button(root,text="3",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(3))
btn9.place(x=160,y=230)
btn10=Button(root,text="0",font="Arial 19 bold",bg="Grey",bd=10,padx=10,pady=5,command=lambda :click(0))
btn10.place(x=10,y=320)
btn11=Button(root,text="+",font="Arial 19 bold",height=4,bd=10,bg="skyblue",command=Add)
btn11.place(x=235,y=60)
btn12=Button(root,text="C",font="Arial 19 bold",width=8,height=1,bd=10,bg="crimson",command=clear)
btn12.place(x=85,y=320)
btn13=Button(root,text="=",font="Arial 19 bold",height=4,bd=10,bg="khaki",command=Equal)
btn13.place(x=235,y=230)

root.mainloop()

print("Select an operation :")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operation=input()

if operation=="1":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The sum is"+str(int(num1) +int(num2)))
elif operation=="2":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The difference is"+str(int(num1) -int(num2)))
elif operation=="3":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The result is"+ str(int(num1) * int(num2)))
elif operation=="4":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The result is"+str(int(num1) / int(num2))) 
    '''
while True:
    print("select an operation:")
    print("1.Add","2.subtract","3.Multiply","4.Divide",sep="\n")
    operation=input()
    break   '''
else:
    print("NO, that is invalid")

