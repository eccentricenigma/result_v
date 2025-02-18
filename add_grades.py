import customtkinter as ctk
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

class AddGrades(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Student")
        self.state("zoomed")
        
        #connect to database
        self.conn = sqlite3.connect(os.getenv('DATABASE'))
        self.cursor = self.conn.cursor()
            
        #extract courses from database
        self.cursor.execute("SELECT course, subject FROM courses")
        self.courses = self.cursor.fetchall()
        
        #extract student details from database 
        self.cursor.execute("SELECT sur_name, first_name, middle_name, examination_number FROM students")
        self.students = self.cursor.fetchall()
        
        #create headers
        self.headers = ["Name", "Examination number"]
        for x, course in self.courses:
            self.headers.append(course)
            
        #display instructions
        total_columns = len(self.headers)
        
        for col in range(total_columns):
            self.grid_columnconfigure(col, weight=1)

        self.label = ctk.CTkLabel(self, 
                                            text = "Please ensure to fill in the student's details accordingly",
                                            font = ("Times", 18, "bold"))
        self.label.grid(row = 0, column = 0, columnspan=total_columns, padx = 15, pady = 10, sticky = "nsew")
        
         
        for col_index, header in enumerate(self.headers):
            self.label = ctk.CTkLabel(self,
                                           text = header,
                                           font = ("Times", 18, "bold"))
            self.label.grid(row = 1, column = col_index, padx = 15, pady = 10, sticky = "nsew")
        
        #display student details under appropriate headers
        for row_index, student in enumerate(self.students):
            row_index = row_index + 2
            sur_name, first_name, middle_name, examination_number = student            
            full_name = " ".join(filter(None, [sur_name, first_name, middle_name]))
            
            self.name_label = ctk.CTkLabel(self,
                                           text = full_name,
                                           font = ("Arial", 14))
            self.name_label.grid(row = row_index, column = 0,  padx = 15, pady = 10, sticky = "nsew")
            
            self.exam_label = ctk.CTkLabel(self, 
                                           text = examination_number)
            self.exam_label.grid(row = row_index, column = 1, padx = 15, pady = 10, sticky = "nsew")
            
            # create entries for inputting marks under each course for each student
            for col_index, course in enumerate(self.courses):
                self.score = ctk.CTkEntry(self,
                                          placeholder_text = "Input score")
                self.score.grid(row = row_index, column = col_index + 2, padx = 15, pady = 10, sticky = "nsew")
            
            