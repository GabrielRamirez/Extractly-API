# Web Scraper API

Web Scraper API is a versatile tool that extracts webpage content from any URL and converts it into Markdown format. It is built with Python, Flask, BeautifulSoup and html2text.

## Setup

- Clone this repository to your local machine.
- Set up a virtual environment and activate it.
- Install the required dependencies with:

```bash
pip install flask requests beautifulsoup4 html2text
```

## API Usage

Run `python main.py` to start the server, which listens on http://localhost:5000 by default.

It offers a single endpoint, `GET /v1/url`, which accepts a `url` query parameter with the URL of the page to scrape.

**Example:**
```
http://localhost:5000/v1/url?url=http://example.com
```

## Response

It responds with a JSON object. On successful requests, the `content` field contains the main content of the webpage in Markdown format. If an error occurs, the `error` field provides an error message.

**Success example:**
```json
{
  "content": "# Title\n\nThis is some text from the example.com homepage.\n\n* And a bullet point\n\n> And a quote"
}
```
**Error example:**
```json
{
  "error": "Invalid URL 'http: ww//': No schema supplied. Perhaps you meant http://http: ww//?"
}
```

## Contributing

We welcome contributions. To propose changes, please open an issue for discussion. For minor fixes and improvements, feel free to open a