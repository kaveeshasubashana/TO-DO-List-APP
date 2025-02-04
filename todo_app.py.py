import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.font import Font


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        # Dark mode toggle
        self.is_dark_mode = False

        # Fonts
        self.title_font = Font(family="Helvetica", size=18, weight="bold")
        self.task_font = Font(family="Helvetica", size=14)

        # UI Setup
        self.title_label = tk.Label(self.root, text="TODO LIST", font=self.title_font)
        self.title_label.pack(pady=10)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, font=self.task_font, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(
            self.input_frame, text="ADD", font=self.task_font, command=self.add_task, bg="#4CAF50", fg="white"
        )
        self.add_button.grid(row=0, column=1)

        self.task_listbox_frame = tk.Frame(self.root)
        self.task_listbox_frame.pack(pady=10)

        self.delete_all_button = tk.Button(
            self.root, text="Delete All Tasks", font=self.task_font, command=self.delete_all_tasks, bg="#FF9800", fg="white"
        )
        self.delete_all_button.pack(pady=5)

        self.theme_button = tk.Button(
            self.root, text="Toggle Dark Mode", font=self.task_font, command=self.toggle_dark_mode, bg="#2196F3", fg="white"
        )
        self.theme_button.pack(pady=5)

        # Store tasks and widgets
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.create_task_widget(task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def create_task_widget(self, task_text):
        task_frame = tk.Frame(self.task_listbox_frame, bg=self.get_bg_color())
        task_frame.pack(fill="x", pady=5, padx=10)

        task_label = tk.Label(task_frame, text=task_text, font=self.task_font, bg=self.get_bg_color(), fg=self.get_fg_color())
        task_label.pack(side="left", padx=5)

        delete_button = tk.Button(
            task_frame, text="Delete", font=("Helvetica", 12), command=lambda: self.delete_task(task_frame), bg="#F44336", fg="white"
        )
        delete_button.pack(side="right", padx=5)

        edit_button = tk.Button(
            task_frame, text="Edit", font=("Helvetica", 12), command=lambda: self.edit_task(task_frame, task_label), bg="#2196F3", fg="white"
        )
        edit_button.pack(side="right", padx=5)

        self.tasks.append(task_frame)

    def delete_task(self, task_frame):
        self.tasks.remove(task_frame)
        task_frame.destroy()

    def delete_all_tasks(self):
        for task_frame in self.tasks:
            task_frame.destroy()
        self.tasks.clear()

    def edit_task(self, task_frame, task_label):
        new_text = simpledialog.askstring("Edit Task", "Enter new task:", initialvalue=task_label.cget("text"))
        if new_text:
            task_label.config(text=new_text)

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.update_theme()

    def update_theme(self):
        bg_color = self.get_bg_color()
        fg_color = self.get_fg_color()

        self.root.configure(bg=bg_color)
        self.title_label.configure(bg=bg_color, fg=fg_color)
        self.input_frame.configure(bg=bg_color)
        self.task_entry.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.add_button.configure(bg="#4CAF50", fg="white")
        self.delete_all_button.configure(bg="#FF9800", fg="white")
        self.theme_button.configure(bg="#2196F3", fg="white")

        for task_frame in self.tasks:
            task_frame.configure(bg=bg_color)
            for widget in task_frame.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.configure(bg=bg_color, fg=fg_color)
                elif isinstance(widget, tk.Button):
                    widget.configure(bg="#F44336" if widget.cget("text") == "Delete" else "#2196F3", fg="white")

    def get_bg_color(self):
        return "#121212" if self.is_dark_mode else "#E8E8E8"

    def get_fg_color(self):
        return "white" if self.is_dark_mode else "black"

    def run(self):
        self.root.mainloop()


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    app.run()
