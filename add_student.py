import customtkinter

class StudentDetails(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Add Student")
        self.state("zoomed")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")
        
        self.stu_det = ["First name", "Middle name (optional)", " Surname", "Examination number"]
        
        for x in range(10):
            for y in range(len(self.stu_det)):
                details = customtkinter.CTkEntry(self, placeholder_text = self.stu_det[y], width = 180)
                details.grid(row = x + 1, column = y + 1, padx = 10, pady = 20)
                
        add_rec = customtkinter.CTkButton(self, text = "Add record")
        add_rec.grid(row = 11, column = 2, columnspan = 2, padx = 10, pady = 20, sticky = "nsew")
