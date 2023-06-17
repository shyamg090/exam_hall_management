from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        # Admin role
        messagebox.showinfo("Login Successful", "Welcome "+ username)
        enable_admin_features()
    elif username == "student" and password == "student":
        # Student role
        messagebox.showinfo("Login Successful", "Welcome "+username)
        # enable_student_features()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to enable features for the admin role
def enable_admin_features():
    register_button.config(state=tk.NORMAL)
    edit_button.config(state=tk.NORMAL)
    delete_button.config(state=tk.NORMAL)

# Function to enable features for the student role
# def enable_student_features():
    # register_button.config(state=tk.NORMAL)

# Function to handle the registration of a new student
def register_student():
    usn = usn_entry.get()
    name = name_entry.get()
    department = department_entry.get()
    room = room_entry.get()

    if usn and name and department and room:
        record = f"{usn}|{name}|{department}|{room}\n"
        try:
            with open("examHall.txt", "a") as file:
                file.write(record)
            messagebox.showinfo("Success", "Student registered successfully.")
            clear_entries()
        except IOError:
            messagebox.showerror("Error", "Failed to write to file.")
    else:
        messagebox.showwarning("Warning", "Please fill in all the fields.")

# Function to handle the search and display of student records
def search_students():
    search_query = search_entry.get()

    if search_query:
        try:
            with open("examHall.txt", "r") as file:
                students = file.readlines()

            found_students = []
            for student in students:
                usn, name, department, room = student.strip().split("|")
                if search_query.lower() in usn.lower() or search_query.lower() in name.lower():
                    found_students.append(student)

            if found_students:
                display_text.delete("1.0", tk.END)
                display_text.insert(tk.END, "Search Results:\n\n")
                for student in found_students:
                    display_text.insert(tk.END, student)
            else:
                display_text.delete("1.0", tk.END)
                display_text.insert(tk.END, "No matching records found.")
        except IOError:
            messagebox.showerror("Error", "Failed to read from file.")
    else:
        messagebox.showwarning("Warning", "Please enter a search query.")

# Function to handle the editing and updating of student records
def edit_student():
    selected_student = display_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    selected_student_index = display_text.tag_ranges(tk.SEL)
    if selected_student_index:
        usn, name, department, room = selected_student.strip().split("|")
        usn_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        room_entry.delete(0, tk.END)

        usn_entry.insert(tk.END, usn)
        name_entry.insert(tk.END, name)
        department_entry.insert(tk.END, department)
        room_entry.insert(tk.END, room)

        display_text.delete(selected_student_index[0], selected_student_index[1])
    else:
        messagebox.showwarning("Warning", "Please select a student to edit.")

# Function to handle the deletion of student records
def delete_student():
    selected_student = display_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    selected_student_index = display_text.tag_ranges(tk.SEL)
    if selected_student_index:
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this student?")
        if confirm:
            try:
                with open("examHall.txt", "r") as file:
                    students = file.readlines()

                with open("examHall.txt", "w") as file:
                    for student in students:
                        if student.strip() != selected_student.strip():
                            file.write(student)

                display_text.delete(selected_student_index[0], selected_student_index[1])
                messagebox.showinfo("Success", "Student deleted successfully.")
            except IOError:
                messagebox.showerror("Error", "Failed to delete student.")
    else:
        messagebox.showwarning("Warning", "Please select a student to delete.")

# Function to clear the entry fields
def clear_entries():
    usn_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Exam Conduction Management")

# Set window size and position
window_width = 600
window_height = 400
filename=PhotoImage(file="C://Users//samsh//OneDrive//Desktop//Exam_Conduction_Management//sce.png")
background_label= Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place widgets for login
login_frame = tk.LabelFrame(root, text="Login", padx=8, pady=8, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
login_frame.pack(pady=8)

username_label = tk.Label(login_frame, text="Username:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
username_label.grid(row=0, column=0, sticky=tk.E)
username_entry = tk.Entry(login_frame, font=("Arial", 15))
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
password_label.grid(row=1, column=0, sticky=tk.E)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 15))
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
login_button.grid(row=2, column=1, pady=8)

# Create and place widgets for student registration
registration_frame = tk.LabelFrame(root, text="Student Registration", padx=8, pady=8, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
registration_frame.pack(pady=8)

usn_label = tk.Label(registration_frame, text="USN:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
usn_label.grid(row=0, column=0, sticky=tk.E)
usn_entry = tk.Entry(registration_frame, font=("Arial", 15))
usn_entry.grid(row=0, column=1)

name_label = tk.Label(registration_frame, text="Name:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
name_label.grid(row=1, column=0, sticky=tk.E)
name_entry = tk.Entry(registration_frame, font=("Arial", 15))
name_entry.grid(row=1, column=1)

department_label = tk.Label(registration_frame, text="Department:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
department_label.grid(row=2, column=0, sticky=tk.E)
department_entry = tk.Entry(registration_frame, font=("Arial", 15))
department_entry.grid(row=2, column=1)

room_label = tk.Label(registration_frame, text="Room:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
room_label.grid(row=3, column=0, sticky=tk.E)
room_entry = tk.Entry(registration_frame, font=("Arial", 15))
room_entry.grid(row=3, column=1)

register_button = tk.Button(registration_frame, text="Register", command=register_student, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
register_button.grid(row=4, column=1, pady=8)
register_button.config(state=tk.DISABLED)

# Set registration frame background color
registration_frame.configure(bg="#F2F7A1")

# Create and place widgets for search and display
search_frame = tk.LabelFrame(root, text="Search", padx=8, pady=8, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
search_frame.pack(pady=8)

search_label = tk.Label(search_frame, text="Search by USN or Name:", bg="#F2F7A1", fg="#080202", font=("Arial", 15))
search_label.grid(row=0, column=0, sticky=tk.E)
search_entry = tk.Entry(search_frame, font=("Arial", 15))
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_students, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
search_button.grid(row=0, column=2, padx=8)

display_text = tk.Text(root, height=8, width=50, bg="#F2F7A1", fg="#080202", bd="0", font=("Arial", 15))
display_text.pack(pady=8, padx=8)

# Create and place buttons for edit and delete
edit_button = tk.Button(root, text="Edit", command=edit_student, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
edit_button.pack(pady=8)
edit_button.config(state=tk.DISABLED)

delete_button = tk.Button(root, text="Delete", command=delete_student, bg="#F2F7A1", fg="#080202", font=("Arial", 15))
delete_button.pack(pady=8)
delete_button.config(state=tk.DISABLED)

# Set text widget font size
display_text.configure(font=("Arial", 15))

# Run the main event loop
root.mainloop()
