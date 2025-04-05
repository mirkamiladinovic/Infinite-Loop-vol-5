import tkinter as tk
from tkinter import ttk
import threading
import time

"""
- Authors: xor525 (class, logic), Andrejj005 (tkinter)
- Date: 05/4/2025
- src/vega.py
"""

class Vega:
    __slots__ = ('file', 'limit')
    
    def __init__(self, file: str, limit: int):
        self.file = file
        self.limit = limit

    def pisanje_errora(self) -> None:
        def task() -> None:
            error_lines = [line for line in self.file if "ERROR" in line]
            label_status.config(text="Pisanje ERROR logova...")

            with open("error.txt", "w") as err_file:
                for err in error_lines:
                    err_file.write(err)
                    root.update_idletasks()


    def brojanje_logova(self) -> None:
        counts = {
            "ERROR": 0,
            "WARNING": 0,
            "INFO": 0,
            "DEBUG": 0
        }

        for line in self.file:
            for key in counts:
                if key in line:
                    counts[key] += 1
                    break
        
        label_total.config(text=f"Ukupno logova: {total}")
        label_error.config(text=f"ERROR: {counts['ERROR']}")
        label_warn.config(text=f"WARNING: {counts['WARNING']}")
        label_info.config(text=f"INFO: {counts['INFO']}")
        label_debug.config(text=f"DEBUG: {counts['DEBUG']}")

    def search_sa_limitom(self) -> None:
        for i in range(self.limit):
            print(self.file[i])


def main() -> None:
    with open("../vegini_logovi.txt", "r") as logs:
        file = logs.readlines()

    root = tk.Tk()
    root.geometry("500x500")
    root.title("Vega Logovi GUI")
    tk.Label(root, text="Vega Log Analizator", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(frame_opts, text="Limit:").grid(row=0, column=0)
    entry_limit = tk.Entry(frame_opts, width=5)
    entry_limit.insert(0, "10")
    entry_limit.grid(row=0, column=1)
    tk.Label(frame_opts, text="Offset:").grid(row=0, column=2)
    entry_offset = tk.Entry(frame_opts, width=5)
    entry_offset.insert(0, "0")
    entry_offset.grid(row=0, column=3)
    
    vega = Vega(file, entry_limit)

    tk.Button(root, text="Pisanje ERROR-a u file", command=vega.pisanje_errora, width=30).pack(pady=5)
    tk.Button(root, text="Brojanje logova", command=vega.brojanje_logova, width=30).pack(pady=5)
    tk.Button(root, text="Search limit", command=vega.search_sa_limitom, width=30).pack(pady=5)

    label_total = tk.Label(root, text="Ukupno logova: 0")
    label_total.pack()

    label_error = tk.Label(root, text="ERROR: 0")
    label_error.pack()

    label_warn = tk.Label(root, text="WARNING: 0")
    label_warn.pack()

    label_info = tk.Label(root, text="INFO: 0")
    label_info.pack()

    label_debug = tk.Label(root, text="DEBUG: 0")
    label_debug.pack()

    progress_bar = ttk.Progressbar(root, length=400)
    progress_bar.pack(pady=15)

    label_status = tk.Label(root, text="")
    label_status.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
