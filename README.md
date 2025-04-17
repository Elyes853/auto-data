## 🤖 robots.txt & Ethical Scraping

Before starting the scraping process, I checked the site's `robots.txt` file at:

https://www.auto-data.net/robots.txt

This file provides rules about which parts of the website are allowed to be crawled by bots. As of the time of scraping, the `robots.txt` did not disallow the pages I accessed for data collection (brands, models, and detail pages).

Even though scraping is technically possible, I made sure to:

- Add short delays to avoid overloading the server
- Avoid scraping unnecessary or restricted content

Respecting website policies and being gentle with traffic is a priority.

# Auto-Data Web Scraper 🚗

This project is a simple web scraper built to extract car specification data from [auto-data.net](https://www.auto-data.net/en/allbrands).

It navigates through car brands, models, and detail pages to collect structured data such as engine power, fuel type, production years, and more.

## 📹 Demo

Check out the video walkthrough of this project here:  
👉 [Video Link](#)

## 📂 Features

- Extracts car brands, models, and their specs
- Outputs data into a structured JSON file
- Modular and extensible

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup (for HTML parsing): *pip install beautifulsoup4*
- Selenium (for dynamic page loading): *pip install selenium*


