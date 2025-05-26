#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from datetime import timedelta
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_btn = tk.Button(master, text="Start", command=self.start)
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = tk.Button(master, text="Stop", command=self.stop)
        self.stop_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(master, text="Reset", command=self.reset)
        self.reset_btn.pack(side="left", padx=10)

        self.update_display()

    def update_display(self):
        if self.running:
            now = time.time()
            self.elapsed_time = now - self.start_time
        formatted = str(timedelta(seconds=int(self.elapsed_time)))
        self.label.config(text=formatted)
        self.master.after(500, self.update_display)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()


# In[ ]:




