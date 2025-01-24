import customtkinter

class StudentDetails(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
        first_name = customtkinter.CTkEntry(self, placeholder_text="First name", width = 180)
        first_name.grid(row = 1, column = 0, padx = 10, pady = 20)

        middle_name = customtkinter.CTkEntry(self, placeholder_text="Middle name (optional)", width = 180)
        middle_name.grid(row = 1, column = 1, padx = 10, pady = 20)
        
        sur_name = customtkinter.CTkEntry(self, placeholder_text="Surname", width = 180)
        sur_name.grid(row = 1, column = 2, padx = 10, pady = 20)
        
        exam_number = customtkinter.CTkEntry(self, placeholder_text="Examination Number", width = 180)
        exam_number.grid(row = 1, column = 3, padx = 10, pady = 20)


class CourseDetails(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
        course = customtkinter.CTkLabel(self, text = "Course", width = 100)
        course.grid(row = 2, column = 0, padx = 10, pady = 20, sticky="nsew")
        
        title = customtkinter.CTkLabel(self, text = "Subject Title", width = 100)
        title.grid(row = 2, column = 1, padx = 10, pady = 20, sticky="nsew")
        
        marks = customtkinter.CTkLabel(self, text = "Mark Obtained", width = 100)
        marks.grid(row = 2, column = 2, padx = 10, pady = 20, sticky="nsew")
        
        grade = customtkinter.CTkLabel(self, text = "Grade", width = 100)
        grade.grid(row = 2, column = 3, padx = 10, pady = 20, sticky="nsew")
        
        remark = customtkinter.CTkLabel(self, text = "Remarks", width = 100)
        remark.grid(row = 2, column = 4, padx = 10, pady = 20, sticky="nsew")  
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Result")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.StudentDetails = StudentDetails(self)
        self.StudentDetails.grid(row=1, column=0, padx=0, pady=(10, 0), sticky="e")
        
        self.CourseDetails = CourseDetails(self)
        self.CourseDetails.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        
        add_rec = customtkinter.CTkButton(self, text = "Add record")
        add_rec.grid(row = 7, column = 0, padx = 10, pady = 20)
        
        
app = App()
app.mainloop()