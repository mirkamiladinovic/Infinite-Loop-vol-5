import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
import re
from datetime import datetime
from collections import defaultdict
import os

LOG_PATTERN = re.compile(r"\[(.*?)\]\s+(DEBUG|INFO|WARNING|ERROR)\s+\S+\s+([\w\.]+):\s+(.*)")
LOG_TYPES = ["DEBUG", "INFO", "WARNING", "ERROR"]

LOG_COLORS = {
    "DEBUG": "gray",
    "INFO": "blue",
    "WARNING": "orange",
    "ERROR": "red"
}

class LogAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Log Analyzer")
        master.geometry("900x600")

        self.logs = []
        self.parsed_logs = []
        self.displayed_logs = []
        self.sort_ascending = True

        self.setup_ui()
        self.set_inputs_state("disabled")

    def setup_ui(self):
        # Top Controls
        top_frame = tk.Frame(self.master)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="Load Log File", command=self.load_file).pack(side=tk.LEFT, padx=5)
        self.count_button = tk.Button(top_frame, text="Count Types", command=self.count_log_types)
        self.count_button.pack(side=tk.LEFT, padx=5)
        self.top_files_button = tk.Button(top_frame, text="Top 5 Problem Files", command=self.top_error_files)
        self.top_files_button.pack(side=tk.LEFT, padx=5)
        self.export_button = tk.Button(top_frame, text="Export ERROR Logs", command=self.export_errors)
        self.export_button.pack(side=tk.LEFT, padx=5)
        self.sort_button = tk.Button(top_frame, text="Sort by Date ↑", command=self.sort_by_date)
        self.sort_button.pack(side=tk.LEFT, padx=5)

        # Filters
        filter_frame = tk.LabelFrame(self.master, text="Filters")
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(filter_frame, text="Search Text:").grid(row=0, column=0)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.grid(row=0, column=1)

        tk.Label(filter_frame, text="Log Type:").grid(row=0, column=2)
        self.type_var = tk.StringVar(value="ALL")
        self.type_menu = tk.OptionMenu(filter_frame, self.type_var, "ALL", *LOG_TYPES)
        self.type_menu.grid(row=0, column=3)

        tk.Label(filter_frame, text="From Date:").grid(row=1, column=0)
        self.from_entry = DateEntry(filter_frame, date_pattern='yyyy-mm-dd')
        self.from_entry.grid(row=1, column=1)

        tk.Label(filter_frame, text="To Date:").grid(row=1, column=2)
        self.to_entry = DateEntry(filter_frame, date_pattern='yyyy-mm-dd')
        self.to_entry.grid(row=1, column=3)

        tk.Label(filter_frame, text="Limit:").grid(row=2, column=0)
        self.limit_entry = tk.Entry(filter_frame)
        self.limit_entry.grid(row=2, column=1)

        tk.Label(filter_frame, text="Offset:").grid(row=2, column=2)
        self.offset_entry = tk.Entry(filter_frame)
        self.offset_entry.grid(row=2, column=3)

        self.apply_button = tk.Button(filter_frame, text="Apply Filters", command=self.apply_filters)
        self.apply_button.grid(row=3, column=0, columnspan=4, pady=5)

        # Text Area
        self.text_area = tk.Text(self.master, wrap=tk.NONE)
        self.text_area.pack(fill="both", expand=True, padx=10, pady=5)

        # Reset Button
        self.reset_button = tk.Button(self.master, text="Show All Logs", command=self.reset_logs)
        self.reset_button.pack(pady=5)

    def set_inputs_state(self, state):
        self.export_button.config(state=state)
        self.count_button.config(state=state)
        self.top_files_button.config(state=state)
        self.search_entry.config(state=state)
        self.from_entry.config(state=state)
        self.to_entry.config(state=state)
        self.limit_entry.config(state=state)
        self.offset_entry.config(state=state)
        self.apply_button.config(state=state)
        self.reset_button.config(state=state)
        self.sort_button.config(state=state)
        menu = self.type_menu["menu"]
        for i in range(menu.index("end") + 1):
            menu.entryconfig(i, state=state)
        self.type_menu.config(state=state)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[["Text Files", "*.txt"]])
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as file:
            self.logs = file.readlines()

        self.parsed_logs = self.parse_logs(self.logs)
        self.displayed_logs = self.parsed_logs[:]
        self.set_date_range()
        self.display_logs(self.displayed_logs)
        self.set_inputs_state("normal")
        messagebox.showinfo("Loaded", f"{len(self.parsed_logs)} valid log entries loaded.")

    def set_date_range(self):
        if not self.parsed_logs:
            return
        dates = [log["timestamp"] for log in self.parsed_logs]
        min_date = min(dates).date()
        max_date = max(dates).date()

        self.from_entry.config(mindate=min_date, maxdate=max_date)
        self.to_entry.config(mindate=min_date, maxdate=max_date)
        self.from_entry.set_date(min_date)
        self.to_entry.set_date(max_date)

    def parse_logs(self, lines):
        parsed = []
        for line in lines:
            match = LOG_PATTERN.match(line)
            if match:
                timestamp_str, log_type, filename, message = match.groups()
                try:
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
                except ValueError:
                    continue
                parsed.append({
                    "timestamp": timestamp,
                    "type": log_type,
                    "filename": filename,
                    "message": message,
                    "raw": line
                })
        return parsed

    def export_errors(self):
        errors = [log["raw"] for log in self.parsed_logs if log["type"] == "ERROR"]
        if not errors:
            messagebox.showwarning("No errors", "No ERROR logs found.")
            return
        output_dir = os.path.abspath("output")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "errors_only.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(errors)
        messagebox.showinfo("Exported", f"{len(errors)} ERROR logs saved to:\n{output_path}")

    def count_log_types(self):
        counts = defaultdict(int)
        for log in self.parsed_logs:
            counts[log["type"]] += 1
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Log Level Counts:\n")
        for typ in LOG_TYPES:
            line = f"{typ}: {counts[typ]}\n"
            self.text_area.insert(tk.END, line, typ)
            self.text_area.tag_config(typ, foreground=LOG_COLORS.get(typ, "black"))

    def top_error_files(self):
        error_counts = defaultdict(int)
        for log in self.parsed_logs:
            if log["type"] == "ERROR":
                error_counts[log["filename"]] += 1
        sorted_files = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Top 5 Files with Most Errors:\n")
        if not sorted_files:
            self.text_area.insert(tk.END, "No ERROR logs found.\n")
            return
        for fname, count in sorted_files:
            self.text_area.insert(tk.END, f"{fname}: {count}\n")

    def apply_filters(self):
        result = self.parsed_logs

        query = self.search_entry.get().lower()
        log_type = self.type_var.get()
        from_date = self.from_entry.get()
        to_date = self.to_entry.get()
        limit = self.limit_entry.get()
        offset = self.offset_entry.get()

        if query:
            result = [log for log in result if query in log["message"].lower() or query in log["filename"].lower()]

        if log_type != "ALL":
            result = [log for log in result if log["type"] == log_type]

        if from_date:
            try:
                dt = datetime.strptime(from_date, "%Y-%m-%d")
                result = [log for log in result if log["timestamp"] >= dt]
            except ValueError:
                pass

        if to_date:
            try:
                dt = datetime.strptime(to_date, "%Y-%m-%d")
                result = [log for log in result if log["timestamp"] <= dt]
            except ValueError:
                pass

        try:
            offset = int(offset) if offset else 0
            limit = int(limit) if limit else len(result)
            result = result[offset:offset + limit]
        except ValueError:
            pass

        self.displayed_logs = result
        self.display_logs(self.displayed_logs)

    def reset_logs(self):
        self.displayed_logs = self.parsed_logs[:]
        self.display_logs(self.displayed_logs)

    def sort_by_date(self):
        self.sort_ascending = not self.sort_ascending
        self.displayed_logs = sorted(self.displayed_logs, key=lambda log: log["timestamp"], reverse=not self.sort_ascending)
        self.display_logs(self.displayed_logs)
        self.sort_button.config(text=f"Sort by Date {'↑' if self.sort_ascending else '↓'}")

    def display_logs(self, logs):
        self.text_area.delete(1.0, tk.END)
        for log in logs:
            color = LOG_COLORS.get(log["type"], "black")
            self.text_area.insert(tk.END, log["raw"], log["type"])
            self.text_area.tag_config(log["type"], foreground=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerApp(root)
    root.mainloop()
