Sure, here's your updated README.md with added explanations on how to use your tool:

```markdown
# Extractly

Extractly is a web scraping API built with Flask, BeautifulSoup, and html2text. It offers a straightforward service for scraping specific content from web pages.

## Requirements

- Python 3
- pip 

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/extractly.git
cd extractly
```

2. (Optional) Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Start the server:

```bash
python app.py
```

The server runs on port `5000` and is accessible from any network interface on your machine.

## Usage

You can call Extractly's scraping service by sending a GET request to the `/v1/api/webpage/` route with `url` and `selector` as parameters.

### Using the Selector

- **Select by ID**: Prefix the element's ID with a '#' symbol. For example, to select an element with the ID 'main', your selector would be '#main'.
- **Select by Class**: Prefix the class name with a '.' symbol. If the class is 'content', your selector should be '.content'.
- **Select by HTML Tag**: If you want to select elements by a specific HTML tag (like 'div', 'p', etc.), simply use the tag name as the selector.

### Example Requests:

- **Request to scrape the first element with the ID 'main':**

```bash
curl -X GET "http://localhost:5000/v1/api/webpage/?url=https://www.example.com&selector=#main"
```

- **Request to scrape the first element with the class 'content':**

```bash
curl -X GET "http://localhost:5000/v1/api/webpage/?url=https://www.example.com&selector=.content"
```

- **Request to scrape the first 'article' element:**

```bash
curl -X GET "http://localhost:5000/v1/api/webpage/?url=https://www.example.com&selector=article"
```

Note: This tool only returns the first matching element for the provided selector.

## Contributing

All contributions are welcome. Please open a new Issue or submit a Pull Request for any bugs, improvements, or feature requests.

## License

Extractly is licensed under the MIT License. See the `LICENSE.txt` file for details.

## Contact

For any inquiries or support, please create a new Issue or contact me at `gabe805@gmail.com`.
```