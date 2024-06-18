# YouTube Video Downloader
This Python script downloads YouTube videos using the pytube library. It provides a simple GUI interface for selecting the download directory and downloads the highest resolution video available.

# Features
Downloads YouTube videos in the highest available resolution.
Simple GUI for selecting the download directory using tkinter.
Handles errors gracefully.
# Requirements
- Python 3.x
- pytube
- tkinter (comes pre-installed with Python)
# Installation
1. Install Python: Ensure Python 3.x is installed on your system from python.org.

2. Install pytube:
`pip install pytube`

# Usage
1. Run the Script:

`python youtube_downloader.py`
2. Enter the YouTube URL: The script will prompt you to enter the URL of the YouTube video you wish to download.

3. Select Download Directory: A file dialog will appear asking you to select the directory where you want to save the video.

4. Download: The script will download the video to the selected directory and print a success message.

# Functions
- download_video(url, save_path): Downloads the YouTube video from the provided URL to the specified save path.
- open_file_dialog(): Opens a file dialog for selecting the download directory and returns the selected directory path.
# Main Program Flow
1. Initialize Tkinter: Hides the root Tkinter window.
2. Get YouTube URL: Prompts the user to enter the YouTube video URL.
3. Select Directory: Opens a file dialog for the user to select the download directory.
4. Download Video: Calls the download_video function to download the video to the selected directory.