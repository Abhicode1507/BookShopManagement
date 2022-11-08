import csv
import pandas as pd

def insert_book(name,email,book,n):
    with open('Books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "email", "Book in cart","Book number"])
        writer.writerow([name, email, book, n])

def delete_book(book_name):
    Books = "Books.csv"
    df=pd.read_csv(Books)
    df_s1=df[:5]
    df_s1=df_s1.drop(df_s1[df_s1.name==book_name])

print("Enter your name ")
name=input()
print("Enter your email ")
email=input()
print("Enter your password ")
password=input()
book=""

print("**************HEY",name,"WELCOME TO BOOK SHOP**************")
print("what you want?")
print("enter add to add book")
print("enter delete to remove book")

s=input()
if s=="add":
    print("Press the key written in front of book name to add them in your cart")
    print("1. Bhagvad Gita")
    print("2. Ramayana")
    print("3. Vedas")
    print("4. Be here now")
    print("5. Hinduism")

    n=int(input())
    if n==1:
        book="Bhagvad Gita"
    if n==2:
        book="Ramayana"
    if n==3:
        book="Vedas"
    if n==4:
        book="Be here now"
    if n==5:
        book="Hinduism"
    insert_book(name,email,book,n)
    print("CONGRATULATIONS!", book, "added to your cart succesfully")
else:
    print("enter book name")
    book=input()
    delete_book(book)
    print("Book",book,"remove")

print("**************Thank you for purchasing**************")