import os
from datetime import datetime, timedelta
import tkinter as tk
from organizer import organize_files
from reminder import set_reminder

class UserInterface(tk.Tk):
    def __init__(self):
        try:
            super().__init__()
            self.title("Failu Organizēšanas un Atgādinājumu Sistēma")
            self.geometry("400x300")
            
            self.label = tk.Label(self, text="Sveiki! Šī ir jūsu sākuma lietotāja saskarne.")
            self.label.pack(pady=20)

            self.organize_button = tk.Button(self, text="Organizēt Failus", command=self.organize_files)
            self.organize_button.pack(pady=10)

            self.reminder_button = tk.Button(self, text="Iestatīt Atgādinājumu", command=self.set_reminder)
            self.reminder_button.pack(pady=10)
        except tk.TclError as e:
            print(f"Izņēmums no tkinter: {e}")
            print("Programma turpinās bez grafiskā interfeisa.")

    def organize_files(self):
        organize_files()
        self.label.config(text="Faili tika veiksmīgi organizēti!")

    def set_reminder(self):
        reminder_time = datetime.now() + timedelta(minutes=5)
        set_reminder(reminder_time)
        self.label.config(text=f"Atgādinājums iestatīts uz {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")

def run_user_interface():
    ui = UserInterface()
    if tk._default_root:
        tk._default_root.update()
        tk.mainloop()

def main():
    print("Sveiki! Šī ir Failu Organizēšanas un Atgādinājumu Sistēma.")
    run_user_interface()

if __name__ == "__main__":
    main()
