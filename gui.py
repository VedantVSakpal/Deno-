import tkinter as tk
from chatbot import DenoBot


class DenoGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Deno Assistant")
        self.root.geometry("700x500")
        self.bot = DenoBot()

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Deno College Assistant", font=("Arial", 18, "bold"))
        title.pack(pady=(15, 10))

        self.chat_box = tk.Text(self.root, wrap="word", state="disabled", height=20)
        self.chat_box.pack(padx=15, pady=5, fill="both", expand=True)

        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=15, pady=(5, 15))

        self.entry = tk.Entry(input_frame, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side="right", padx=(8, 0))

    def append_message(self, sender: str, message: str) -> None:
        self.chat_box.configure(state="normal")
        self.chat_box.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see(tk.END)

    def send_message(self, event=None) -> None:
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.entry.delete(0, tk.END)
        self.append_message("You", user_input)
        response = self.bot.respond(user_input)
        self.append_message(self.bot.name, response)


def run_text_mode() -> None:
    bot = DenoBot()
    print("Tkinter GUI is not available in this environment. Running in text mode instead.")
    print(f"{bot.name} Assistant is ready. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        print(f"{bot.name}: {bot.respond(user_input)}")


def main() -> None:
    try:
        root = tk.Tk()
    except tk.TclError:
        run_text_mode()
        return

    app = DenoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
