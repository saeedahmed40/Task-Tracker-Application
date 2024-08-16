import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Set a modern theme for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Task entry
        self.task_entry_frame = ttk.Frame(root, padding=(10, 10))
        self.task_entry_frame.pack(fill="x")

        self.task_entry = ttk.Entry(self.task_entry_frame, width=40)
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        add_button = ttk.Button(self.task_entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side="right")

        # Task list
        self.task_list_frame = ttk.Frame(root, padding=(10, 0))
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list = tk.Listbox(self.task_list_frame, height=10, activestyle="none", selectmode="single", bg="#ffffff", fg="#333333", font=("Helvetica", 12))
        self.task_list.pack(side="left", fill="both", expand=True)

        self.task_scrollbar = ttk.Scrollbar(self.task_list_frame, orient="vertical", command=self.task_list.yview)
        self.task_scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.task_scrollbar.set)

        # Delete button
        self.button_frame = ttk.Frame(root, padding=(10, 10))
        self.button_frame.pack(fill="x")

        delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side="right")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()