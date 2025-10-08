
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        bmi = weight / (height ** 2)
        
        result = f"BMI : {bmi:.2f}\n"
        
        if bmi < 18.5:
            result += "Status: Under weight!"
            lbl_result.config(fg="orange")
        elif 18.5 <= bmi <= 24.9:
            result += "Status: Healthy weight"
            lbl_result.config(fg="green")

        elif 25 <= bmi <= 29.9:
            result += "status: Over weight"
            lbl_result.config(fg="darkorange")
        else:
            result += "status: Obesity"
            lbl_result.config(fg="red")
        
        lbl_result.config(text=result)
    
    except ValueError:
        messagebox.showerror("Error", "please enter your height and weight numerically.")

root = tk.Tk()
root.title("Calculator BMI")
root.geometry("400x300")
root.configure(bg="#f0f5f5")


lbl_title = tk.Label(root, text="Calculator BMI", font=("Arial", 16, "bold"), bg="#f0f5f5", fg="#333")
lbl_title.pack(pady=10)

lbl_weight = tk.Label(root, text="weight(Kg)", bg="#f0f5f5", font=("Arial", 12))
lbl_weight.pack(pady=5)
entry_weight = tk.Entry(root, font=("Arial", 12), justify="center")
entry_weight.pack(pady=5)

lbl_height = tk.Label(root, text="height(Mt)", bg="#f0f5f5", font=("Arial", 12))
lbl_height.pack(pady=5)
entry_height = tk.Entry(root, font=("Arial", 12), justify="center")
entry_height.pack(pady=5)


btn_calc = tk.Button(root, text="Calculation BMI", command=calculate_bmi, bg="#4CAF50", fg="white",
                     font=("Arial", 12, "bold"), relief="raised", padx=10, pady=5)
btn_calc.pack(pady=15)

lbl_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f5f5")
lbl_result.pack(pady=10)

root.mainloop()