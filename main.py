import tkinter as tk
import eng_to_ipa as ipa

def convert_to_ipa():
    paragraph = input_text.get("1.0", "end-1c")
    ipa_paragraph = ipa.convert(paragraph)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", ipa_paragraph)

window = tk.Tk()
window.title("Paragraph to IPA Converter")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

input_text = tk.Text(window, height=10, width=50, font=("Courier", 16))
input_text.pack(fill=tk.BOTH, expand=True)
input_text.pack_propagate(False)

convert_button = tk.Button(window, text="Convert", command=convert_to_ipa)
convert_button.pack(pady=10)
convert_button.pack_propagate(False)

output_text = tk.Text(window, height=10, width=50, font=("Courier", 16))
output_text.pack(fill=tk.BOTH, expand=True)
output_text.pack_propagate(False)

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"+{x}+{y}")

window.mainloop()