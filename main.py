import subprocess
import sys
import re

def is_package_installed(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package], stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def is_ffmpeg_installed():
    try:
        result = subprocess.check_output(["ffmpeg", "-version"], stderr=subprocess.STDOUT).decode()
        return 'ffmpeg version' in result
    except Exception:
        pass
        # return False

def download_youtube_video(url):
    command = f"youtube-dl -f 'bestvideo+bestaudio/best' {url}"
    subprocess.run(command, shell=True)

# Check for python3-pip
if not is_package_installed('pip'):
    print("pip is not installed. Please install python3-pip.")
    sys.exit(1)

# Check and install youtube-dl
if not is_package_installed('youtube_dl'):
    print("youtube-dl is not installed. Installing...")
    install_package('youtube-dl')

# Check for ffmpeg
if not is_ffmpeg_installed():
    print("ffmpeg is not installed or not properly configured with all addons.")
    sys.exit(1)

# Ask for YouTube link and download video
youtube_link = input("Enter the YouTube link to download: ")
download_youtube_video(youtube_link)
