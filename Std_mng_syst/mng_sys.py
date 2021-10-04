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

    def query():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        c = conn.cursor()

        # query of the database
        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
       # print(records)

        # Loop through the results
        print_record=''
        for record in records:
            #str(record[6]) added for displaying the id
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) +  ' '+str(record[6]) + '    '+str(record[7])+ "\n"

        print("showing data", print_record)
        query_label = Label(details_frame, text=print_record, font=("Times", 10, "bold"))
        query_label.place(x=0, y=0)




        conn.commit()
        conn.close()





    # Creating a function to delete a record

    def delete():
        # create database
        conn = sqlite3.connect('address_book.db')

        #create cursor
        c = conn.cursor()

        #delete a record
        c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
        print('Deleted Successfully')

        # query of the database
        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
        # print(records)

        # Loop through the results
        print_record = ''
        for record in records:
            # str(record[6]) added for displaying the id
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) +' ' +str(record[7])+ "\n"

        delete_box.delete(0, END)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted successfully", "Data Deleted sucessfully")


    # Create edit function to update a record
