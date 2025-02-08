import customtkinter
from add_courses import CourseDetails
from add_student import StudentDetails

class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color = "white")
        
        # label = customtkinter.CTkLabel(self, 
        #                                text = "Select ")
        # label.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "new")
    
        add_courses = customtkinter.CTkButton(self, 
                                              text = "Add Courses", 
                                              
                                              command = self.open_courses)
        add_courses.grid(row = 1, column = 0, padx = 10, pady = 20)
        
        add_students = customtkinter.CTkButton(self, 
                                               text = "Add Students", 
                                               
                                               command = self.open_students)
        add_students.grid(row = 2, column = 0, padx = 10, pady = 20)
        
        logout = customtkinter.CTkButton(self, 
                                         text = "Log Out",
                                         fg_color = "red", 
                                         )
        logout.grid(row = 4, column = 0, padx = 10, pady = 20, sticky = "sew")
       
        self.toplevel_window = None
        
    def open_courses(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CourseDetails(self)
        else:
            self.toplevel_window.focus()
        
    def open_students(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = StudentDetails(self)
        else:
            self.toplevel_window.focus()
                                
                
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  
        self.geometry("800x600")
        self.resizable(0, 0)
        self.title("Result")
        self.grid_columnconfigure(1, weight = 1)
        
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.sidebar = SideBar(self)
        self.sidebar.grid(row = 3, column = 0, sticky = "nsew")
        # self.sidebar.grid_propagate(False)
        
        welcome = customtkinter.CTkLabel(self, 
                                         text = "Welcome!",
                                         font = ("Times", 20))
        welcome.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "nsew")
        
        alert = customtkinter.CTkLabel(self, 
                                       text = "Sorry, you have no records at the moment",
                                       font = ("Times", 16))
        alert.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "nsew")
        
        alert = customtkinter.CTkLabel(self, 
                                       text = "Click on 'Add courses' on the left to add a new set and their registered courses",
                                       font = ("Times", 16))
        alert.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = "nsew")
        
        alert = customtkinter.CTkLabel(self, 
                                       text = "Click on 'Add students' on the left to add students to a previously registerd set",
                                       font = ("Times", 16))
        alert.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = "nsew")
        
        alert = customtkinter.CTkLabel(self, 
                                       text = "Remember that you cannot add students unless you have registered a set and its courses first",
                                       font = ("Times", 16))
        alert.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = "nsew")
            
app = App()
app.mainloop()