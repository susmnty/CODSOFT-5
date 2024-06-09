import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone and email and address:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        list_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields given")

def list_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected_contact = listbox_contacts.curselection()
    if selected_contact:
        index = selected_contact[0]
        contacts[index] = {
            'name': entry_name.get(),
            'phone': entry_phone.get(),
            'email': entry_email.get(),
            'address': entry_address.get()
        }
        list_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update")

def delete_contact():
    selected_contact = listbox_contacts.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        list_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Information Manager")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

frame_middle = tk.Frame(root)
frame_middle.pack(pady=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

label_name = tk.Label(frame_top, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame_top)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(frame_top, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(frame_top)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame_top, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(frame_top)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_address = tk.Label(frame_top, text="Address:")
label_address.grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(frame_top)
entry_address.grid(row=3, column=1, padx=10, pady=5)

btn_add = tk.Button(frame_top, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0, padx=10, pady=5)

btn_update = tk.Button(frame_top, text="Update Contact", command=update_contact)
btn_update.grid(row=4, column=1, padx=10, pady=5)

btn_delete = tk.Button(frame_top, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=5, column=0, padx=10, pady=5)

label_search = tk.Label(frame_middle, text="Search:")
label_search.pack(side=tk.LEFT, padx=10, pady=5)
entry_search = tk.Entry(frame_middle)
entry_search.pack(side=tk.LEFT, padx=10, pady=5)
btn_search = tk.Button(frame_middle, text="Search Contact", command=search_contact)
btn_search.pack(side=tk.LEFT, padx=10, pady=5)

listbox_contacts = tk.Listbox(frame_bottom, width=50, height=10)
listbox_contacts.pack(pady=10)

root.mainloop()