#import the flask, Google's GenAI SDK package, Python Imaging Library and Python's default tool for safe url formating
from flask import Flask, render_template, request, jsonify
from google import genai
from PIL import Image
import urllib.parse #ensuring emojis other non-english characters are safe in the url

app = Flask(__name__)

client = genai.Client()

#if on homepage route, just render the index.html template
@app.route('/')
def index():
    return render_template("index.html")

#if on the ./process-frame route which is called upon from the script in index.html, turn the image to be searchable on RoyaleAPI
@app.route('/process-frame', methods=['POST'])
def process_frame():
    #in case there is no image sent
    if 'image' not in request.files:
        return jsonify({'error': 'No Image data received'}), 400
    file = request.files['image']

    #open image, generate response using the image and prompt, then search it on RoyaleAPI
    try:
        #open image using method from pillow library
        image = Image.open(file.stream)

        #generate response with gemini 3.1 flash-lite given image and prompt
        response = client.models.generate_content(
           model='gemini-3.1-flash-lite',
           contents=[
               image,
               "Return only the opponent's username from this Clash Royale screenshot (the text just above the clan name), with no other text or formatting. Do not use special characters to substitude actual characters. For example, don't use м to replace M. Never use м"
           ]
        )

        #strip filler from response
        player_query = response.text.strip().strip('"\'`')

        #print to terminal of what the extracted text is
        print(f"Gemini Extracted Text\n{player_query}")

        #checks whether there was a response from gemini and if not, returns json file to the Javascript part of index.html
        if not player_query:
            return jsonify({'error': 'Could not extract player name'}), 400
        
        #ensures proper formating when searching up special characters so that it's url friendly
        encoded_query = urllib.parse.quote(player_query)

        #url link for player search
        redirect_url = f"https://royaleapi.com/player/search/results?q={encoded_query}"

        #gives scrip the URL
        return jsonify({'redirect_url': redirect_url})
    #if any error occurs, it is printed in terminal and notified to user
    except Exception as e:
        #prints the error to terminal
        print(f"Error: {e}")

        #Alerts the user as well
        return jsonify({'error': str(e)}), 500

#fire up web server if this script is running
if __name__ == '__main__':
    app.run(debug=True) #ensure I can reload if I make changes and see detailed errors if they occur