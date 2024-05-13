# Import the necessary libraries
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import html2text

# Create a Flask web server
app = Flask(__name__)

# Define the only route for this API
@app.route('/v1/url', methods=['GET'])
def scrape():
    # Get the URL from the request arguments
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "URL query parameter is missing"}), 400 

    # Make a request to the provided URL
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400  # Return the error message and a bad request status

    # Parse the response text with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # List the tags you want to check for main webpage content
    tags_to_check = ['main', 'article', 'section', 'div']

    content = None
    # Iterate over each tag
    for tag in tags_to_check:
        # Find the first occurrence of this tag in the parsed HTML
        content = soup.find(tag)
        
        if content:  # If a tag was found with content
            break  # Stop looking for more tags

    # If some content was found in any of the tags
    if content:
        # Create an HTML to Markdown converter
        h = html2text.HTML2Text()
        # Ignore any links in the conversion
        h.ignore_links = True
        # Convert the HTML content to Markdown and store in the result
        result = {"content": h.handle(str(content))}
    else:
        result = {"error": "No suitable content tag found"}

    # Return the result as JSON
    return jsonify(result)

# Run this server if the script is started directly
if __name__ == '__main__':
    app.run(port=5000, debug=True)