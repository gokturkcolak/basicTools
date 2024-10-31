import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video(video_url, download_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save file with the video title
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {video_url}")
            ydl.download([video_url])  # Download the video
            messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_directory():
    download_path = filedialog.askdirectory()  # Prompt user to select a directory
    directory_label.config(text=download_path)  # Update label with selected directory
    return download_path

def on_download():
    video_url = url_entry.get()  # Get the video URL from the entry box
    download_path = directory_label.cget("text")  # Get the selected download path
    if not download_path:
        messagebox.showwarning("Warning", "Please select a download directory.")
        return
    download_video(video_url, download_path)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL input
tk.Label(root, text="YouTube Video URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Directory selection
tk.Label(root, text="Download Directory:").pack(pady=5)
directory_label = tk.Label(root, text="No directory selected")
directory_label.pack(pady=5)
tk.Button(root, text="Select Directory", command=select_directory).pack(pady=5)

# Download button
tk.Button(root, text="Download", command=on_download).pack(pady=20)

# Start the GUI event loop
root.mainloop()
