import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from linked_list import LinkedList

class DictionaryApp:
    def __init__(self, master, file_name):
        self.master = master
        self.master.title("Dictionary App")

        self.file_name = file_name
        self.dictionary_list = LinkedList(self.load_dictionary())

        self.master.geometry("500x340")

        # GUI components
        self.label = tk.Label(master, text="Dictionary App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_word_button = tk.Button(master, text="เพิ่มคำศัพท์", command=self.show_add_word_window)
        self.add_word_button.pack()

        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.pack(pady=10)

        self.load_all_words()
        self.listbox.bind('<<ListboxSelect>>', self.listbox_selection)

        self.search_entry = ttk.Combobox(master, width=30)
        self.search_entry.set("ป้อนคำศัพท์ที่ต้องการค้นหา")
        self.search_entry['values'] = self.get_word_suggestions()
        self.search_entry.pack(pady=10)

        self.search_entry.bind('<FocusOut>', self.restore_default_text)
        self.search_entry.bind('<FocusIn>', self.clear_search_entry)
        self.search_entry.bind('<FocusIn>', self.clear_search_entry)

        self.search_button = tk.Button(master, text="ค้นหา", command=self.show_word_details)
        self.search_button.pack()

    def clear_search_entry(self, event):
        if self.search_entry.get() == "ป้อนคำศัพท์ที่ต้องการค้นหา":
            self.search_entry.delete(0, tk.END)

    def restore_default_text(self, event):
        if not self.search_entry.get():
            self.search_entry.set("ป้อนคำศัพท์ที่ต้องการค้นหา")
            self.search_entry.bind('<FocusIn>', self.clear_search_entry)

    def show_add_word_window(self):
        add_word_window = tk.Toplevel(self.master)
        add_word_window.title("เพิ่มคำศัพท์")
        add_word_window.geometry("300x240")

        english_label = tk.Label(add_word_window, text="คำศัพท์ (ภาษาอังกฤษ):")
        english_label.pack(pady=5)

        english_entry = tk.Entry(add_word_window, width=30)
        english_entry.pack(pady=5)

        thai_label = tk.Label(add_word_window, text="คำแปล (ภาษาไทย):")
        thai_label.pack(pady=5)

        thai_entry = tk.Entry(add_word_window, width=30)
        thai_entry.pack(pady=5)

        type_label = tk.Label(add_word_window, text="ชนิดของคำ:")
        type_label.pack(pady=5)

        type_entry = tk.Entry(add_word_window, width=30)
        type_entry.pack(pady=5)

        add_button = tk.Button(add_word_window, text="เพิ่ม", command=lambda: self.add_word_from_entry(
            english_entry.get(), thai_entry.get(), type_entry.get(), add_word_window))
        add_button.pack(pady=10)

    def add_word_from_entry(self, english, thai, word_type, window):
        self.add_word(english, thai, word_type)
        window.destroy()

    def add_word(self, english, thai, word_type):
        word = {"english": english, "thai": thai, "type": word_type}
        self.dictionary_list.append_and_sort(word)
        self.save_dictionary()
        self.load_all_words()

    def show_word_details(self):
        search_term = self.search_entry.get().lower()

        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_word = self.dictionary_list.to_list()[selected_index]
            self.display_word_details(selected_word)
        else:
            result = self.find_word(search_term)
            if result:
                self.display_word_details(result)
            else:
                messagebox.showinfo("ไม่พบคำศัพท์", "ไม่มีคำศัพท์ที่ค้นหา")

    def display_word_details(self, word):
        search_term = self.search_entry.get().lower()

        if hasattr(self, 'details_window') and self.details_window.winfo_exists():
            details_window = self.details_window
            details_window.title("Word Details")
            details_window.geometry("220x120")
        else:
            details_window = tk.Toplevel(self.master)
            details_window.title("Word Details")
            details_window.geometry("220x120")
            self.details_window = details_window

        for widget in details_window.winfo_children():
            widget.destroy()

        label = tk.Label(details_window,
                         text=f"คำศัพท์: {word['english']}\nความหมาย: {word['thai']} ({word['type']})")
        label.pack(pady=10)

        prev_button = tk.Button(details_window, text="ก่อนหน้า",
                                command=lambda: self.show_adjacent_word(word, direction="prev"))
        prev_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(details_window, text="แก้ไข", command=lambda: self.show_edit_word_window(word))
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(details_window, text="ลบคำศัพท์", command=lambda: self.delete_word(word))
        delete_button.pack(side=tk.LEFT, padx=5)

        next_button = tk.Button(details_window, text="ถัดไป",
                                command=lambda: self.show_adjacent_word(word, direction="next"))
        next_button.pack(side=tk.LEFT, padx=5)

    def listbox_selection(self, event):
        if self.listbox.curselection():
            selected_index = self.listbox.curselection()[0]
            selected_word = self.dictionary_list.to_list()[selected_index]
            self.display_word_details(selected_word)

    def find_word(self, term):
        for word in self.dictionary_list.to_list():
            if term == word['english'].lower() or term == word['thai'].lower():
                return word
        return None

    def load_dictionary(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_dictionary(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.dictionary_list.to_list(), file, ensure_ascii=False, indent=2)

    def load_all_words(self):
        # ลบทุกคอมโพเนนต์ที่มีอยู่ใน Listbox
        self.listbox.delete(0, tk.END)

        # เพิ่มคำศัพท์ใหม่ลงใน Listbox
        for word in self.dictionary_list.to_list():
            self.listbox.insert(tk.END, f"{word['english']}")

        self.dictionary_list.sort()

    def show_adjacent_word(self, current_word, direction):
        current_index = self.dictionary_list.to_list().index(current_word)

        if direction == "prev" and current_index > 0:
            new_index = current_index - 1
        elif direction == "next" and current_index < len(self.dictionary_list.to_list()) - 1:
            new_index = current_index + 1
        else:
            return

        new_word = self.dictionary_list.to_list()[new_index]
        self.display_word_details(new_word)

    def show_edit_word_window(self, word):
        edit_word_window = tk.Toplevel(self.details_window)
        edit_word_window.title("แก้ไขคำศัพท์")
        edit_word_window.geometry("300x250")

        english_label = tk.Label(edit_word_window, text="คำศัพท์ (ภาษาอังกฤษ):")
        english_label.pack(pady=5)

        english_entry = tk.Entry(edit_word_window, width=30)
        english_entry.insert(0, word['english'])
        english_entry.pack(pady=5)

        thai_label = tk.Label(edit_word_window, text="คำแปล (ภาษาไทย):")
        thai_label.pack(pady=5)

        thai_entry = tk.Entry(edit_word_window, width=30)
        thai_entry.insert(0, word['thai'])
        thai_entry.pack(pady=5)

        type_label = tk.Label(edit_word_window, text="ชนิดของคำ:")
        type_label.pack(pady=5)

        type_entry = tk.Entry(edit_word_window, width=30)
        type_entry.insert(0, word['type'])
        type_entry.pack(pady=5)

        save_button = tk.Button(edit_word_window, text="บันทึก", command=lambda: self.save_edited_word(
            word, english_entry.get(), thai_entry.get(), type_entry.get(), edit_word_window))
        save_button.pack(pady=10)

    def save_edited_word(self, original_word, new_english, new_thai, new_type, edit_window):

        original_word['english'] = new_english
        original_word['thai'] = new_thai
        original_word['type'] = new_type

        self.save_dictionary()
        edit_window.destroy()
        self.display_word_details(original_word)

        messagebox.showinfo("แก้ไขคำศัพท์สำเร็จ", f"คำศัพท์ '{new_english}' ถูกแก้ไขแล้ว")

        self.load_all_words()
        self.listbox_sort()
        self.details_window.lift()

    def listbox_sort(self):
        # เรียกใช้ sort ของ Listbox
        items = self.listbox.get(0, tk.END)
        items = sorted(items, key=lambda x: x.lower())
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)

    def delete_word(self, word):
        confirmation = messagebox.askyesno("ยืนยันการลบ", f"คุณต้องการลบคำศัพท์ '{word['english']}' ใช่หรือไม่?")
        if confirmation:
            self.dictionary_list.remove(word)
            self.save_dictionary()
            self.details_window.destroy()
            messagebox.showinfo("ลบคำศัพท์สำเร็จ", f"คำศัพท์ '{word['english']}' ถูกลบแล้ว")
            self.update_listbox_after_delete()

    def update_listbox_after_delete(self):
        self.listbox.delete(0, tk.END)
        for word in self.dictionary_list.to_list():
            self.listbox.insert(tk.END, f"{word['english']}")

    def show_suggestions(self, event):
        search_term = self.search_entry.get().lower()
        suggestions = [word['english'] for word in self.dictionary_list.to_list()
                       if word['english'].lower().startswith(search_term)]
        self.search_entry['values'] = suggestions

    def get_word_suggestions(self):
        return [word['english'] for word in self.dictionary_list.to_list()]