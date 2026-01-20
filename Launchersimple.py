import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import subprocess

class SimpleLauncher:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game Launcher")
        self.window.geometry("600x400")

        self.games_file = "games_simple.json"
        self.games = []

        self.load_games()

        self.create_ui()

    def create_ui(self):
            title = tk.Label(
                self.window,
                text="МОЇ ІГРИ",
                font=("Arial", 20, "bold")
            )
            title.pack(pady=10)

            add_btn = tk.Button(
                self.window,
                text="add game",
                command=self.add_game,
                font=("Arial", 12),
                bg="#4CAF50",
                fg="white",
                width=15
            )
            add_btn.pack(pady=10)
            
            frame = tk.Frame(self.window)
            frame.pack(fill="both", expand=True, padx=20, pady=10)
        
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            self.listbox = tk.Listbox(
                frame,
                font=("Arial", 12),
                yscrollcommand=scrollbar.set,
                height=10
            )
            self.listbox.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=self.listbox.yview)

            buttons_frame = tk.Frame(self.window)
            buttons_frame.pack(pady=10)

            play_btn = tk.Button(
                buttons_frame,
                text="play",
                command=self.play_game,
                font=("Arial", 12),
                bg="#2196F3",
                fg="white",
                width=10
            )
            play_btn.pack(side="left", padx=5)

            delete_btn = tk.Button(
                buttons_frame,
                text="delete",
                command=self.delete_game,
                font=("Arial", 12),
                bg="#f44336",
                fg="white",
                width=10
            )
            delete_btn.pack(side="left", padx=5)

            self.update_list()
    def update_list(self):
        self.listbox.delete(0, tk.END)
        for game in self.games:
            self.listbox.insert(tk.END, game['name'])

    def add_game(self):
        file_path = filedialog.askopenfilename(
            title="select game",
            filetypes=[("Programs", "*.exe"), ("All files", "*.*")]
        )

        if file_path:
            name = os.path.basename(file_path)

            new_game = {
                'name': name,
                'path': file_path
            }
            self.games.append(new_game)

            self.save_games()
            self.update_list()

            messagebox.showinfo("success", f"added: {name}")

    def play_game(self):
        selection = self.listbox.curselection()

        if not selection:
            messagebox.showwarning("Warning", "Select game!")
            return
        
        index = selection[0]
        game = self.games[index]

        try:
            subprocess.Popen([game['path']])
            messagebox.showinfo("Launching", f"lanched: {game['name']}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to Launch: \n{e}")

    def delete_game(self):
        selection = self.listbox.curselection()

        if not selection:
            messagebox.showwarning("Warning!", "Select game!")
            return
        index = selection[0]
        game = self.games[index]

        if messagebox.askyesno("Delete", f"delete: {game['name']}?"):
            self.games.pop(index)
            self.save_games()
            self.update_list()

    def save_games(self):
        with open(self.games_file, 'w', encoding='utf-8') as f:
            json.dump(self.games, f, ensure_ascii=False, indent=4)

    def load_games(self):
        if os.path.exists(self.games_file):
            with open(self.games_file, 'r', encoding='utf-8') as f:
                self.games = json.load(f)
        else:
            self.games = []
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SimpleLauncher()
    app.run()