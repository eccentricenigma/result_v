import customtkinter

class StudentDetails(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Add Student")
        self.state("zoomed")
        # self.columnconfigure(0, weight = 1)
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")
        
        label = customtkinter.CTkLabel(self, 
                                       text = "PLEASE FILL IN THE GIVEN SPACES ACCURATELY WITH THE STUDENT'S DATA",
                                       font = ("Times", 20))
        label.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 20, sticky = "nsew")
        
        self.stu_det = ["First name", "Middle name (optional)", " Surname", "Examination number"]
        
        for x in range(10):
            for y in range(len(self.stu_det)):
                details = customtkinter.CTkEntry(self, placeholder_text = self.stu_det[y], width = 300)
                details.grid(row = x + 1, column = y, padx = 35, pady = 15)
                
        add_rec = customtkinter.CTkButton(self, text = "Add Students", height = 50)
        add_rec.grid(row = 11, column = 1, columnspan = 2, padx = 35, pady = 20, sticky = "nsew")
