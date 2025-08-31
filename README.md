<div align="center">
  <h1>🌐 Web Scraper App</h1>
  <p><i>A simple and extensible command-line tool for scraping web data.</i></p>
</div>

<br>

<div align="center">
  <!-- Replace with your actual repo URL -->
  <a href="https://github.com/brej-29/Logicmojo-AIML-Assignment-WebScrapperApp">
    <img alt="Last Commit" src="https://img.shields.io/github/last-commit/brej-29/Logicmojo-AIML-Assignment-WebScrapperApp">
  </a>
  <img alt="Python Language" src="https://img.shields.io/badge/Language-Python-blue">
  <img alt="Requests" src="https://img.shields.io/badge/Library-Requests-orange">
  <img alt="BeautifulSoup" src="https://img.shields.io/badge/Library-BeautifulSoup-green">
  <img alt="Pandas" src="https://img.shields.io/badge/Library-Pandas-blueviolet">
</div>

<div align="center">
  <br>
  <b>Built with the tools and technologies:</b>
  <br>
  <br>
  <code>Python</code> | <code>Requests</code> | <code>BeautifulSoup</code> | <code>Pandas</code>
</div>

---

## **Table of Contents**
* [Overview](#overview)
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## **Overview**

This project is a command-line web scraping application built with Python. It allows users to extract structured data from different websites through an interactive menu. The scraped data is displayed in the console and can be optionally saved to a CSV file for further analysis.

The application is designed to be easily extensible, allowing new scrapers for other websites to be added with minimal effort.

---

## **Features**

- **Interactive CLI:** A user-friendly command-line interface to select a scraping target.
- **Multiple Scrapers:**
    - **IMDb Top 250 Movies:** Scrapes movie title, release year, duration, and IMDb rating.
    - **Former Presidents of India:** Scrapes the list of presidents from Wikipedia, including their name, lifespan, home state, and term of office.
- **Data Export:** Option to save the scraped data into a clean, well-formatted CSV file.
- **Modular Design:** The code is organized into modules for scraping, utilities, and the main application logic, promoting readability and maintainability.

---

## **Getting Started**

### **Prerequisites**
- Python 3.7+
- The following Python libraries are required:
  * `requests`
  * `beautifulsoup4`
  * `pandas`

### **Installation**
1. Clone the repository (you'll need to set this up on a platform like GitHub):
   ```sh
   git clone https://github.com/your-username/webscraper-app.git
   ```
2. Navigate to the project directory:
   ```sh
   cd webscraper-app
   ```
3. It is recommended to create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required packages from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

### **Usage**
1. Run the application from the root directory of the project:
   ```sh
   python src/main.py
   ```
2. The console will display a menu of available scraping options. Follow the on-screen prompts to choose a website to scrape, view the results, and optionally save them to a CSV file.

---

## **Project Structure**
```
webscraper-app/
├── src/
│   ├── __init__.py
│   ├── main.py         # Main application entry point, handles user interaction
│   ├── scraper.py      # Contains all the web scraping logic
│   └── utils.py        # Utility functions (e.g., saving to CSV)
├── requirements.txt    # Lists project dependencies
└── README.md           # This file
```

---

## **License**
This project is licensed under the MIT License. Consider creating a `LICENSE` file in your project root.

---

## **Contact**
If you have any questions or feedback, feel free to reach out to me via my [LinkedIn Profile](https://www.linkedin.com/in/brejesh-balakrishnan-7855051b9/).
