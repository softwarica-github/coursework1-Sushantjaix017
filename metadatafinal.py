import tkinter as tk
from tkinter import filedialog
import subprocess
import threading
import unittest

def extract_metadata(file_path):
    metadata_output = subprocess.check_output(["mdls", file_path])
    metadata_output = metadata_output.decode("utf-8")
    return metadata_output

def extract_metadata_from_entry():
    file_path = entry.get()
    if file_path:
        metadata = extract_metadata(file_path)
        display_metadata(metadata)

def display_metadata(metadata):
    result_window = tk.Toplevel()
    result_window.title("Metadata Result")
    result_window.configure(bg="black")  # Set background color to black
    # Create a label as the heading in red color
    heading_label = tk.Label(result_window, text="Metadata Result", fg="red", font=("Arial", 14, "bold"))
    heading_label.pack(pady=10)

    result_text = tk.Text(result_window, bg="black", fg="light green")  # Set text color to light green
    result_text.insert(tk.END, metadata)
    result_text.pack()

def run_unit_tests():
    unittest.main(exit=False)

def browse_file():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, file_path)  # Insert the selected file path into the entry field

def main():
    global entry  # Declare entry as a global variable
    root = tk.Tk()
    root.title("Metadata Extraction Tool")
    root.geometry("500x250")  # Set window size
    root.configure(bg="indigo")  # Set background color to grey

    # Create label for entering the file path
    path_label = tk.Label(root, text="Enter the path of the file:", fg="red")
    path_label.grid(row=0, column=0, padx=(140, 10), pady=(20, 5))  # Added padx to shift the label to the left

    # Create entry field for file path with dark border
    entry = tk.Entry(root, bd=2, relief=tk.SOLID, width=40)
    entry.grid(row=1, column=0, columnspan=3, padx=20)

    # Create browse button
    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.grid(row=1, column=3)

    # Create button to trigger metadata extraction
    extract_button = tk.Button(root, text="Extract Metadata", command=extract_metadata_from_entry)
    extract_button.grid(row=2, column=0, columnspan=4, pady=10)

    root.mainloop()

# Run unit tests first
run_unit_tests()
# Start the GUI after unit tests are completed
main()


