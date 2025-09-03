# archive.org_searcher

This project is a full-stack, free-software application designed for educational purposes. Its primary function is to search for all links on a specific webpage (https://archive.org) and display them in a user-friendly modal interface. By leveraging Python with Flask for the backend and BeautifulSoup4 for web scraping, it allows users to extract links efficiently from any item hosted on archive.org. The frontend is built with standard web technologies, providing a clean, interactive experience where users can quickly view and copy the extracted links without leaving the page.

Beyond its practical functionality, this project serves as an excellent learning tool for students and developers exploring web scraping, full-stack development, and modal-based UI interactions. Users can study the code to understand how Flask handles requests, how BeautifulSoup parses HTML, and how frontend JavaScript dynamically updates the interface. Because it is fully open-source, it encourages experimentation and modification, allowing learners to extend its capabilities—for example, adding filters for certain types of links, integrating download options, or improving the modal design.

---

##  Description
A simple tool built with Flask, Python, and BeautifulSoup4, requests. It scrapes links from any provided URL and displays the results in a modal window on the front-end.

---

##  Technologies Used
- **Python** — backend logic  
- **Flask** — lightweight web server
- **requests** - simple restAPI lib
- **BeautifulSoup4** — parsing and link extraction  
- **HTML / CSS / JavaScript** — interface, modal, and asynchronous requests (AJAX/fetch)

---

##  How to Use

### Installation
```bash
git clone https://github.com/Dum2601/archive.org_searcher.git
cd archive.org_searcher
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### Run
```bash
flask run
```
Or:
```bash
python app.py
```
Access: `http://localhost:5000/`

### Workflow
1. Enter the target URL in the search field.  
2. Flask receives the request and performs scraping using BeautifulSoup4.  
3. A list of links is returned.  
4. The front-end displays the links inside an interactive modal.

---

##  Project Structure
```
src/
├── pages/                     # Front-end files (HTML + CSS)
│   ├── style/                  # Styles and layout
│   │   ├── modal.css           # CSS specific to the modal window
│   │   └── style.css           # Global styles for the page
│   └── index.html              # Main HTML page with search form and modal
│
├── utils/                      # Utility code and backend logic
│   ├── URL_operations/         # Module for URL processing
│   │   └── get_page.py         # Functions to fetch and parse links from a webpage
│   ├── routes.py               # Flask routes (handles requests and responses)
│   └── __pycache__/            # Auto-generated cache from Python (can be ignored)
│
├── main.py                     # Entry point of the Flask app (runs the server)
├── LICENSE                     # License file for open source use
└── README.md                   # Documentation of the project

```

---

##  Example of Use
- Open the main page.  
- Enter link, example: "https://archive.org/details/kotov-soviet-chess-school-1961"
- Click **Search links**.  
- The modal will show all the links found on the page.

---

##  Possible Improvements
- Error handling (timeouts, invalid URL, empty response).  
- Filtering by link type (internal, external, images, etc.).  
- Pagination or grouping of links.  
- Responsive design.  
- Docker containerization for easier deployment.

---

##  License
Released under the **GPL‑3.0** license.

---

##  Contact
Contributions are welcome. Please open Pull Requests or Issues on the author's GitHub.
