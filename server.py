from flask import Flask, request, jsonify
import json

app = Flask(__name__)

FILE_PATH = "game.json"

@app.route('/')
def index():
    return "Welcome to Game"

# POST API for saving level
@app.route('/save_level', methods=['POST'])
def save_level():
    content = request.json

    print(content)

    data = {}


    try:
        f = open(FILE_PATH)
        
        data = json.load(f)
        f.close()
    except IOError:
        print("File not accessible")

    f = open(FILE_PATH, 'w')

    print("Before")
    print(data)
    user_id = str(content["user_id"])
    data[user_id] = content
    print("After")
    print(data)


    json.dump(data, f)
    f.close()
        

    return jsonify({'status': 'success'})

@app.route('/display_players', methods=['GET']) 
def display_players():
    data = {}
    try:
        f = open(FILE_PATH)
        data = json.load(f)
        f.close()
    except IOError:
        print("File not accessible")

    html = ""
    for user_id in data:
        user = data[user_id]        
        html += f"ID: {user['user_id']}: Level: {user['level']}: Score: {user['score']}<br>"

    return html

if __name__ == '__main__':
    app.run()

    