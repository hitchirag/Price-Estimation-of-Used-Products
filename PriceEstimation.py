from tkinter import *
from tkinter import messagebox
import tkinter as tk

def price():
    productsscreen = Toplevel()
    productsscreen.title("Price Estimation of Used Products")
    productsscreen.geometry("800x650")
    productsscreen.config(bg="#FDD7E4")

    Heading = StringVar()
    Headinglabel = Label( productsscreen, textvariable = Heading ,bg="#7E587E",width="1000",pady="10")
    Heading.set("Price Estimation of Used Products")
    Headinglabel.pack()

    mainline = StringVar()
    mainlinelable = Message(productsscreen,textvariable=mainline,width="1000",fg="#800517",pady="20")
    mainline.set("")
    mainlinelable.pack()
    
    entername = StringVar()
    enternamelabel = Message(productsscreen,textvariable = entername,bg="#C9BE62",width="1000",pady="10")
    entername.set("Enter the Name of the Product: ")
    enternamelabel.pack()
    productname = Entry(productsscreen,bd=5,width="25")
    productname.pack()
    
    enterprice = StringVar()
    enterpricelabel = Message(productsscreen,textvariable = enterprice,bg="#C9BE62",width="1000",pady="10")
    enterprice.set("Enter the Price of the Product: ")
    enterpricelabel.pack()
    productprice = Entry(productsscreen,bd=5,width="25")
    productprice.pack()
    
    entertype = StringVar()
    entertypelabel = Message(productsscreen,textvariable = entertype,bg="#C9BE62",width="1000",pady="10")
    entertype.set("Enter the Type of the Product: ")
    entertypelabel.pack()
    producttype = Entry(productsscreen,bd=5,width="25")
    producttype.pack()
    
    entermonth = StringVar()
    entermonthlabel = Message(productsscreen,textvariable = entermonth,bg="#C9BE62",width="1000",pady="20")
    entermonth.set("Enter the Months since you have bought the Product: ")
    entermonthlabel.pack()
    month = Entry(productsscreen,bd=5,width="25")
    month.pack()

    def estimatedpricefunctioninside():
        productpricefloat = float(productprice.get())
        monthfloat = float(month.get())
        estimatedprice = productpricefloat - (0.2*productpricefloat + 0.01*monthfloat*productpricefloat)
        if(estimatedprice<0):
            estimatedprice=0
        messagebox.showinfo( "Estimated Price","Estimate Price is Rs." + str(estimatedprice))

    def addtolist():
        productpricefloat = float(productprice.get())
        monthfloat = float(month.get())
        estimatedprice = productpricefloat - (0.2*productpricefloat + 0.01*monthfloat*productpricefloat)
        if(estimatedprice<0):
            estimatedprice=0
        f = open("ProductsList.txt","a")
        f.write("  " + productname.get() + "   \t\t\t      Rs." + productprice.get() + "    \t\t\t       " + producttype.get() + "    \t\t\t       Rs."  + str(estimatedprice) + "  " )
        f.write("\n\n")
        f.close()
        messagebox.showinfo("Add to List","Information has been successfully added.")

    mainline1 = StringVar()
    mainlinelable1 = Message(productsscreen,textvariable=mainline1,width="1000",fg="#800517",pady="20")
    mainline1.set("")
    mainlinelable1.pack()

    estimatedpricebutton = Button(productsscreen,text = "Click to See Estimated Price",bg="#2B65EC",fg="#82CAFA",padx="20",pady="20",command=estimatedpricefunctioninside)
    estimatedpricebutton.pack()

    mainline2 = StringVar()
    mainlinelable2 = Message(productsscreen,textvariable=mainline2,width="1000",fg="#800517",pady="20")
    mainline2.set("")
    mainlinelable2.pack()

    addtolistbutton = Button(productsscreen,text="Click to Add Product to List",bg="#2B65EC",fg="#82CAFA",padx="20",pady="20",command=addtolist)
    addtolistbutton.pack()

def availableproducts():
    productslistscreen = Toplevel()
    productslistscreen.geometry("800x500")
    productslistscreen.title("Products List")

    Heading = StringVar()
    Headinglabel = Label( productslistscreen, textvariable = Heading ,bg="#7E587E",width="1000",pady="10")
    Heading.set("Products List")
    Headinglabel.pack()

    Headingnext = StringVar()
    Headingnextlabel = Label( productslistscreen, textvariable = Headingnext ,bg="#46C7C7",width="1000",pady="10")
    Headingnext.set("  Product Name     \t\t     Actual Price      \t\t     Product Type     \t\t      Estimated Price    ")
    Headingnextlabel.pack()

    productsdetailsinstringcopy = StringVar()
    productsdetailsinstring=""
    f = open("ProductsList.txt","r")
    productsdetails = f.readlines()
    for product in productsdetails:
        productsdetailsinstring = productsdetailsinstring + product
    f.close()
    enterpricelabel = Message(productslistscreen,textvariable = productsdetailsinstringcopy,width="1000",pady="20")
    productsdetailsinstringcopy.set(productsdetailsinstring)
    enterpricelabel.pack()
    productslistscreen.mainloop()

def mainscreen():
    
    screen  = tk.Tk()
    screen.title("Main Screen")
    screen.geometry("600x400")
    screen.config(bg="#C6AEC7")

    Heading = StringVar()
    Headinglabel = Label( screen, textvariable = Heading ,bg="#FBBBB9",width="200",pady="20")
    Heading.set("Price Estimation of Used Products")
    Headinglabel.pack()

    mainline = StringVar()
    mainlinelable = Message(screen,textvariable=mainline,width="1000",fg="#800517",pady="20")
    mainline.set("Select Your Choice")
    mainlinelable.pack()

    priceestimation = Button(screen,text="Find Price Estimation",bg="#7D1B7E",fg="#FCDFFF",padx="20",pady="10",command=price)
    priceestimation.pack()
    
    mainline1 = StringVar()
    mainlinelable1 = Message(screen,textvariable=mainline1,width="1000",fg="#800517",pady="20")
    mainline1.set("")
    mainlinelable1.pack()
    
    products = Button(screen,text="Available Products",bg="#990012",fg="#F7E7CE",padx="10",pady="10",command=availableproducts)
    products.pack()
    
    mainline2 = StringVar()
    mainlinelable2 = Message(screen,textvariable=mainline2,width="1000",fg="#800517",pady="20")
    mainline2.set("")
    mainlinelable2.pack()
    
    def exitscreen():
        screen.destroy()
    
    exit = Button(screen,text="Exit",bg="#2B65EC",fg="#B6B6B4",padx="30",pady="10",command=exitscreen)
    exit.pack()
    
    screen.mainloop()

def check(username,password):

    username=username+"\n"
    password=password+"\n"
    
    f=open("Username.txt","r")
    usernames = f.readlines()
    nameindex=0
    namefound=0
    for name in usernames:
        nameindex=nameindex+1
        if(username==name):
            namefound=1
            break
    f.close()
    if namefound==0:
        return False

    f=open("Password.txt","r")
    passwords = f.readlines()
    passwordindex=0
    for passs in passwords:
        passwordindex=passwordindex+1
        if(passwordindex==nameindex):
            if(passs==password):
                return True
    return False

print("-------------Price Estimation of Used Products-----------")
print("Select your choice")
print("1.Login")
print("2.SignUp")
choice=input()

if(choice=='1'):
    print("Enter the username: ",end="")
    username=input()
    print("Enter the password: ",end="")
    password=input()
    
    if(check(username,password)==True):
        mainscreen()
        print("Input credentials are correct")
    
    else:
        print("Input credentials are incorrect")

elif(choice=='2'):
    print("Enter the username: ",end="")
    username=input()
    print("Enter the password: ",end="")
    password=input()
    print("Re-enter the password: ",end="")
    repassword=input()
    
    if(password!=repassword):
        print("------Password and Re-entered Password are Not Matching------")
    
    else:
        f=open("Username.txt","a")
        f.write(username)
        f.write("\n")
        f.close()
        f=open("Password.txt","a")
        f.write(password)
        f.write("\n")
        f.close()
        mainscreen()

else:
    print("Input Choice is Incorrect")