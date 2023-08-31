from customtkinter import *

class App:
    def __init__(self):
        self.screen_setting()
        
        speek = SpeekScreen(self.app)
        speek.micbtn._command = self.btn_event
        speek.visible()
        
    def screen_setting(self):
        self.app = CTk()
        self.app.title("WA")
        self.app.geometry("400x600")
        self.app.resizable(width=False, height=False)
        
        
    def btn_event(self):
        print("Click")
        
        
        
        
    def start(self):
        self.app.mainloop()
      
        
class SpeekScreen:
    def __init__(self, master):
        self.micbtn = CTkButton(master, text="", width=200, height=200, 
                                corner_radius=100)
        
    def visible(self):
        self.micbtn.place(relx=0.5, rely=0.5, anchor=CENTER)
        


if __name__ == "__main__":
    app = App()
    app.start()