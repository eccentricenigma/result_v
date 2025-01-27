import customtkinter

class StudentDetails(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.stu_det = ["First name", "Middle name (optional)", " Surname", "Examination number"]
        
        col_count = 1 
        
        for detail in self.stu_det:
            first_name = customtkinter.CTkEntry(self, placeholder_text = detail, width = 180)
            first_name.grid(row = 1, column = col_count, padx = 10, pady = 20)
            col_count = col_count + 1


class CourseDetails(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.cou_det = ["Course", "Subject title", "Mark obtained", "Grade", "Remarks"]
        
        # def boxg():
        #     if grade.get() == "A":
        #         return("Passed")
            
        col_count = 1 
        
        for detail in self.cou_det:
            course = customtkinter.CTkLabel(self, text = detail)
            course.grid(row = 2, column = col_count, padx = 10, pady = 20, sticky="nsew")
            col_count = col_count + 1
            
        for x in range(7):
            for y in range(len(self.cou_det)):
                if y == 3:
                    grade = customtkinter.CTkComboBox(self, values = ["Select grade", "A", "B", "C", "D"])
                    grade.grid(row = 3 + x, column = y + 1, padx = 10, pady = 20, sticky="nsew")
                else:
                    new_entry = customtkinter.CTkEntry(self, width = 130)
                    new_entry.grid(row = 3 + x, column = y + 1, padx = 10, pady = 20, sticky="nsew")

              
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Result")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.StudentDetails = StudentDetails(self)
        self.StudentDetails.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="nsew")
        
        self.CourseDetails = CourseDetails(self)
        self.CourseDetails.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        
        add_rec = customtkinter.CTkButton(self, text = "Add record")
        add_rec.grid(row = 7, column = 0, padx = 10, pady = 20)
        
        
app = App()
app.mainloop()