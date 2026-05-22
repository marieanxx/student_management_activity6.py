import tkinter as tk
from tkinter import messagebox

students = []
student_labels = []

window = tk.Tk()
window.title("Student Management System")
window.geometry("750x700")
window.resizable(True, True)
window.configure(bg="#F0F0F0")

title_label = tk.Label(window,
                       text = "STUDENT MANAGEMENT SYSTEM",
                       font = ("Arial", 16, "bold"),
                       bg ="#F0F0F0",
                       fg ="#800080")

name_label = tk.Label(window, 
                      text ="Student Name:", 
                      font = ("Arial", 11), 
                      bg ="#F0F0F0",
                      fg = "#800080")
name_entry = tk.Entry(window, width=35, font=("Arial", 11))

id_label = tk.Label(window, 
                    text ="Student ID:", 
                    font = ("Arial", 11), 
                    bg ="#F0F0F0",
                    fg = "#800080")
id_entry = tk.Entry(window, width=35, font=("Arial", 11))

email_label = tk.Label(window, 
                       text ="Email:", 
                       font = ("Arial", 11), 
                       bg ="#F0F0F0",
                       fg = "#800080")
email_entry = tk.Entry(window, width=35, font=("Arial", 11))

phone_label = tk.Label(window, 
                       text ="Phone Number:", 
                       font = ("Arial", 11), 
                       bg ="#F0F0F0",
                       fg = "#800080")
phone_entry = tk.Entry(window, width=35, font=("Arial", 11))

course_label = tk.Label(window, 
                        text ="Course:", 
                        font = ("Arial", 11), 
                        bg ="#F0F0F0",
                        fg = "#800080")
course_entry = tk.Entry(window, width=35, font=("Arial", 11))

year_label = tk.Label(window, 
                      text="Year Level:", 
                      font= ("Arial", 11), 
                      bg="#F0F0F0",
                      fg = "#800080")
year_entry = tk.Entry(window, width=35, font=("Arial", 11))

gpa_label = tk.Label(window,
                     text = "GPA: ",
                     font = ("Arial", 11),
                     bg = "#F0F0F0",
                     fg = "#800080")
gpa_entry = tk.Entry(window, width=35, font=("Arial", 11))

status_label = tk.Label(window,
                     text = "Status: ",
                     font = ("Arial", 11),
                     bg = "#F0F0F0",
                     fg = "#800080")
status_entry = tk.Entry(window, width=35, font=("Arial", 11))

def addStudents():
    name = name_entry.get()
    student_id = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()
    year = year_entry.get()
    gpa = gpa_entry.get()
    status = status_entry.get()

    if not name or not student_id or not email or not phone or not course or not year:
        messagebox.showwarning("Warning", "Please complete all information!")
        return

    student = {
        "name": name,
        "id": student_id,
        "email": email,
        "phone": phone,
        "course": course,
        "year": year,
        "gpa": gpa,
        "status": status
    }

    students.append(student)

    student_text = f"Name: {name} | ID: {student_id} | Email: {email} | Phone: {phone} | Course: {course} | Year: {year} | GPA: {gpa} | Status: {status}"
    student_label = tk.Label(list_frame, text=student_text, font=("Arial", 10), bg="#FFFFFF")
    student_label.pack(fill="x", pady=1)
    student_labels.append(student_label)

    total_label.config(text=f"Total Students: {len(students)}")

    clearFields()

def clearFields():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    gpa_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

def deleteLastStudent():
    if len(students) == 0:
        messagebox.showinfo("Info", "No student record to delete.")
        return
    
    students.pop()
    last_label = student_labels.pop()
    last_label.destroy()

button_frame = tk.Frame(window, bg="#F0F0F0")
btn_add = tk.Button(button_frame,
                    text="Add Student",
                    font=("Arial", 10, "bold"),
                    bg="#2D0C5E",
                    fg="#FFFFFF",
                    width=15,
                    command=addStudents)

btn_clear = tk.Button(button_frame,
                      text="Clear Fields",
                      font=("Arial", 10, "bold"),
                      bg="#2D0C5E",
                      fg="#FFFFFF",
                      width=15,
                      command=clearFields)

btn_delete = tk.Button(button_frame,
                       text = "Delete Last",
                       font = ("Arial", 10, "bold"),
                       bg = "#2D0C5E",
                       fg = "#FFFFFF",
                       width = 15,
                       command = deleteLastStudent)

total_label = tk.Label(window,
                      text ="Total Students: 0",
                      font =("Arial", 12, "bold"),
                      bg ="#F0F0F0",
                      fg = "#800080")

list_frame = tk.Frame(window,
                      bg ="#FFFFFF",
                      bd =1,
                      relief ="solid",
                      width =850,
                      height =250)
list_frame.pack_propagate(False)


title_label.pack(pady=15)

name_label.pack()
name_entry.pack(pady=2)
id_label.pack()
id_entry.pack(pady=2)
email_label.pack()
email_entry.pack(pady=2)
phone_label.pack()
phone_entry.pack(pady=2)
course_label.pack()
course_entry.pack(pady=2)
year_label.pack()
year_entry.pack(pady=2)
gpa_label.pack()
gpa_entry.pack(pady=2)
status_label.pack()
status_entry.pack(pady=2)

button_frame.pack(pady=15)
btn_add.pack(side=tk.LEFT, padx=5)   
btn_clear.pack(side=tk.LEFT, padx=5) 
btn_delete.pack(side=tk.LEFT, padx=5)

total_label.pack()
list_frame.pack(padx=20, pady=5)

window.mainloop()
