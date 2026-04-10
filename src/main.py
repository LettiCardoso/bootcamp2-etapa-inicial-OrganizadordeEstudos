import tkinter as tk
from tkinter import messagebox
from logic import SessaoDeEstudo

class FocusFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FocusFlow - Organizador de Estudos v1.0.0")
        self.root.geometry("400x300")
        
        self.timer_running = False
        self.seconds_left = 0

        # UI Elements
        tk.Label(root, text="O que vamos estudar agora?", font=("Arial", 12)).pack(pady=10)
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack()

        tk.Label(root, text="Duração (minutos):").pack(pady=5)
        self.entry_time = tk.Entry(root, width=10)
        self.entry_time.insert(0, "25")
        self.entry_time.pack()

        self.label_timer = tk.Label(root, text="00:00", font=("Arial", 30, "bold"))
        self.label_timer.pack(pady=20)

        self.btn_start = tk.Button(root, text="Iniciar Foco", command=self.start_timer, bg="green", fg="white")
        self.btn_start.pack()

    def update_timer(self):
        if self.timer_running and self.seconds_left > 0:
            mins, secs = divmod(self.seconds_left, 60)
            self.label_timer.config(text=f"{mins:02d}:{secs:02d}")
            self.seconds_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.seconds_left == 0:
            self.timer_running = False
            messagebox.showinfo("Parabéns!", "Ciclo de estudos finalizado! Hora de uma pausa.")
            self.label_timer.config(text="00:00")

    def start_timer(self):
        try:
            task = self.entry_task.get()
            minutes = int(self.entry_time.get())
            session = SessaoDeEstudo(task, minutes)
            
            self.seconds_left = session.duracao_minutos
            self.timer_running = True
            self.btn_start.config(state="disabled")
            self.update_timer()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusFlowApp(root)
    root.mainloop()