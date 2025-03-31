
# Web Spider

This is a simple implementation of a web spider, written in python.

When given a URL then it will fetch the webpage and look for links (<a> tags) which it will then save in an array, before scanning that page aswell. 


## Features

- Recursively scan webpages
- Save selected tags with their contents
- Output results to a file
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/BenjaminGade/Web-Spider.git
```

Go to the project directory and set up venv

```bash
  cd Web-Spider
  python -m venv .
```

Install beautifulsoup4

```bash
  pip install bs4
```

Run the spider

```bash
  python spider.py -h
```

Example

```bash
  python spider.py --url https://example.com --find p --output out.txt
```
