import tkinter as tk
from tkinter import messagebox
import requests

class EmergencyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Emergency Response System")
        self.window.geometry("400x300")

        self.label = tk.Label(self.window, text="Enter emergency text:")
        self.label.pack(pady=10)

        self.text_input = tk.Entry(self.window, width=50)
        self.text_input.pack(pady=5)

        self.analyze_button = tk.Button(self.window, text="Analyze", command=self.analyze_text)
        self.analyze_button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="", wraplength=350)
        self.result_label.pack(pady=10)

    def analyze_text(self):
        text = self.text_input.get()
        if not text:
            messagebox.showerror("Error", "Text cannot be empty")
            return

        try:
            response = requests.post("http://localhost:5000/analyze", json={"text": text})
            if response.status_code == 200:
                result = response.json()["analysis"][0]
                self.result_label.config(text=f"{result['label']} ({result['score']:.2f})")
            else:
                self.result_label.config(text="Error analyzing text.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()
