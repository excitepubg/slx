from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__)

BOT_TOKEN = "8330506188:AAFo8DWbo1X1mFZUuDQfpQBdsnKz6fUloeo"
CHAT_ID = "8197301287"

@app.route('/')
def index():
    # HTML faylni to'g'ridan-to'g'ri yuboradi
    return send_file('index.html')  # index.html shu yerda, app.py bilan bir joyda bo'lishi kerak

@app.route('/send', methods=['POST'])
def send_message():
    try:
        name = request.form.get('name', 'No name')
        message = request.form.get('message', 'No message')
        text = f"🧾 hazl:\n👤 habar: {name}\n nma gap ako hazl bu yerda: {message}"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})

        if response.status_code == 200:
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error", "message": "Telegram API error"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
