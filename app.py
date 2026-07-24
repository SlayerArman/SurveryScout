import tkinter as tk
import platform

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

    computer_name = platform.node()

    computer_label = tk.Label(
        info_frame,
        text=f"Computer Name: {computer_name}",
        font=("Segoe UI", 11)
    )

    computer_label.pack(pady=20)

    operating_system = platform.system()
    os_version = platform.release()

    os_label = tk.Label(
        info_frame,
        text=f"Operating System: {operating_system} {os_version}",
        font=("Segoe UI", 11)
    )

    os_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()