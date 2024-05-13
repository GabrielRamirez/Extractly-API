from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import html2text

app = Flask(__name__)

@app.route('/v1/api/webpage/', methods=['GET'])
def scrape():
    url = request.args.get('url')
    selector = request.args.get('selector')

    if not url:
        return jsonify({"error": "URL query parameter is missing"}), 400 

    if not selector:
        return jsonify({"error": "Selector query parameter is missing"}), 400 

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400

    soup = BeautifulSoup(response.text, 'html.parser')

    if selector.startswith('#'):  # treat as an ID
        content = soup.find(id=selector[1:])  
    elif selector.startswith('.'):  # treat as a class
        content = soup.find(class_=selector[1:])
    else:  # treat as a tag
        content = soup.find(selector)

    if content:
        h = html2text.HTML2Text()
        h.ignore_links = True
        result = {"content": h.handle(str(content))}
    else:
        result = {"error": "No content found with specified selector"}

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)