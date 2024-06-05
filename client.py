import tkinter as tk
import socket
import threading

def send_to_socket(message):
    if message:
        server_socket.send(message.encode())
        message_entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = server_socket.recv(1024).decode()
            if message:
                message_list.insert(tk.END, message)
        except ConnectionAbortedError:
            break

def send_message():
    message = message_entry.get()

    nickname = nickname_entry.get()

    formatted_message = f"{nickname}: {message}"

    send_to_socket(formatted_message)

root = tk.Tk()
root.title("Chat 37KI")

message_list = tk.Listbox(root, width=50, height=20)
message_list.pack(padx=10, pady=10)

nickname_entry = tk.Entry(root, width=50)
nickname_entry.pack(padx=10, pady=5)
nickname_entry.insert(0, "Enter your nickname")

message_entry = tk.Entry(root, width=50)
message_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Надіслати", command=send_message)
send_button.pack(padx=10, pady=5)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('151.115.78.136', 9999))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
