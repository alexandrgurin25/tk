import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

left_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
left_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the left listbox
left_scrollbar = tk.Scrollbar(root)
left_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Configure the left listbox to work with the left scrollbar
left_listbox.config(yscrollcommand=left_scrollbar.set)
left_scrollbar.config(command=left_listbox.yview)

# Create a scrollbar for the right listbox
right_scrollbar = tk.Scrollbar(root)
right_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

right_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, yscrollcommand=right_scrollbar.set)
right_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Configure the right listbox to work with the right scrollbar
right_scrollbar.config(command=right_listbox.yview)


# Неупорядоченный список групп
groups = ["KVBO-02", "KVBO-01", "KVBO-03", "KVBO-04", "KVBO-05", "KVBO-06", "KVBO-07", "KVBO-08", "KVBO-09"]

# Функция для сортировки списка групп по номеру
def sort_groups(groups):
    return sorted(groups)

# Упорядочиваем группы
sorted_groups = sort_groups(groups)

# Наполняем левую колонку упорядоченными группами
for group in sorted_groups:
    left_listbox.insert(tk.END, group)

def move_to_right():
    selected = left_listbox.curselection()
    if selected:
        # Получаем индексы всех выделенных элементов
        selected_indices = list(selected)
        # Получаем значения всех выделенных элементов
        selected_values = [left_listbox.get(index) for index in selected_indices]
        for value in selected_values:
            right_listbox.insert(tk.END, value)
        # Удаляем выделенные элементы из левого Listbox в обратном порядке
        for index in reversed(selected_indices):
            left_listbox.delete(index)
        # Сортируем группы в правом Listbox
        sorted_right_groups = sort_groups(right_listbox.get(0, tk.END))
        right_listbox.delete(0, tk.END)
        for item in sorted_right_groups:
            right_listbox.insert(tk.END, item)

def move_to_left():
    selected = right_listbox.curselection()
    if selected:
        # Получаем индексы всех выделенных элементов
        selected_indices = list(selected)
        # Получаем значения всех выделенных элементов
        selected_values = [right_listbox.get(index) for index in selected_indices]
        for value in selected_values:
            left_listbox.insert(tk.END, value)
        # Удаляем выделенные элементы из правого Listbox в обратном порядке
        for index in reversed(selected_indices):
            right_listbox.delete(index)
        # Сортируем группы в левом Listbox
        sorted_left_groups = sort_groups(left_listbox.get(0, tk.END))
        left_listbox.delete(0, tk.END)
        for item in sorted_left_groups:
            left_listbox.insert(tk.END, item)

buttons_frame = tk.Frame(root)

to_right_button = tk.Button(buttons_frame, text="Перенести в правую колонку", command=move_to_right)
to_right_button.pack()

to_left_button = tk.Button(buttons_frame, text="Перенести в левую колонку", command=move_to_left)
to_left_button.pack()

# Размещаем контейнер кнопок по центру
buttons_frame.pack(expand=True)

root.mainloop()