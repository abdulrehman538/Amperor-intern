# Step 1: Import libraries

import requests  # 👉 REQUESTS LIBRARY (used to fetch website data)
from bs4 import BeautifulSoup  # 👉 BeautifulSoup (used for web scraping)

# Step 2: Website URL
url = "https://example.com"

# Step 3: REQUESTS LIBRARY in action
# 👉 This sends an HTTP request to the website and gets HTML back
response = requests.get(url)

# Step 4: Store HTML content
html_content = response.text  # raw HTML from website

# Step 5: WEB SCRAPING starts here
# 👉 BeautifulSoup parses HTML so we can extract data easily
soup = BeautifulSoup(html_content, "html.parser")

# Step 6: Extract data (SCRAPING)
# 👉 Now we are scraping specific elements from HTML

title = soup.title.text   # extract page title
heading = soup.h1.text     # extract first heading (if exists)

# Step 7: Print results
print("Title:", title)
print("Heading:", heading)