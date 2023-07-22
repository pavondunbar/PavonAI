from flask import Flask, render_template, request
from PIL import Image
import openai

openai.api_key = 'PUT_YOUR_OPEN_AI_API_KEY_HERE'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    prompt = "You: " + user_input + "\nPAVON AI:"
    chatbot_response = create_chatgpt_clone(prompt)
    return chatbot_response

def create_chatgpt_clone(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Uncomment the below if you want to use a development server to test your application.

if __name__ == '__main__':
    app.run()

# Uncomment the below if you want to use Waitress as your production server to test your application..

#if __name__ == '__main__':
    # Run the application using Waitress
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=8000)

# Gunicorn below is the default production server. Simply run `gunicorn app:application` to fire off the Gunicorn prod server.

# Export the Flask application object as 'application'
application = app

