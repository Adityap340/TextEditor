import tkinter as tk
from tkinter import filedialog
from tkinter import font
import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Text Editor")

        # Create a text widget
        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create a File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create a Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_command(label="Font", command=self.set_font)
        self.format_menu.add_separator()
        self.format_menu.add_command(label="Bold", command=self.set_bold)
        self.format_menu.add_command(label="Italic", command=self.set_italic)
        self.format_menu.add_separator()
        self.format_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        self.format_menu.add_command(label="Decrease Font Size", command=self.decrease_font_size)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        # Initialize the current font
        self.current_font = font.Font(family="Arial", size=12, weight="normal", slant="roman")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)

    def set_font(self):
        font_dialog = font.FontDialog(self.root)
        new_font = font_dialog.show()
        if new_font:
            self.current_font = new_font
            self.text_widget.configure(font=new_font)

    def set_bold(self):
        bold = "bold" if self.current_font.actual()["weight"] != "bold" else "normal"
        self.current_font.configure(weight=bold)
        self.text_widget.configure(font=self.current_font)

    def set_italic(self):
        italic = "italic" if self.current_font.actual()["slant"] != "italic" else "roman"
        self.current_font.configure(slant=italic)
        self.text_widget.configure(font=self.current_font)

    def increase_font_size(self):
        size = self.current_font.actual()["size"]
        new_size = size + 2
        self.current_font.configure(size=new_size)
        self.text_widget.configure(font=self.current_font)

    def decrease_font_size(self):
        size = self.current_font.actual()["size"]
        new_size = max(size - 2, 8)  # Ensure minimum font size of 8
        self.current_font.configure(size=new_size)
        self.text_widget.configure(font=self.current_font)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("wordnet")

    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
