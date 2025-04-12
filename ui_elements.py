import tkinter as tk
from tkinter import ttk

def create_text_area(frame):
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    text_area = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)
    scrollbar.grid(row=1, column=1, sticky="ns", pady=5)
    text_area.grid(row=1, column=0, pady=5, sticky="nsew")
    return text_area

def create_combo(frame, values):
    combo = ttk.Combobox(frame, values=values, state="readonly", width = 20)
    combo.grid(row=0, column=0, pady=5, sticky="ew")
    return combo