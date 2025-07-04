from flask import Flask, request, jsonify
import threading
import main  # This imports your main.py

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    youtube_url = data.get('youtube_url')
    row_id = data.get('row_id')
    if not youtube_url:
        return jsonify({'error': 'No YouTube URL provided'}), 400

    def run_workflow():
        main.run_for_url(youtube_url, row_id=row_id)

    threading.Thread(target=run_workflow).start()
    return jsonify({'status': 'Processing started'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 