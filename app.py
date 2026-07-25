import tkinter as tk
from tkinter import messagebox

from scout.report import save_report

from scout.system import (
    get_computer_name,
    get_memory,
    get_operating_system,
    get_processor,
    get_storage,
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

    labels["os"].config(
        text=f"Operating System: {get_operating_system()}"
    )

    labels["processor"].config(
        text=f"Processor: {get_processor()}"
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
        f"Operating System: {get_operating_system()}",
        f"Processor: {get_processor()}",
        f"Installed Memory: {get_memory()}",
        f"Storage: {get_storage()}",
    ]

    filename = save_report(report)

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

    operating_system = get_operating_system()

    os_label = create_info_label(
        info_frame,
        f"Operating System: {operating_system}"
    )

    processor = get_processor()

    processor_label = create_info_label(
        info_frame,
        f"Processor: {processor}"
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
        "os": os_label,
        "processor": processor_label,
        "memory": memory_label,
        "storage": storage_label,
    }

    button_frame = tk.Frame(root)
    button_frame.pack(pady=15)

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
        label="Export Report",
        command=export_report
    )

    file_menu.add_separator()

    file_menu.add_command(
        label="Exit",
        accelerator="Ctrl+Q",
        command=root.destroy
    )

    root.bind("<Control-q>", lambda event: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()