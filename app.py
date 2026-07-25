import tkinter as tk
from tkinter import messagebox

from scout.report import save_report

from scout.system import (
    get_computer_name,
    get_memory,
    get_operating_system,
    get_processor,
    get_storage,
    get_current_user,
    get_python_version,
    get_cpu_usage,
)

def create_info_label(parent, text):
    label = tk.Label(
        parent,
        text=text,
        font=("Segoe UI", 11),
        anchor="w"
    )

    label.pack(
        fill="x",
        pady=6,
        anchor="w"
    )

    return label

def refresh_information(labels):
    labels["computer"].config(
        text=f"Computer Name: {get_computer_name()}"
    )

    labels["user"].config(
        text=f"Current User: {get_current_user()}"
    )
    

    labels["os"].config(
        text=f"Operating System: {get_operating_system()}"
    )

    labels["python"].config(
        text=f"Python Version: {get_python_version()}"
    )

    labels["processor"].config(
        text=f"Processor: {get_processor()}"
    )

    labels["cpu"].config(
        text=f"CPU Usage: {get_cpu_usage()}"
    )

    labels["memory"].config(
        text=f"Installed Memory: {get_memory()}"
    )

    labels["storage"].config(
        text=f"Storage: {get_storage()}"
    )

def export_report():
    report = [
        f"Computer Name: {get_computer_name()}",
        f"Computer User: {get_current_user()}"
        f"Operating System: {get_operating_system()}",
        f"Python Version: {get_python_version()}",
        f"Processor: {get_processor()}",
        f"CPU Usage: {get_cpu_usage}",
        f"Installed Memory: {get_memory()}",
        f"Storage: {get_storage()}",
    ]

    filename = save_report(report)

def copy_report(root):
    report = [
        f"Computer Name: {get_computer_name()}",
        f"Current User: {get_current_user()}",
        f"Operating System: {get_operating_system()}",
        f"Python Version: {get_python_version()}",
        f"Processor: {get_processor()}",
        f"CPU Usage: {get_cpu_usage()}",
        f"Installed Memory: {get_memory()}",
        f"Storage: {get_storage()}",
    ]

    root.clipboard_clear()
    root.clipboard_append("\n".join(report))
    root.update()

    messagebox.showinfo(
        "Copied",
        "System information has been copied to the clipboard"
    )

def show_about():
    messagebox.showinfo(
        "About Operation Scout",
        (
            "Operation Scout\n"
            "Version 1.0\n\n"
            "A beginner-friendly desktop application for"
            "viewing basic system information"
        )
    )

    messagebox.showinfo(
        "Report Saved",
        f"System report saved to:\n\n{filename}"
    )

def main():
    root = tk.Tk()

    root.title("Operation Scout")
    root.geometry("700x500")
    root.minsize(500, 350)

    heading = tk.Label(
        root,
        text="Operation Scout",
        font=("Segoe UI", 20, "bold")
    )

    heading.pack(pady=(20, 5))

    subtitle = tk.Label(
        root,
        text="System Information",
        font=("Segoe UI", 11)
    )

    subtitle.pack()

    separator = tk.Frame(
        root,
        height=2,
        bg="#d9d9d9"
    )

    separator.pack(fill="x", padx=30, pady=(15, 10))

    info_frame = tk.Frame(root)
    info_frame.pack(fill="x", padx=30, pady=25)

    computer_name = get_computer_name()

    computer_label = create_info_label(
        info_frame,
        f"Computer Name: {computer_name}"
    )

    current_user = get_current_user()

    user_label = create_info_label(
        info_frame,
        f"Current User: {current_user}"
    )

    operating_system = get_operating_system()

    os_label = create_info_label(
        info_frame,
        f"Operating System: {operating_system}"
    )

    python_version = get_python_version()

    python_label = create_info_label(
        info_frame,
        f"Python Version: {python_version}"
    )

    processor = get_processor()

    processor_label = create_info_label(
        info_frame,
        f"Processor: {processor}"
    )

    cpu_usage = get_cpu_usage()

    cpu_label = create_info_label(
        info_frame,
        f"CPU Usage: {cpu_usage}"
    )

    memory = get_memory()

    memory_label = create_info_label(
        info_frame,
        f"Installed Memory: {memory}"
    )

    storage = get_storage()

    storage_label = create_info_label(
        info_frame,
        f"Storage: {storage}"
    )

    labels = {
        "computer": computer_label,
        "user": user_label,
        "os": os_label,
        "python": python_label,
        "processor": processor_label,
        "cpu": cpu_label,
        "memory": memory_label,
        "storage": storage_label,
    }

    button_frame = tk.Frame(root)
    button_frame.pack(pady=15)

    copy_button = tk.Button(
        button_frame,
        text="Copy Report",
        width=15,
        command=lambda: copy_report(root)
    )

    copy_button.pack(side="left", padx=10)

    export_button = tk.Button(
        button_frame,
        text="Export Report",
        width=15,
        command=export_report
    )

    export_button.pack(side="left", padx=10)

    refresh_button = tk.Button(
        button_frame,
        text="Refresh",
        width=15,
        command=lambda: refresh_information(labels)
    )

    refresh_button.pack(side="left", padx=10)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar) 

    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(
        label="Copy Report",
        command=lambda: copy_report(root)
    )

    file_menu.add_command(
        label="Export Report",
        command=export_report
    )

    file_menu.add_separator()

    file_menu.add_command(
        label="Exit",
        accelerator="Ctrl+Q",
        command=root.destroy
    )

    help_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    help_menu.add_command(
        label="About",
        command=show_about
    )

    root.bind("<Control-q>", lambda event: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()