import customtkinter
from add_courses import CourseDetails
from add_student import StudentDetails
                   
                
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  
        self.geometry("600x400")
        self.resizable(0, 0)
        self.title("Result")
        self.grid_columnconfigure(3, weight = 3)
        
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        welcome = customtkinter.CTkLabel(self, text = "Welcome")
        welcome.grid(row = 0, column = 3, padx = 20, pady = 20, sticky = "nsew")
        
        add_courses = customtkinter.CTkButton(self, text = "Add Courses", command = self.open_courses)
        add_courses.grid(row = 1, column = 3, padx = 10, pady = 10)
        
        add_students = customtkinter.CTkButton(self, text = "Add Students", command = self.open_students)
        add_students.grid(row = 2, column = 3, padx = 10, pady = 10)
        
        add_rec = customtkinter.CTkButton(self, text = "Add Record", command = self.open_records)
        add_rec.grid(row = 3, column = 3, padx = 10, pady = 10)
       
        self.toplevel_window = None
        
    def open_courses(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CourseDetails(self)
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
        
    def open_students(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = StudentDetails()
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
        
    def open_records(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            print("Not yet ready")
        #     self.toplevel_window = Records(self)
        # else:
        #     self.toplevel_window.focus()
            
app = App()
app.mainloop()