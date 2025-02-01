import customtkinter

class CourseDetails(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Course")
        self.state("zoomed")
        self.cou_det = ["Course", "Subject title"]
        
        
        label = customtkinter.CTkLabel(self, text = "Course")
        label.grid(row = 1, column = 0, padx = 20, pady = 20, sticky="nsew")
        
        label = customtkinter.CTkLabel(self, text = "Subject Title")
        label.grid(row = 1, column = 1, padx = 20, pady = 20, sticky="nsew")
            
        #Loop to add entry and combo boxe widgets for each of the items in the self.cou_det list    
        for x in range(10):
            for y in range(2):
                #This adds the entry widgets
                new_entry = customtkinter.CTkEntry(self, width = 130)
                new_entry.grid(row = x + 2, column = y, padx = 10, pady = 20, sticky="nsew")
