import customtkinter

class CourseDetails(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Course")
        # self.state("zoomed")
        self.resizable(0, 0)
        self.geometry("800x800")
        self.cou_det = ["Course", "Subject title"]
        
        label = customtkinter.CTkLabel(self, 
                                       text = "PLEASE FILL IN THE GIVEN SPACES ACCURATELY WITH THE COURSES",
                                       font = ("Times", 20))
        label.grid(row = 0, column = 0, columnspan = 2, padx = 50, pady = 15, sticky = "nsew")
        
        label = customtkinter.CTkLabel(self, text = "Course")
        label.grid(row = 1, column = 0, padx = 25, pady = 15, sticky="nsew")
        
        label = customtkinter.CTkLabel(self, text = "Subject Title")
        label.grid(row = 1, column = 1, padx = 25, pady = 15, sticky="nsew")
            
        for x in range(10):
            for y in range(2):
                new_entry = customtkinter.CTkEntry(self, width = 350)
                new_entry.grid(row = x + 2, column = y, padx = 25, pady = 15, sticky="nsew")
        
        add_rec = customtkinter.CTkButton(self, text = "Add Courses")
        add_rec.grid(row = 12, column = 0, columnspan = 2, padx = 25, pady = 15, sticky = "nsew")
