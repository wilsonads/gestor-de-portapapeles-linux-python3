import tkinter as tk
import tkinter.messagebox as messagebox
import pickle

# Función para copiar el contenido de un botón al portapapeles
def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

# Función para eliminar un botón existente
def delete_button(button, text):
    button.destroy()
    buttons.remove(text)
    with open('buttons.pickle', 'wb') as file:
        pickle.dump(buttons, file)

# Función para crear un nuevo botón personalizado
def create_custom_button():
    text = entry.get()
    if text:
        button_frame = tk.Frame(frame, bg='black')
        button_frame.pack()

        button = tk.Button(button_frame, text=text, command=lambda t=text: copy_to_clipboard(t), bg='green', fg='white', bd=1)
        button.pack(side=tk.LEFT)

        delete_button_button = tk.Button(button_frame, text='X', command=lambda b=button, t=text: delete_button(b, t), bg='red', fg='white', bd=1, width=2)
        delete_button_button.pack(side=tk.LEFT)

        entry.delete(0, tk.END)

        # Guardar el contenido del botón en el archivo
        buttons.append(text)
        with open('buttons.pickle', 'wb') as file:
            pickle.dump(buttons, file)
    else:
        messagebox.showwarning('Advertencia', 'Por favor, ingresa un texto válido')

# Crear la ventana principal
root = tk.Tk()
root.title('Gestor de Portapapeles')
root.configure(bg='black')

# Crear el marco principal
frame = tk.Frame(root, bg='black')
frame.pack(padx=10, pady=10)

# Crear un campo de texto para ingresar texto personalizado
entry = tk.Entry(frame, width=30, fg='white', bg='black', bd=1)
entry.pack(pady=10)

# Crear un botón para crear botones personalizados
create_button = tk.Button(frame, text='Crear Botón', command=create_custom_button, bg='black', fg='white', bd=1)
create_button.pack(pady=5)

# Cargar los botones desde el archivo
try:
    with open('buttons.pickle', 'rb') as file:
        buttons = pickle.load(file)
except FileNotFoundError:
    buttons = []

# Crear los botones guardados anteriormente
button_frames = []  # Lista para almacenar los marcos de los botones
for text in buttons:
    button_frame = tk.Frame(frame, bg='black')
    button_frame.pack()

    button = tk.Button(button_frame, text=text, command=lambda t=text: copy_to_clipboard(t), bg='green', fg='white', bd=1)
    button.pack(side=tk.LEFT)

    delete_button_button = tk.Button(button_frame, text='X', command=lambda b=button_frame, t=text: delete_button(b, t), bg='red', fg='white', bd=1, width=2)
    delete_button_button.pack(side=tk.LEFT)

    button_frames.append(button_frame)  # Agregar el marco a la lista

# Ejecutar la aplicación
root.mainloop()
