from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def load_html():
    html_url = request.args.get('url')
    if not html_url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(html_url)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 400

    return response.text, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)
