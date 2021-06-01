from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
root=Tk()
root.title('Pharmacy_Management_System')
root.configure(width=1500,height=600,bg='BLACK')

conn=sqlite3.connect('pharmacy_data.db')
c=conn.cursor()


'''c.execute("""CREATE TABLE pharmacydata(
      item_name text,
      item_price integer,
      item_quantity integer,
      item_discount integer,
      manufacture_date integer,
      expiry_date integer
)""")
print("table successfully created")
'''

# Creating a function to delete a record
def delete():
    # create database
    conn = sqlite3.connect('pharmacy_data.db')
    #create cursor
    c = conn.cursor()
    #delete a record
    c.execute("DELETE from pharmacydata WHERE oid = " + delete_box.get())
    print('Deleted Successfully')
    # query of the database
    c.execute("SELECT *, oid FROM pharmacydata")
    records = c.fetchall()
    # print(records)
    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)
    conn.commit()
    conn.close()

#Creating an update function
def update():
    # Create a databases or connect to one
    conn = sqlite3.connect('pharmacy_data.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute(""" UPDATE pharmacydata SET
         item_name = :name,
         item_price = :price,
         item_quantity = :quantity,
         item_discount = :discount,
         manufacture_date = :manufacture,
         expiry_date = :expiry
         WHERE oid = :oid""",
         {'name': item_name_editor.get(),
          'price': item_price_editor.get(),
          'quantity': item_quantity_editor.get(),
          'discount': item_discount_editor.get(),
          'manufacture': manufacture_date_editor.get(),
          'expiry': expiry_date_editor.get(),
          'oid': record_id
               }
    )
    conn.commit()
    conn.close()
    #Destroying all the data and closing window
    editor.destroy()


# Create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update Data')

    editor.geometry('300x480')
    # Create a databases or connect to one
    conn = sqlite3.connect('pharmacy_data.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    # query of the database
    c.execute("SELECT * FROM pharmacydata WHERE oid=" + record_id)
    records = c.fetchall()
    # print(records)
    #Creating global variable for all text boxes
    global item_name_editor
    global item_price_editor
    global item_quantity_editor
    global item_discount_editor
    global manufacture_date_editor
    global expiry_date_editor

    # Create text boxes
    item_name_editor = Entry(editor, width=30)
    item_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    item_price_editor = Entry(editor, width=30)
    item_price_editor.grid(row=1, column=1)
    item_quantity_editor = Entry(editor, width=30)
    item_quantity_editor.grid(row=2, column=1)
    item_discount_editor = Entry(editor, width=30)
    item_discount_editor.grid(row=3, column=1)
    manufacture_date_editor = Entry(editor, width=30)
    manufacture_date_editor.grid(row=4, column=1)
    expiry_date_editor = Entry(editor, width=30)
    expiry_date_editor.grid(row=5, column=1)

    # Create textbox labels
    item_name_label = Label(editor, text="Item Name")
    item_name_label.grid(row=0, column=0, pady=(10, 0))
    item_price_label = Label(editor, text="Item Price")
    item_price_label.grid(row=1, column=0)
    item_quantity_label = Label(editor, text="Item quantity")
    item_quantity_label.grid(row=2, column=0)
    item_discount_label = Label(editor, text="Item Discount")
    item_discount_label.grid(row=3, column=0)
    manufacture_date_label = Label(editor, text="Manufacture Date")
    manufacture_date_label.grid(row=4, column=0)
    expiry_date_label = Label(editor, text="Expiry Date")
    expiry_date_label.grid(row=5, column=0)

    # loop through the results
    for record in records:
        item_name_editor.insert(0, record[0])
        item_price_editor.insert(0, record[1])
        item_quantity_editor.insert(0, record[2])
        item_discount_editor.insert(0, record[3])
        manufacture_date_editor.insert(0, record[4])
        expiry_date_editor.insert(0, record[5])
    save_btn=Button(editor,text="Save",relief="raised",command=update)
    save_btn.grid(row=6,column=0)

# Create submit button for databases
def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('pharmacy_data.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO pharmacydata VALUES (:item_name, :item_price, :item_quantity, :item_discount, :manufacture_date, :expiry_date)",{
        'item_name':item_name.get(),
        'item_price':item_price.get(),
        'item_quantity':item_quantity.get(),
        'item_discount':item_discount.get(),
        'manufacture_date':manufacture_date.get(),
        'expiry_date':expiry_date.get()
    })
    # showinfo messagebox
    messagebox.showinfo("pharmacydata", "Inserted Successfully")
    conn.commit()
    conn.close()
    # clear the text boxes
    item_name.delete(0,END)
    item_price.delete(0,END)
    item_quantity.delete(0,END)
    item_discount.delete(0, END)
    manufacture_date.delete(0, END)
    expiry_date.delete(0, END)

def query():
    global display
    display=Tk()
    display.title('Display Items')
    # Create a databases or connect to one
    conn = sqlite3.connect('pharmacy_data.db')
    # Create cursor
    c = conn.cursor()
    # query of the database
    c.execute("SELECT *, oid FROM pharmacydata")
    records = c.fetchall()
   # print(records)
    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + '\t' + str(record[1]) + ' ' + '\t' + str(record[2]) +' ' + '\t' + str(record[3]) + ' ' + '\t' + str(record[4]) + ' ' + '\t' + str(record[5]) + ' ' + '\t' + str(record[6]) + "\n"
    query_label = Label(display, text=print_record)
    query_label.grid(row=0, column=0)

    conn.commit()
    conn.close()

#create label
name=Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="light blue",fg="dark green",font=("Times", 30))
name.grid(columnspan=6, padx=10, pady=10)

item_name=Label(root,text="ENTER ITEM NAME",relief="ridge",bg="yellow",fg="black",font=("Times", 12),width=25)
item_name.grid(row=1,column=0,padx=10,pady=10)

item_price=Label(root, text="ENTER ITEM PRICE",relief="ridge",bg="yellow",fg="black",font=("Times", 12),width=25)
item_price.grid(row=2,column=0, padx=10,pady=10)

item_quantity=Label(root,text="ENTER ITEM QUANTITY",relief="ridge",bg="yellow",fg="black",font=("Times", 12),width=25)
item_quantity.grid(row=3,column=0,padx=10,pady=10)

item_discount=Label(root,text="ENTER ITEM DISCOUNT",relief="ridge",bg="yellow",fg="black",font=("Times", 12),width=25)
item_discount.grid(row=4,column=0,padx=10,pady=10)

manufacture_date=Label(root,text="ENTER MANUFACTURED DATE",bg="yellow",relief="ridge",fg="black",font=("Times", 12),width=25)
manufacture_date.grid(row=5,column=0,padx=10,pady=10)

expiry_date=Label(root,text="ENTER EXPIRY DATE",bg="yellow",relief="ridge",fg="black", font=("Times", 12),width=25)
expiry_date.grid(row=6,column=0,padx=10,pady=10)

delete_box=Label(root,text="ENTER ID",bg="yellow",relief="ridge",fg="black", font=("Times", 12),width=25)
delete_box.grid(row=7,column=0,padx=10,pady=10)

#create entry
item_name=Entry(root,font=("Times", 12))
item_name.grid(row=1,column=1,padx=40,pady=10)

item_price= Entry(root,font=("Times", 12))
item_price.grid(row=2,column=1,padx=10,pady=10)

item_quantity= Entry(root,font=("Times", 12))
item_quantity.grid(row=3,column=1,padx=10,pady=10)

item_discount= Entry(root, font=("Times", 12))
item_discount.grid(row=4,column=1,padx=10,pady=10)

manufacture_date= Entry(root,font=("Times", 12))
manufacture_date.grid(row=5,column=1,padx=10,pady=10)

expiry_date= Entry(root,font=("Times", 12))
expiry_date.grid(row=6,column=1,padx=10,pady=10)

delete_box= Entry(root,font=("Times",12))
delete_box.grid(row=7,column=1,padx=10,pady=10)

# Create submit button
submit_btn = Button(root,bg="yellow",fg="black",relief="raised",font=("Times", 12),width=25,text="ADD ITEM",command=submit)
submit_btn.grid(row=1,column=4,padx=40,pady=10)

# Create query button
query_btn = Button(root,bg="yellow",fg="black",relief="raised",font=("Times", 12),width=25,text="VIEW ITEMS",command=query)
query_btn.grid(row=2,column=4,padx=40,pady=10)

# Create a delete button
delete_btn = Button(root,bg="yellow",fg="black",relief="raised",font=("Times", 12),width=25,text="DELETE ITEM",command=delete)
delete_btn.grid(row=3,column=4, padx=40,pady=10)

# Create a update button
save_btn = Button(root,bg="yellow",fg="black",relief="raised",font=("Times", 12),width=25,text="UPDATE",command=edit)
save_btn.grid(row=4,column=4,padx=40,pady=10)

# commit change
conn.commit()
# close connection
conn.close()
mainloop()