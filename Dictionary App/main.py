import tkinter as tk

from dictionary_app import DictionaryApp

def main():
    root = tk.Tk()
    app = DictionaryApp(root, "dictionary_data.json")
    app.load_all_words()
    root.mainloop()

if __name__ == "__main__":
    main()
