import customtkinter
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

#SQLITE IS A TEST!!! CHANGE IT!!! AS SOON AS POSSIBLE!!!

class CourseDetails(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Course")
        self.state("zoomed")
        self.resizable(0, 0)
        self.geometry("800x800")
        self.entries = []
        self.grid_columnconfigure((0,1), weight=1)

        # Database connection
        self.conn = sqlite3.connect(os.getenv('DATABASE'))
        self.cursor = self.conn.cursor()
        self.create_table()
                
        label = customtkinter.CTkLabel(self, 
                                       text = "PLEASE FILL IN THE GIVEN SPACES ACCURATELY WITH THE COURSES",
                                       font = ("Times", 20, "bold"))
        label.grid(row = 0, column = 0, columnspan = 2, padx = 50, pady = 15, sticky = "nsew")
        
        label = customtkinter.CTkLabel(self, 
                                       text = "Course",
                                       font = ("Times", 20, "bold"))
        label.grid(row = 1, column = 0, padx = 25, pady = 15, sticky="nsew")
        
        label = customtkinter.CTkLabel(self, 
                                       text = "Subject Title",
                                       font = ("Times", 20, "bold"))
        label.grid(row = 1, column = 1, padx = 25, pady = 15, sticky="nsew")
            
        for x in range(10):
            row_entries = []
            for y in range(2):
                new_entry = customtkinter.CTkEntry(self)
                new_entry.grid(row = x + 2, column = y, padx = 25, pady = 15, sticky="nsew")
                row_entries.append(new_entry)
            self.entries.append(row_entries)
        
        add_rec = customtkinter.CTkButton(self, text = "Add Courses", command = self.save_data)
        add_rec.grid(row = 12, column = 0, columnspan = 2, padx = 25, pady = 15, sticky = "nsew")


    def create_table(self):
        """Create the SQLite table if it doesn't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course VARCHAR(20) NOT NULL CHECK(course <> ""),
                subject VARCHAR(20) NOT NULL CHECK(subject <> "")
            )
        """)
        self.conn.commit()
        
    def save_data(self):
        #Retrieve data from widgets and insert into the database
        for row_entries in self.entries:
            course = row_entries[0].get()
            subject = row_entries[1].get()
            # Insert into SQLite database
            if not (course and subject):
                print("Empty entries")
            else:
                try:
                    self.cursor.execute("""
                        INSERT INTO courses (course, subject) 
                        VALUES (?, ?)
                    """, (course, subject))
                    print("Data saved successfully!")
                except sqlite3.IntegrityError as i:
                    print("Integrity error i.e value error", i)
                except sqlite3.OperationalError as o:
                    print("Operational error i.e schema error", o)
        self.conn.commit()
        

