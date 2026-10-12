# What it does + Problem it solves:
This is a tool that can be used in Clash Royale to scan an opponent's name to find them on RoyaleAPI.

This is better than searching the name because it can process faster than typing (takes 2-3 seconds) and can type any emoji / international language symbols.

# How it works:
You take a picture of the opponent's name on your computer's webcam.

It then creates a PNG image of the opponent's name and sends it to Gemini 3.1-flash-lite OCR with a prompt to extract the name from the image.

It then redirects you to the RoyaleAPI search bar of the opponent where you can find the opponent and then look at their battle log to see their previous decks used.

# Structure of Program

HTML + CSS + Javascript Frontend

Python Backend

Flask Framework


# Prerequisites
> python 3.10+ installed

> modern web browser with webcam permissions available

> Google Gemini API Key


# How to set it up for use
Clone the repo
> git clone https://github.com/jack3051/Clash-Opponent-Finder.git

> cd Clash-Opponent-Finder

Setup virtual environment to isolate environment
> python3 -m venv .venv

Mac
> source .venv/bin/activate

Windows
>.venv\Scripts\activate

Install Flask framework and genai SDK package
> pip install flask google-genai

Export your Gemini API Key
> export GEMINI_API_KEY="your_api_key_here"

Run the program
> flask run



# How I used it:
I used it on the ranked game mode in Clash Royale to achieve a top #510 rank global. It has been a useful tool to quickly check the opponent's deck which has led me to beat matchups and make plays that I wouldn't have before, especially in single elixir. Across 10 trials I've tested, 7 of them were highly useful (was successful in finding the deck they played) and the 3 weren't only because it was a common name (Arthur, Christopher, King) so there were too many results. The range of which it take to search up the name on RoyaleAPI was from 2-3 seconds.

<img width="414" height="896" alt="IMG_3926" src="https://github.com/user-attachments/assets/b5e77227-9050-4aa5-b44b-306ee13b3091" />

## Additional notes
I have used a bunch of comments because this I personally felt that writing all of these comments helped with my understanding of the program. This is my first iteration of the project and will hopefully be improving the project going forward and this is also my CS50 week 10 project.
