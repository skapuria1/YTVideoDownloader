from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    """
    Downloads a YouTube video.

    Args:
        url (str): The URL of the YouTube video.
        save_path (str): The directory where the video will be saved.
    """
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension = "mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Downloaded Video Successfully!")
    except Exception as e:
        print(e)
    

def open_file_dialog():
    """
    Opens a file dialog for selecting a directory.

    Returns:
        str: The path of the selected directory.
    """
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder



if __name__ == "__main__":
    root = tk.Tk() #instantiates TK module
    root.withdraw() #hides window

    video_url = input("Please enter the Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print ("Invalid file location")
    else:
        download_video(video_url,save_dir)
        print("Downloaded Successfully!")