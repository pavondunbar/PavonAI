import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import openai

openai.api_key = 'PUT_YOUR_OPEN_AI_API_KEY_HERE'

def create_chatgpt_clone(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def process_user_input():
    user_input = user_entry.get()
    chatbox.configure(state=tk.NORMAL)
    chatbox.insert(tk.END, "YOU: " + user_input + "\n\n")  # Add an empty line after user input
    chatbox.configure(state=tk.DISABLED)

    prompt = "You: " + user_input + "\nPAVON AI:"
    chatbot_response = create_chatgpt_clone(prompt)

    chatbox.configure(state=tk.NORMAL)
    chatbox.insert(tk.END, "PAVON AI: " + chatbot_response + "\n\n")  # Add an empty line after chatbot response
    chatbox.configure(state=tk.DISABLED)

    user_entry.delete(0, tk.END)

def clear_output():
    chatbox.configure(state=tk.NORMAL)
    chatbox.delete(1.0, tk.END)
    chatbox.configure(state=tk.DISABLED)

def set_default_text(event):
    user_entry.delete(0, tk.END)
    user_entry.unbind('<Button-1>')

def handle_user_input(event):
    process_user_input()

# Create GUI window
window = tk.Tk()
window.title("Welcome to Pavon AI!")
window.geometry("500x500")

# Set background color
window.configure(bg="#0000FF")

# Add logo image
logo_image = Image.open("pavon.png")  # Replace with your logo image file
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(window, image=logo_photo, bg="#0000FF")
logo_label.grid(row=0, column=0, columnspan=2, pady=5)

# Create chatbox
chatbox = scrolledtext.ScrolledText(window, height=15, width=70, wrap=tk.WORD)  # Set wrap option to tk.WORD
chatbox.configure(state=tk.DISABLED)
chatbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Create user input entry
user_entry = tk.Entry(window, width=70)
user_entry.grid(row=2, column=0, padx=5, pady=5, sticky="w")
user_entry.insert(0, "Type your question here")
user_entry.bind('<Button-1>', set_default_text)
user_entry.bind('<Return>', handle_user_input)  # Bind the Return key event to handle_user_input function

# Create send button
send_button = tk.Button(window, text="Send", command=process_user_input, bg="#0000FF", fg="black")
send_button.grid(row=3, column=0, padx=5, pady=5, sticky="e")

# Create clear button
clear_button = tk.Button(window, text="Clear", command=clear_output, bg="#0000FF", fg="black")
clear_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Configure grid weights
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the GUI main loop
window.mainloop()

