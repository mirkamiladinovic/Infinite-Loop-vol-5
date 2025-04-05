import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import re
from datetime import datetime
from tkcalendar import DateEntry
import subprocess
import importlib.util
import os

log_file_path = None

script_dir = os.path.dirname(os.path.abspath(__file__))
vz1_path = os.path.join(script_dir, "vz1.py")
vz2_path = os.path.join(script_dir, "vz2.py")
vz3_path = os.path.join(script_dir, "vz3.py")

# Glavni prozor
window = tk.Tk()
window.title("Log Viewer")
window.geometry("600x500")

# Funkcije
def open_file():
    global log_file_path
    file_path = filedialog.askopenfilename(title="Select log file", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        log_file_path = file_path
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, f"Log fajl učitan:\n{log_file_path}\n")

def parse_log_line(line):
    match = re.match(r"\[(.*?)\] (\w+) .*?: (.*)", line)
    if match:
        date_str, level, message = match.groups()
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        return {"date": date, "level": level, "message": message, "raw": line.strip()}
    return None

def apply_filters():
    try:
        limit = int(limit_entry.get() or 0)
        offset = int(offset_entry.get() or 0)
    except ValueError:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "Limit and offset must be integers.")
        return

    sort = sort_order.get()
    search_text = search_entry.get().lower()
    date_from_str = date_from_entry.get()
    date_to_str = date_to_entry.get()
    selected_levels = [level for level, var in log_level_vars.items() if var.get()]

    date_from = datetime.strptime(date_from_str, "%m/%d/%Y") if date_from_str and date_from_check.get() else None
    date_to = datetime.strptime(date_to_str, "%m/%d/%Y") if date_to_str and date_to_check.get() else None

    if not log_file_path:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "No log file selected.")
        return

    logs = []
    matched_count = 0

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            if selected_levels and parsed["level"] not in selected_levels:
                continue
            if search_text and search_text not in parsed["message"].lower() and search_text not in parsed["raw"].lower():
                continue
            if date_from and parsed["date"] < date_from:
                continue
            if date_to and parsed["date"] > date_to:
                continue

            if matched_count < offset:
                matched_count += 1
                continue

            logs.append(parsed)

            if limit and len(logs) >= limit:
                break

    if sort == "desc":
        logs.sort(key=lambda log: log["date"], reverse=True)
    elif sort == "asc":
        logs.sort(key=lambda log: log["date"])

    output_text.delete('1.0', tk.END)
    if logs:
        output_text.insert(tk.END, "\n".join(log["raw"] for log in logs))
    else:
        output_text.insert(tk.END, "No logs match the filters.")

def run_make_error_file():
    if not log_file_path:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "Greška: fajl nije učitan.\n")
        return

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        vz3_path = os.path.join(current_dir, "vz3.py")

        spec = importlib.util.spec_from_file_location("vz3", vz3_path)
        vz3 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vz3)

        error_output_path = os.path.join(script_dir, "error_logs.txt")

        vz3.extract_error_lines(log_file_path, error_output_path)

        with open(error_output_path, "r", encoding="utf-8") as f:
            error_content = f.read()

        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, f"Napravljen fajl sa greškama:\n\n{error_content}")

    except Exception as e:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, f"Greška pri izvršavanju:\n{e}")

def run_external_script(script_name):
    if not log_file_path:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "Nema učitanog fajla.\n")
        return

    try:
        result = subprocess.run(
            ["python", script_name, log_file_path],
            capture_output=True, text=True, check=True
        )
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, result.stdout)

    except subprocess.CalledProcessError as e:
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, f"Greška pri izvršavanju skripte:\n{e.stderr}")

# File selection
file_frame = ttk.Frame(window)
file_frame.pack(fill='x', padx=10, pady=5)

open_button = ttk.Button(file_frame, text="Open Log File", command=open_file)
open_button.pack(side='left')

# Limit & Offset
limit_offset_frame = ttk.LabelFrame(window, text="Limit & Offset")
limit_offset_frame.pack(fill='x', padx=10, pady=5)

tk.Label(limit_offset_frame, text="Limit:").pack(side='left', padx=5)
limit_entry = ttk.Entry(limit_offset_frame, width=10)
limit_entry.pack(side='left')

tk.Label(limit_offset_frame, text="Offset:").pack(side='left', padx=5)
offset_entry = ttk.Entry(limit_offset_frame, width=10)
offset_entry.pack(side='left')

# Sort by date
sort_frame = ttk.LabelFrame(window, text="Sort by Date")
sort_frame.pack(fill='x', padx=10, pady=5)

sort_order = tk.StringVar(value="asc")
ttkw = ttk.Radiobutton

ttkw(sort_frame, text='Ascending', variable=sort_order, value='asc').pack(side='left', padx=5)
ttkw(sort_frame, text='Descending', variable=sort_order, value='desc').pack(side='left', padx=5)

# Filter by log level
log_level_frame = ttk.LabelFrame(window, text="Log Level")
log_level_frame.pack(fill='x', padx=10, pady=5)

log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
log_level_vars = {level: tk.BooleanVar() for level in log_levels}

for level in log_levels:
    ttk.Checkbutton(log_level_frame, text=level, variable=log_level_vars[level]).pack(side='left', padx=5)

# Search text
search_frame = ttk.LabelFrame(window, text="Search Text")
search_frame.pack(fill='x', padx=10, pady=5)

search_entry = ttk.Entry(search_frame)
search_entry.pack(fill='x', padx=5, pady=5)

# Date range filter
date_range_frame = ttk.LabelFrame(window, text="Date Range (MM/DD/YY)")
date_range_frame.pack(fill='x', padx=10, pady=5)

date_from_check = tk.BooleanVar(value=False)
date_to_check = tk.BooleanVar(value=False)

tk.Label(date_range_frame, text="From:").pack(side='left', padx=5)
date_from_entry = DateEntry(date_range_frame, width=12, date_pattern='mm/dd/yyyy')
date_from_entry.pack(side='left', padx=5)

date_from_checkbox = ttk.Checkbutton(date_range_frame, text="Use From Date", variable=date_from_check)
date_from_checkbox.pack(side='left', padx=5)

tk.Label(date_range_frame, text="To:").pack(side='left', padx=5)
date_to_entry = DateEntry(date_range_frame, width=12, date_pattern='mm/dd/yyyy')
date_to_entry.pack(side='left', padx=5)

date_to_checkbox = ttk.Checkbutton(date_range_frame, text="Use To Date", variable=date_to_check)
date_to_checkbox.pack(side='left', padx=5)

# Buttons
button_frame = ttk.Frame(window)
button_frame.pack(fill='x', padx=10, pady=5)

apply_button = ttk.Button(button_frame, text="Apply Filters", command=apply_filters)
apply_button.pack(side='left', padx=5)

# Operacije nad fajlom
operation_frame = ttk.LabelFrame(window, text="Operations on the whole file")
operation_frame.pack(fill='x', padx=10, pady=5)

vz1_button = ttk.Button(operation_frame, text="Analyse log level", command=lambda: run_external_script(vz1_path))
vz1_button.pack(side='left', padx=5)

vz2_button = ttk.Button(operation_frame, text="Top 5 files with ERRORs", command=lambda: run_external_script(vz2_path))
vz2_button.pack(side='left', padx=5)

make_error_button = ttk.Button(operation_frame, text="Make Error File", command=run_make_error_file)
make_error_button.pack(side='left', padx=5)

# Log output
output_frame = ttk.LabelFrame(window, text="Log Output")
output_frame.pack(fill='both', expand=True, padx=10, pady=5)

output_text = tk.Text(output_frame, wrap='none')
output_text.pack(fill='both', expand=True)

x_scroll = ttk.Scrollbar(output_frame, orient='horizontal', command=output_text.xview)
x_scroll.pack(side='bottom', fill='x')
output_text.configure(xscrollcommand=x_scroll.set)

y_scroll = ttk.Scrollbar(output_frame, orient='vertical', command=output_text.yview)
y_scroll.pack(side='right', fill='y')
output_text.configure(yscrollcommand=y_scroll.set)

# Pokretanje aplikacije
window.mainloop()