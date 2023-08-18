import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kontaktbuch")

        self.contacts = []

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.name_label = ttk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(self.frame, text="Telefon:")
        self.phone_label.grid(row=1, column=0, sticky="w")

        self.phone_entry = ttk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(self.frame, text="Hinzufügen", command=self.add_contact)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        self.search_label = ttk.Label(self.frame, text="Suche:")
        self.search_label.grid(row=3, column=0, sticky="w")

        self.search_entry = ttk.Entry(self.frame)
        self.search_entry.grid(row=3, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.frame, text="Suchen", command=self.search_contacts)
        self.search_button.grid(row=4, columnspan=2, pady=10)

        self.contacts_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE)
        self.contacts_listbox.grid(row=5, columnspan=2, padx=5, pady=5, sticky="w"+"e")
        self.contacts_listbox.bind("<<ListboxSelect>>", self.show_contact_details)

        self.details_label = ttk.Label(self.frame, text="Kontaktdetails:")
        self.details_label.grid(row=6, column=0, sticky="w")

        self.details_text = tk.Text(self.frame, height=5, width=30)
        self.details_text.grid(row=7, columnspan=2, padx=5, pady=5, sticky="w"+"e")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact = {"name": name, "phone": phone}
            self.contacts.append(contact)
            self.contacts_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.details_text.delete("1.0", tk.END)
            messagebox.showinfo("Erfolg", "Kontakt hinzugefügt.")
        else:
            messagebox.showerror("Fehler", "Bitte geben Sie Name und Telefonnummer ein.")

    def search_contacts(self):
        query = self.search_entry.get()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query.lower() in contact["name"].lower():
                self.contacts_listbox.insert(tk.END, contact["name"])

    def show_contact_details(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            details = f"Name: {contact['name']}\nTelefon: {contact['phone']}"
            self.details_text.delete("1.0", tk.END)
            self.details_text.insert(tk.END, details)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
