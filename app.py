import tkinter as tk

from scout.system import(
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

    label.pack(fill="x", pady=4)

    return label

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

    info_frame = tk.Frame(root)
    info_frame.pack(pady=25)

    computer_name = get_computer_name()

    create_info_label(
        info_frame,
        f"Computer Name: {computer_name}"
    )

    operating_system = get_operating_system()

    create_info_label(
        info_frame,
        f"Operating System: {operating_system}"
    )

    processor = get_processor()

    create_info_label(
        info_frame,
        f"Processor: {processor}"
    )

    memory = get_memory()

    create_info_label(
        info_frame,
        f"Installed Memory: {memory}"
    )

    storage = get_storage()

    create_info_label(
        info_frame,
        f"Storage: {storage}"
    )

    root.mainloop()

if __name__ == "__main__":
    main()