import pandas as pd
from datetime import date
import csv

def main():
    print("WHO ARE YOU ? ")
    print("1. USER      2. MANAGER")
    c=input("enter choice : ")
    if c=="1":
        user()
    elif c=="2":
        manager()
        p=input()
        if p=="1234":
            manager()
        else:
            main()
    else:
        main()

def manager():
    print(" 1.Add 2.Books 3.Delete 4.Check Orders. ")
    c=input("enter choice : ")
    if c=='1':
        add()
    elif c=='2':
        books()
    elif c=='3':
        delete()
    elif c=='4':
        orders()
    else:
        manager()

def add():
    n=input("enter book name : ")
    c=input("Cost : ")
    row=[n,c]
    l=r'C:\Users\user\Desktop\BookShopManagement\bookshop.csv'
    with open(l,'a+',newline='')as cf:
        cw=csv.writer(cf)
        cw.writerow(row)
    cf.close()
    manager()

def books():
    l=r'C:\Users\user\Desktop\BookShopManagement\bookshop.csv'
    with open(l,'r')as cf:
        cw=csv.reader(cf)
        cd=pd.DataFrame(cw)
        print("|--------------------------------------------------|")
        for i in cd.index:
            x=list(cd.loc[i])
            print("BID : ",i)
            print("NAME : ",x[0])
            print("COST : ",x[1])
            print("|--------------------------------------------------|")
    cf.close()
    manager()

def delete():
    d=int(input("Enter BID : "))
    l=r'C:\Users\user\Desktop\BookShopManagement\bookshop.csv'
    with open(l,'r+')as cf:
        cw=csv.reader(cf)
        cd=pd.DataFrame(cw)
        cd.drop([d],inplace=True)
        cf.close()
        with open(l,'w',newline='')as cf:
            cw=csv.writer(cf)
            for i in cd.index:
                x=list(cd.loc[i])
                cw.writerow(x)
    cf.close()
    manager()

def user():
    print("1.Check Books    2.Buy")
    c=input("enter choice : ")
    if c=='1':
        cproducts()
    elif c=='2':
        buy()
    else:
        user()

def cproducts():
    l=r'C:\Users\user\Desktop\BookShopManagement\bookshop.csv'
    with open(l,'r') as cf:
        cw=csv.reader(cf)
        cd=pd.DataFrame(cw)
        print("|--------------------------------------------------|")
        for i in cd.index:
            x=list(cd.loc[i])
            print("BID : ",i)
            print("NAME : ",x[0])
            print("COST : ",x[1])
            print("|--------------------------------------------------|")
    cf.close()
    user()

def buy():
    p=input("Book ID : ")
    n=input("Your Name : ")
    a=input("Email : ")
    t=date.today()
    row=[p,n,a,t]
    ol=r'C:\Users\user\Desktop\BookShopManagement\cart.csv'
    with open(ol,'a+',newline='')as cf:
        cw=csv.writer(cf)
        cw.writerow(row)
    cf.close()
    user()

def orders():
    l=r'C:\Users\user\Desktop\BookShopManagement\cart.csv'
    with open(l,'r') as cf:
        cw=csv.reader(cf)
        cd=pd.DataFrame(cw)
        print("|--------------------------------------------------|")
        for i in cd.index:
            x=list(cd.loc[i])
            print("BID : ",x[0])
            print("NAME : ",x[1])
            print("Email : ",x[2])
            print("Date : ",x[3])
            print("|--------------------------------------------------|")
    cf.close()
    manager()
main()