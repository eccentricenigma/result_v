import customtkinter
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

#SQLITE IS A TEST!!! CHANGE IT!!! AS SOON AS POSSIBLE!!!

class StudentDetails(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Student")
        self.state("zoomed")
        self.entries = []
        
        # Database connection
        self.conn = sqlite3.connect(os.getenv('DATABASE'))
        self.cursor = self.conn.cursor()
        self.create_table()
        
        self.students = ["First name", "Middle name (optional)", " Surname", "Examination number"]
        
        for col in range(len(self.students)):
            self.grid_columnconfigure(col, weight=1)
            
        label = customtkinter.CTkLabel(self, 
                                       text = "PLEASE FILL IN THE GIVEN SPACES ACCURATELY WITH THE STUDENT'S DATA",
                                       font = ("Times", 20, "bold"))
        label.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 20, sticky = "nsew")

        for x in range(10):
            row_entries = []
            for y in range(len(self.students)):
                details = customtkinter.CTkEntry(self, 
                                                 placeholder_text = self.students[y], 
                                                 width = 300)
                details.grid(row = x + 1, column = y, padx = 35, pady = 15)
                row_entries.append(details)
            self.entries.append(row_entries)

        add_rec = customtkinter.CTkButton(self, 
                                          text = "Add Students", 
                                          height = 50, 
                                          command = self.save_data)
        add_rec.grid(row = 11, column = 1, columnspan = 2, padx = 35, pady = 20, sticky = "nsew")
     
     
    def create_table(self):
        """Create the SQLite table if it doesn't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(15) NOT NULL CHECK(first_name <> ""),
                middle_name VARCHAR(15),
                sur_name VARCHAR(15) NOT NULL CHECK(sur_name <> ""),
                examination_number VARCHAR(15) NOT NULL CHECK(examination_number <> "")
            )
        """)
        self.conn.commit()

        
    def save_data(self):
        #Retrieve data from widgets and insert into the database
        for row_entries in self.entries:
            first_name = row_entries[0].get()
            middle_name = row_entries[1].get()
            sur_name = row_entries[2].get()
            examination_number = row_entries[3].get()
            
            # Insert into SQLite database
            if not (first_name and sur_name):
                print("Incomplete Name")
            elif not examination_number:
                print("No examination number")
            else:
                try:
                    self.cursor.execute("""
                        INSERT INTO students (first_name, middle_name, sur_name, examination_number) 
                        VALUES (?, ?, ?, ?)
                    """, (first_name, middle_name, sur_name, examination_number))
                    print("Data saved successfully!")
                except sqlite3.IntegrityError as i:
                    print("Integrity error i.e value error", i)
                except sqlite3.OperationalError as o:
                    print("Operational error i.e schema error", o)
        self.conn.commit()