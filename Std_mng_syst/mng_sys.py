from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox



def login_page():




#Databases

    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    '''
    # Create table
    c.execute(""" CREATE TABLE addresses(
          name text,
          fathers_name text,
          mothers_name text,
          address text,
          gender text,
          date_of_birth text,
          phone_num integer
    ) """)
    '''
    # Create submit button for databases

    def submit():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO addresses VALUES (:name, :fathers_name, :mothers_name, :address, :gender, :date_of_birth,:phone_num)",
                  {
                      'name':name.get(),
                      'fathers_name':fathers_name.get(),
                      'mothers_name':mothers_name.get(),
                      'address':address.get(),
                      'gender':gender.get(),
                      'date_of_birth':date_of_birth.get(),
                      'phone_num':phone_num.get()
                  })
        # showinfo messagebox
        messagebox.showinfo("Adresses", "Inserted Successfully")

        conn.commit()

        conn.close()

        # clear the text boxes
        name.delete(0,END)
        fathers_name.delete(0,END)
        mothers_name.delete(0,END)
        address.delete(0, END)
        gender.delete(0, END)
        date_of_birth.delete(0, END)
        phone_num.delete(0, END)

