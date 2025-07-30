# Full error-free implementation of Library Administrative System using Tkinter and MySQL
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import datetime


class LibraryAdministrativeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Administrative System")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finallprice_var = StringVar()

        # Title Label
        lbltitle = Label(self.root, text="LIBRARY ADMINISTRATIVE SYSTEM", bg="powder blue", fg="red", bd=20,
                         relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # DataFrame Left
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="red", bd=12,
                                   relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # Labels and Entry fields - Left Section
        labels = [
            ("PRN No:", self.prn_var),
            ("ID No:", self.id_var),
            ("First Name:", self.firstname_var),
            ("Last Name:", self.lastname_var),
            ("Address 1:", self.address1_var),
            ("Address 2:", self.address2_var),
            ("Post Code:", self.postcode_var),
            ("Mobile No:", self.mobile_var),
            ("Book ID:", self.bookid_var),
            ("Book Title:", self.booktitle_var),
            ("Author:", self.author_var),
            ("Date Borrowed:", self.dateborrowed_var),
            ("Date Due:", self.datedue_var),
            ("Days on Book:", self.daysonbook_var),
            ("Late Return Fine:", self.lateratefine_var),
            ("Date Overdue:", self.dateoverdue_var),
            ("Final Price:", self.finallprice_var),
        ]

        for idx, (label_text, var) in enumerate(labels):
            Label(DataFrameLeft, text=label_text, font=("arial", 12, "bold"), bg="powder blue").grid(row=idx+1, column=0, sticky=W, pady=2)
            Entry(DataFrameLeft, textvariable=var, font=("arial", 12), width=29).grid(row=idx+1, column=1, pady=2)

        # DataFrame Right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="red", bd=12,
                                    relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12), width=32, height=14, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        # Buttons
        btn_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        btn_frame.place(x=0, y=530, width=1530, height=70)

        Button(btn_frame, text="Add", font=("arial", 12, "bold"), width=23, command=self.add_data).grid(row=0, column=0)
        Button(btn_frame, text="Update", font=("arial", 12, "bold"), width=23, command=self.update_data).grid(row=0, column=1)
        Button(btn_frame, text="Delete", font=("arial", 12, "bold"), width=23, command=self.delete_data).grid(row=0, column=2)
        Button(btn_frame, text="Clear", font=("arial", 12, "bold"), width=23, command=self.clear_fields).grid(row=0, column=3)

        # Table Frame
        table_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        table_frame.place(x=0, y=600, width=1530, height=190)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, columns=(
            "prn", "id", "firstname", "lastname", "address1", "address2", "postcode", "mobile",
            "bookid", "booktitle", "author", "dateborrowed", "datedue", "daysonbook",
            "latereturnfine", "dateoverdue", "finalprice"
        ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("prn", text="PRN No")
        self.library_table.heading("id", text="ID")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postcode", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("daysonbook", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Overdue")
        self.library_table.heading("finalprice", text="Final Price")
        self.library_table["show"] = "headings"

        self.library_table.column("prn", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("daysonbook", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.library_table.pack(fill=BOTH, expand=1)
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="library"
        )

    def add_data(self):
        if self.prn_var.get() == "" or self.firstname_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO members (
                    prn, id_no, first_name, last_name, address1, address2, postcode,
                    mobile, book_id, book_title, author, date_borrowed, date_due,
                    days_on_book, late_return_fine, date_overdue, final_price
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.prn_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(),
                self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
                self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(),
                self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(),
                self.daysonbook_var.get(), self.lateratefine_var.get(),
                self.dateoverdue_var.get(), self.finallprice_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def update_data(self):
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE members SET
                    id_no=%s, first_name=%s, last_name=%s, address1=%s, address2=%s, postcode=%s,
                    mobile=%s, book_id=%s, book_title=%s, author=%s, date_borrowed=%s, date_due=%s,
                    days_on_book=%s, late_return_fine=%s, date_overdue=%s, final_price=%s
                WHERE prn=%s
            """, (
                self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(),
                self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
                self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(),
                self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(),
                self.daysonbook_var.get(), self.lateratefine_var.get(), self.dateoverdue_var.get(),
                self.finallprice_var.get(), self.prn_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_data(self):
        confirm = messagebox.askyesno("Confirm Delete", "Do you want to delete this record?")
        if confirm:
            try:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM members WHERE prn=%s", (self.prn_var.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record deleted successfully")
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    def clear_fields(self):
        for var in [
            self.member_var, self.prn_var, self.id_var, self.firstname_var, self.lastname_var,
            self.address1_var, self.address2_var, self.postcode_var, self.mobile_var, self.bookid_var,
            self.booktitle_var, self.author_var, self.dateborrowed_var, self.datedue_var,
            self.daysonbook_var, self.lateratefine_var, self.dateoverdue_var, self.finallprice_var
        ]:
            var.set("")
        self.txtBox.delete("1.0", END)

    def fetch_data(self):
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM members")
            rows = cursor.fetchall()
            if rows:
                self.library_table.delete(*self.library_table.get_children())
                for row in rows:
                    self.library_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Fetch Error", str(e))

    def get_cursor(self, event):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']
        if row:
            self.prn_var.set(row[0])
            self.id_var.set(row[1])
            self.firstname_var.set(row[2])
            self.lastname_var.set(row[3])
            self.address1_var.set(row[4])
            self.address2_var.set(row[5])
            self.postcode_var.set(row[6])
            self.mobile_var.set(row[7])
            self.bookid_var.set(row[8])
            self.booktitle_var.set(row[9])
            self.author_var.set(row[10])
            self.dateborrowed_var.set(row[11])
            self.datedue_var.set(row[12])
            self.daysonbook_var.set(row[13])
            self.lateratefine_var.set(row[14])
            self.dateoverdue_var.set(row[15])
            self.finallprice_var.set(row[16])


if __name__ == "__main__":
    root = Tk()
    app = LibraryAdministrativeSystem(root)
    root.mainloop()
