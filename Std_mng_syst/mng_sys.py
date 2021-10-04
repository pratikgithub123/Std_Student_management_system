from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


def login_page():
    # Databases

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
        c.execute(
            "INSERT INTO addresses VALUES (:name, :fathers_name, :mothers_name, :address, :gender, :date_of_birth,:phone_num)",
            {
                'name': name.get(),
                'fathers_name': fathers_name.get(),
                'mothers_name': mothers_name.get(),
                'address': address.get(),
                'gender': gender.get(),
                'date_of_birth': date_of_birth.get(),
                'phone_num': phone_num.get()
            })
        # showinfo messagebox
        messagebox.showinfo("Adresses", "Inserted Successfully")

        conn.commit()

        conn.close()

        # clear the text boxes
        name.delete(0, END)
        fathers_name.delete(0, END)
        mothers_name.delete(0, END)
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
        print_record = ''
        for record in records:
            # str(record[6]) added for displaying the id
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + '    ' + str(record[7]) + "\n"

        print("showing data", print_record)
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0, y=0)

        conn.commit()
        conn.close()

    # Creating a function to delete a record

    def delete():
        # create database
        conn = sqlite3.connect('address_book.db')

        # create cursor
        c = conn.cursor()

        # delete a record
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
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) + "\n"

        delete_box.delete(0, END)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted successfully", "Data Deleted sucessfully")

    # Create edit function to update a record
    def edit():

        global editor

        editor = Tk()
        editor.title('Update Data')

        editor.geometry('400x400')
        editor.configure(bg="lightblue")

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()

        # query of the database
        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

        records = c.fetchall()
        # print(records)

        # Creating global variable for all text boxes
        global name_editor
        global fathers_name_editor
        global mothers_name_editor
        global address_editor
        global gender_editor
        global date_of_birth_editor
        global phone_num_editor

        # Create text boxes
        name_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        name_editor.grid(row=0, column=1, padx=3, pady=5)

        fathers_name_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        fathers_name_editor.grid(row=1, column=1, padx=3, pady=5)

        mothers_name_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        mothers_name_editor.grid(row=2, column=1, padx=3, pady=5)

        address_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        address_editor.grid(row=3, column=1, padx=3, pady=5)

        gender_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        gender_editor.grid(row=3, column=1, padx=3, pady=5)

        date_of_birth_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        date_of_birth_editor.grid(row=4, column=1, padx=3, pady=5)

        phone_num_editor = Entry(editor, font=("Times", 15, "bold"), bg="white", width=30)
        phone_num_editor.grid(row=5, column=1, padx=3, pady=5)

        # Create textbox labels
        name_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Students Name")
        name_label.grid(row=0, column=0, padx=3, pady=5)

        fathers_name_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Fathers Name")
        fathers_name_label.grid(row=1, column=0, padx=3, pady=5)

        mothers_name_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Mothers Name")
        mothers_name_label.grid(row=2, column=0, padx=3, pady=5)

        address_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Adress")
        address_label.grid(row=3, column=0, padx=3, pady=5)

        gender_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Gender")
        gender_label.grid(row=3, column=0, padx=3, pady=5)

        date_of_birth_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="DOB")
        date_of_birth_label.grid(row=4, column=0, padx=3, pady=5)

        phone_num_label = Label(editor, font=("Times", 15, "bold"), bg="lightblue", text="Phone No")
        phone_num_label.grid(row=5, column=0, padx=3, pady=5)

        # loop
        for record in records:
            name_editor.insert(0, record[0])
            fathers_name_editor.insert(0, record[1])
            mothers_name_editor.insert(0, record[2])
            address_editor.insert(0, record[3])
            gender_editor.insert(0, record[4])
            date_of_birth_editor.insert(0, record[5])
            phone_num_editor.insert(0, record[6])

        # Create a update button
        edit_btn = Button(editor, font=("Times", 15, "bold"), bg="lightblue", text=" SAVE ", command=update)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

    # Creating an update function
    def update():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("""UPDATE addresses SET
            name=:name,
            fathers_name=:fathers_name,
            mothers_name=:mothers_name,
            address=:address,
            gender=:gender,
            date_of_birth=:date_of_birth,
            phone_num=:phone_num

            WHERE oid =:oid""",
                  {'name': name_editor.get(),
                   'fathers_name': fathers_name.get(),
                   'mothers_name': mothers_name.get(),
                   'address': address.get(),
                   'gender': gender.get(),
                   'date_of_birth': date_of_birth.get(),
                   'phone_num': phone_num.get(),
                   'oid': record_id
                   })

        conn.commit()
        conn.close()
        # Destroying all the data and closing window
        editor.destroy()

    def exit_fun():
        ask = messagebox.askyesno("exit", "Do you want to exit?")
        if ask == 1:
            root.destroy()

    root = Tk()
    root.title('Student Management System')

    root.geometry('900x700')
    root.iconbitmap("graduate.ico")

    # dataframe
    DataFrame = Frame(root, bd=10, bg="skyblue", relief=RIDGE, padx=20, pady=20)
    DataFrame.place(x=0, y=0, width=900, height=400)

    # dataframe left
    DataFrameLeft = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=20, text="Students Details",
                               fg="black", font=("Times", 13, "bold"))
    DataFrameLeft.place(x=0, y=5, width=500, height=300)

    # Create text boxes
    name = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    name.grid(row=0, column=1, pady=5)

    fathers_name = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    fathers_name.grid(row=1, column=1, pady=5)

    mothers_name = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    mothers_name.grid(row=2, column=1, pady=5)

    address = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    address.grid(row=3, column=1, pady=5)

    gender = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    gender.grid(row=3, column=1, pady=5)

    date_of_birth = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    date_of_birth.grid(row=4, column=1, pady=5)

    phone_num = Entry(DataFrameLeft, font=("Times", 15, "bold"), bg="white", width=30)
    phone_num.grid(row=17, column=1, pady=5)

    # Create textbox labels
    name_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Students Name")
    name_label.grid(row=0, column=0, pady=5)

    fathers_name_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Fathers Name")
    fathers_name_label.grid(row=1, column=0, pady=5)

    mothers_name_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Mothers Name")
    mothers_name_label.grid(row=2, column=0, pady=5)

    address_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Adress")
    address_label.grid(row=3, column=0, pady=5)

    gender_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Gender")
    gender_label.grid(row=3, column=0, pady=5)

    date_of_birth_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="DOB")
    date_of_birth_label.grid(row=4, column=0, pady=5)

    phone_num_label = Label(DataFrameLeft, font=("Times", 15, "bold"), bg="lightblue", text="Phone No")
    phone_num_label.grid(row=17, column=0, pady=5)

    # Data Frame Right
    DataFrameRight = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=18,
                                fg="darkgreen", font=("Times", 13, "bold"))
    DataFrameRight.place(x=500, y=5, width=300, height=300)
    font = ("Times", 10, "bold")

    delete_box_label = Label(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="ID")
    delete_box_label.grid(row=3, column=0, pady=5)

    delete_box = Entry(DataFrameRight, font=("Times", 10, "bold"), bg="white", width=30)
    delete_box.grid(row=3, column=1, pady=5)

    # Create submit button

    submit_btn = Button(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="Add", command=submit)
    submit_btn.grid(row=1, column=1, ipadx=10, padx=7, pady=5)

    # Create query button

    query_btn = Button(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="Display", command=query)
    query_btn.grid(row=2, column=1, padx=7, pady=5)

    # Create a delete button
    delete_btn = Button(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="Delete", command=delete)
    delete_btn.grid(row=5, column=1, padx=7, pady=5)

    # Create a update button
    edit_btn = Button(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="Update", command=edit)
    edit_btn.grid(row=4, column=1, padx=7, pady=5)

    exit_btn = Button(DataFrameRight, font=("Times", 12, "bold"), bg="lightblue", text="Exit", command=exit_fun)
    exit_btn.grid(row=6, column=1, ipadx=10, padx=7, pady=5)

    details_frame = LabelFrame(root, bd=10, relief=RIDGE, text="Students Records", font=("Times", 10, "bold"))
    details_frame.place(x=0, y=400, width=900, height=180)

    # details and scrollbar
    sc_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
    sc_x.pack(side=BOTTOM, fill=X)
    sc_y = ttk.Scrollbar(details_frame, orient=VERTICAL)
    sc_y.pack(side=RIGHT, fill=Y)

    sc_x.pack(side=BOTTOM, fill=X)
    sc_y.pack(side=RIGHT, fill=Y)
    # commit change
    conn.commit()

    # close connection
    conn.close()

    mainloop()