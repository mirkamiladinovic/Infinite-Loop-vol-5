import tkinter as tk
from tkinter import  messagebox, scrolledtext
from datetime import datetime
from log_utils import count_log_levels, extract_errors_to_file, get_top_error_files, filter_logs



class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Vega log ")
        self.file_path = "novi.txt"

        self.btn_count = tk.Button(root, text="Count Log Levels", command=self.count_logs)
        self.btn_count.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.btn_extract = tk.Button(root, text="Extract ERROR Logs", command=self.extract_errors)
        self.btn_extract.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.btn_top = tk.Button(root, text="Top 5 ERROR Services", command=self.top_errors)
        self.btn_top.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        
        filter_frame = tk.LabelFrame(root, text="Filter Logs")
        filter_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        
        tk.Label(filter_frame, text="Level:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.entry_level = tk.Entry(filter_frame)
        self.entry_level.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(filter_frame, text="Search Text:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.entry_search = tk.Entry(filter_frame)
        self.entry_search.grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(filter_frame, text="From Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.entry_from_date = tk.Entry(filter_frame)
        self.entry_from_date.grid(row=2, column=1, padx=5, pady=2)
        
        tk.Label(filter_frame, text="To Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.entry_to_date = tk.Entry(filter_frame)
        self.entry_to_date.grid(row=3, column=1, padx=5, pady=2)
        
        self.sort_var = tk.IntVar()
        self.chk_sort = tk.Checkbutton(filter_frame, text="Sort by time", variable=self.sort_var)
        self.chk_sort.grid(row=4, column=0, padx=5, pady=2, sticky="w")
        
        self.btn_filter = tk.Button(filter_frame, text="Filter Logs", command=self.filter_logs)
        self.btn_filter.grid(row=4, column=1, padx=5, pady=2)
        
        self.txt_output = scrolledtext.ScrolledText(root, width=80, height=20)
        self.txt_output.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

            
    def count_logs(self):
        counts = count_log_levels(self.file_path)
        self.txt_output.delete(1.0, tk.END) # brisanje prethodnog sadr
        self.txt_output.insert(tk.END, "Log Level Counts:\n")
        for level, count in counts.items():
            self.txt_output.insert(tk.END, f"{level}: {count}\n")
            
    def extract_errors(self):
        output_path = extract_errors_to_file(self.file_path)
        messagebox.showinfo("Success", "fajlovi upisani u error.txt")
        
    def top_errors(self):

        top = get_top_error_files(self.file_path)
        self.txt_output.delete(1.0, tk.END)
        self.txt_output.insert(tk.END, "Top 5")
        self.txt_output.insert(tk.END,"\n")
        for service, count in top:
            self.txt_output.insert(tk.END, f"{service}: {count} ERRORs\n")
            
    def filter_logs(self):
  
        level = self.entry_level.get().strip() or None
        search_text = self.entry_search.get().strip() or None
        from_date_str = self.entry_from_date.get().strip()
        to_date_str = self.entry_to_date.get().strip()
        
        date_from = None
        date_to = None
        if from_date_str:
            try:
                date_from = datetime.strptime(from_date_str, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("ERROR","nevalidan format")
                return
        if to_date_str:
            try:
                date_to = datetime.strptime(to_date_str, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("ERROR","nevalidan format")
                return
        
        sort = bool(self.sort_var.get())
        filtered = filter_logs(self.file_path, level=level, search_text=search_text, date_from=date_from, date_to=date_to, sort=sort)
        
        self.txt_output.delete(1.0, tk.END)
        self.txt_output.insert(tk.END, "Filtered Logs:\n")
        for log in filtered:
            self.txt_output.insert(tk.END, f"[{log['timestamp']}] {log['level']} {log['service']} {log['message']}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()
