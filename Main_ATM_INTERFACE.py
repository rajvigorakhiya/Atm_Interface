
#atm interface
import tkinter as tk
from tkinter import messagebox, simpledialog

class ATMApp:
    def __init__(self, master): 
        self.master = master
        master.title("ATM Interface")
        master.geometry("400x450")
        master.configure(bg="#e6f2ff")
        self.correct_pin = "1234"
        self.balance = 5000.00

        self.login_screen()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Welcome to ATM", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.master, text="Enter your 4-digit PIN").pack(pady=5)
        self.pin_entry = tk.Entry(self.master, show="*", justify='center')
        self.pin_entry.pack()
        #tk.Button(self.master, text="Login", command=self.check_pin).pack(pady=10)
        self.login_button = tk.Button(self.master, text="Login", command=self.check_pin, bg="#006600", fg="white", font=("Arial", 10), width=5)
        self.login_button.pack(pady=10)

        # Hover effects
        self.login_button.bind("<Enter>", lambda event: self.login_button.config(bg="#004c99"))
        self.login_button.bind("<Leave>", lambda event: self.login_button.config(bg="#0066cc"))


    def check_pin(self):
        pin = self.pin_entry.get()
        if pin == self.correct_pin:
            self.main_menu()
        else:
            messagebox.showerror("Error", "Incorrect PIN!")

    def main_menu(self):
        '''self.clear_screen()
        tk.Label(self.master, text="ATM Main Menu", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.master, text="Check Balance", width=20, command=self.check_balance).pack(pady=5)
        tk.Button(self.master, text="Deposit", width=20, command=self.deposit).pack(pady=5)
        tk.Button(self.master, text="Withdraw", width=20, command=self.withdraw).pack(pady=5)
        tk.Button(self.master, text="Exit", width=20, command=self.master.quit).pack(pady=5)
        def main_menu(self):'''
        self.clear_screen()
        tk.Label(self.master, text="ATM Main Menu", font=("Arial", 16), bg="#e6f2ff", fg="#003366").pack(pady=20)

        # Button styling
        button_font = ("Arial", 12)
        button_bg = "#0066cc"
        hover_bg = "#004c99"
        fg_color = "white"

        # Check Balance
        self.balance_button = tk.Button(self.master, text="Check Balance", width=20, font=button_font,
                                        bg=button_bg, fg=fg_color, command=self.check_balance)
        self.balance_button.pack(pady=5)
        self.balance_button.bind("<Enter>", lambda e: self.balance_button.config(bg=hover_bg))
        self.balance_button.bind("<Leave>", lambda e: self.balance_button.config(bg=button_bg))

        # Deposit
        self.deposit_button = tk.Button(self.master, text="Deposit", width=20, font=button_font,
                                        bg=button_bg, fg=fg_color, command=self.deposit)
        self.deposit_button.pack(pady=5)
        self.deposit_button.bind("<Enter>", lambda e: self.deposit_button.config(bg=hover_bg))
        self.deposit_button.bind("<Leave>", lambda e: self.deposit_button.config(bg=button_bg))

        # Withdraw
        self.withdraw_button = tk.Button(self.master, text="Withdraw", width=20, font=button_font,
                                        bg=button_bg, fg=fg_color, command=self.withdraw)
        self.withdraw_button.pack(pady=5)
        self.withdraw_button.bind("<Enter>", lambda e: self.withdraw_button.config(bg=hover_bg))
        self.withdraw_button.bind("<Leave>", lambda e: self.withdraw_button.config(bg=button_bg))

        # Exit
        self.exit_button = tk.Button(self.master, text="Exit", width=20, font=button_font,
                                    bg="#cc0000", fg="white", command=self.master.quit)
        self.exit_button.pack(pady=5)
        self.exit_button.bind("<Enter>", lambda e: self.exit_button.config(bg="#990000"))
        self.exit_button.bind("<Leave>", lambda e: self.exit_button.config(bg="#cc0000"))


    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
            if amount is None:
                return
            if amount <= 0:
                messagebox.showerror("Error", "Enter a valid amount.")
            else:
                self.balance += amount
                messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully.")
        except:
            messagebox.showerror("Error", "Invalid input.")

    def withdraw(self):
        try:
            amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
            if amount is None:
                return
            if amount <= 0:
                messagebox.showerror("Error", "Enter a valid amount.")
            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully.")
        except:
            messagebox.showerror("Error", "Invalid input.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()