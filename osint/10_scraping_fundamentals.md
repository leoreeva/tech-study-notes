# Web Scraping: Theory and Fundamentals

## Course Overview

Web scraping is the automated extraction of data from websites. It transforms unstructured web content into structured data that can be analyzed, stored, and used for various applications including price monitoring, competitive analysis, market research, and academic studies.

## 1. Introduction to Web Scraping

### 1.1 What is Web Scraping?

**Web scraping** (also called web harvesting or web data extraction) is the process of:
- Automatically fetching web pages
- Parsing the HTML structure
- Extracting specific information
- Storing data in a structured format

### 1.2 Common Applications

| Application | Description |
|-------------|-------------|
| **Price Monitoring** | Track product prices across e-commerce platforms |
| **Competitive Analysis** | Monitor competitor offerings and strategies |
| **Market Research** | Gather data on market trends and consumer behavior |
| **Academic Research** | Collect data for statistical analysis |
| **Content Aggregation** | Compile information from multiple sources |
| **Brand Monitoring** | Track brand reputation and mentions |

### 1.3 Why Learn Web Scraping?

- **Data Accessibility**: Transform web content into usable datasets
- **Automation**: Eliminate manual data collection
- **Competitive Advantage**: Make data-driven decisions
- **Skill Development**: Essential for data science, analytics, and OSINT

## 2. HTML Structure Fundamentals

### 2.1 Basic HTML Document Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <!-- Visible content goes here -->
  </body>
</html>
```

**Key Components:**
- **`<html>`**: Root element containing all content
- **`<head>`**: Metadata, title, and resource links (not visible)
- **`<body>`**: Visible page content

### 2.2 Essential HTML Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| **`<h1>` - `<h6>`** | Headings (h1 largest) | `<h1>Main Title</h1>` |
| **`<p>`** | Paragraph | `<p>Text content</p>` |
| **`<div>`** | Division/container | `<div class="card">...</div>` |
| **`<span>`** | Inline container | `<span class="price">$20</span>` |
| **`<a>`** | Anchor/link | `<a href="url">Link text</a>` |
| **`<table>`** | Table structure | Contains rows and cells |
| **`<tr>`** | Table row | Contains table cells |
| **`<td>`** | Table data cell | Contains cell content |
| **`<th>`** | Table header | Header cell |

### 2.3 HTML Attributes

Attributes provide additional information about elements:

- **`class`**: CSS styling identifier (can be reused)
  ```html
  <div class="course-card">...</div>
  ```

- **`id`**: Unique identifier (used once per page)
  ```html
  <div id="main-content">...</div>
  ```

- **`href`**: Link destination
  ```html
  <a href="https://example.com">Link</a>
  ```

### 2.4 The Document Object Model (DOM)

The **DOM** represents HTML as a tree structure:
- Each element is a node
- Parent-child relationships define hierarchy
- Scraping navigates this tree to locate data

## 3. Web Scraping Tools and Libraries

### 3.1 Python Libraries Overview

| Library | Purpose | Use Case |
|---------|---------|----------|
| **Beautiful Soup** | HTML/XML parsing | Extracting data from HTML |
| **Requests** | HTTP requests | Fetching web pages |
| **lxml** | High-performance parser | Parsing large/malformed HTML |
| **Pandas** | Data manipulation | Structuring scraped data |
| **Selenium** | Browser automation | JavaScript-rendered content |
| **Scrapy** | Full scraping framework | Large-scale projects |

### 3.2 Beautiful Soup Key Concepts

**Installation:**
```bash
pip install beautifulsoup4
pip install lxml
```

**Import and Initialization:**
```python
from bs4 import BeautifulSoup

# Create soup object with lxml parser
soup = BeautifulSoup(html_content, 'lxml')
```

**Parser Comparison:**
| Parser | Speed | Fault Tolerance | Recommendation |
|--------|-------|-----------------|----------------|
| `html.parser` | Moderate | Good | Default, built-in |
| `lxml` | Fast | Excellent | **Recommended** |
| `html5lib` | Slow | Best | HTML5 compliance |

### 3.3 Core Beautiful Soup Methods

#### Finding Single Elements

**`find(tag, attributes)`**: Returns first matching element

```python
# Find first h5 tag
first_heading = soup.find('h5')

# Find with class attribute (note the underscore)
first_card = soup.find('div', class_='card')

# Find with any attribute
specific_link = soup.find('a', href='/courses')
```

#### Finding Multiple Elements

**`find_all(tag, attributes)`**: Returns list of all matching elements

```python
# All h5 headings
all_headings = soup.find_all('h5')

# All course cards
all_cards = soup.find_all('div', class_='card')

# Limit results
first_five = soup.find_all('p', limit=5)
```

#### Extracting Text and Attributes

```python
# Get text content
text = element.text
text = element.get_text()

# Get specific attribute
link_url = element['href']
link_url = element.get('href')
```

## 4. Scraping Methodology

### 4.1 The Scraping Workflow

1. **Inspect the Target**: Use browser developer tools
2. **Identify Data Location**: Find HTML tags containing target data
3. **Make HTTP Request**: Fetch the page content
4. **Parse HTML**: Convert to Beautiful Soup object
5. **Extract Data**: Navigate and select elements
6. **Store Results**: Save to file or database

### 4.2 Browser Developer Tools

**Accessing Developer Tools:**
- **Chrome/Edge**: Right-click → Inspect (or F12)
- **Firefox**: Right-click → Inspect Element
- **Safari**: Enable Develop menu in preferences

**Key Features:**
- **Elements Panel**: View and edit HTML/CSS in real-time
- **Network Panel**: Monitor HTTP requests
- **Console**: Test JavaScript and view errors
- **Selector Highlighting**: Hover over elements to see their HTML

### 4.3 CSS Selectors vs. Tag Navigation

**By Tag Name:**
```python
soup.find('h1')           # First h1 tag
soup.find_all('p')       # All paragraphs
```

**By Class:**
```python
soup.find('div', class_='product')     # Note: class_ with underscore
soup.find_all('span', class_='price')
```

**By ID:**
```python
soup.find('div', id='main-content')
```

**By Attribute:**
```python
soup.find('a', attrs={'data-type': 'product'})
```

### 4.4 Working with Tables

Tables use specific tag structure:
- **`<table>`**: Container
- **`<thead>`**: Header section
- **`<tbody>`**: Body section
- **`<tr>`**: Table row
- **`<th>`**: Header cell
- **`<td>`**: Data cell

**Extraction Pattern:**
```python
# Get table
table = soup.find('table', class_='data-table')

# Extract headers
headers = [th.text.strip() for th in table.find_all('th')]

# Extract rows
rows = []
for tr in table.find_all('tr'):
    row_data = [td.text.strip() for td in tr.find_all('td')]
    if row_data:  # Skip empty rows
        rows.append(row_data)
```

## 5. Data Storage and Structuring

### 5.1 Using Pandas DataFrames

**Why Pandas?**
- Structured tabular data
- Easy data manipulation
- Export to multiple formats (CSV, Excel, JSON)

**Basic Workflow:**
```python
import pandas as pd

# Create DataFrame with headers
df = pd.DataFrame(columns=headers)

# Add rows iteratively
df.loc[len(df)] = row_data

# Export
df.to_csv('scraped_data.csv', index=False)
```

### 5.2 Common Storage Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| **CSV** | `.csv` | Simple data, universal compatibility |
| **JSON** | `.json` | Hierarchical/nested data |
| **Excel** | `.xlsx` | Business reporting |
| **SQLite** | `.db` | Database storage |
| **Pickle** | `.pkl` | Python objects preservation |

## 6. Dynamic Content and JavaScript-Rendered Websites

### 6.1 Static vs. Dynamic Websites

**Static Websites:**
- HTML contains all data when page loads
- Content is immediately available in the source
- Scrapable with standard HTTP requests and HTML parsing

**Dynamic Websites (JavaScript/Ajax):**
- Content loads asynchronously after initial page load
- Data fetched via JavaScript execution
- HTML source ≠ rendered content visible in browser

**Ajax (Asynchronous JavaScript and XML):**
- Technique for loading content dynamically without full page refresh
- Data often loaded from separate API endpoints
- Common in modern web applications

### 6.2 Testing if a Website is Dynamic

**Method: Disable JavaScript in Browser**
1. Open Chrome/Edge developer tools (F12)
2. Press Ctrl+Shift+P to open command menu
3. Type "disable" and select "Disable JavaScript"
4. Refresh the page

**Results:**
- **Static site:** Content remains visible
- **Dynamic site:** Content disappears or falls back to basic functionality
- Note: Some sites may show fallback pagination instead of infinite scroll

### 6.3 Parsing vs. Rendering

| Concept | Definition | Implication |
|---------|------------|-------------|
| **Parsing** | Converting string representation into a data object | Beautiful Soup parses HTML strings |
| **Rendering** | Interpreting HTML, CSS, JavaScript, and images into visual display | Requires browser engine |

**Key Insight:**
- Beautiful Soup is a **parser**—it converts HTML strings into navigable objects
- It does **not** execute JavaScript or render dynamic content
- Dynamic websites require a **rendering engine** (browser) to execute JavaScript

### 6.4 Selenium for Dynamic Content

**When to Use Selenium:**
- JavaScript-rendered content not in initial HTML
- Single-page applications (SPAs)
- Content loaded via Ajax requests
- User interactions required (clicks, scrolling)

**Selenium Architecture:**
1. **Browser**: Chrome, Firefox, Edge, Safari (must be installed)
2. **WebDriver**: Browser-specific automation driver
3. **Selenium Package**: Python bindings for browser control

**Basic Selenium Workflow:**
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load page (JavaScript executes automatically)
driver.get('https://example.com')

# Get rendered HTML
html = driver.page_source

# Close browser
driver.quit()
```

### 6.5 Headless Browsers

**Definition:** Browser that runs without visible GUI—no window displayed.

**Benefits:**
- Faster execution (no rendering overhead)
- Lower resource consumption (CPU, RAM, bandwidth)
- Suitable for server environments
- No CSS/image loading delays

**Implementation:**
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
```

### 6.6 Extracting Data from Rendered Pages

**Hybrid Approach (Selenium + Beautiful Soup):**
```python
from selenium import webdriver
from bs4 import BeautifulSoup

# Use Selenium to render JavaScript
driver.get('https://dynamic-site.com')
html = driver.page_source
driver.quit()

# Use Beautiful Soup to parse rendered HTML
soup = BeautifulSoup(html, 'lxml')
data = soup.find_all('div', class_='content')
```

**Why This Combination Works:**
- Selenium handles JavaScript execution and rendering
- Beautiful Soup provides superior parsing and data extraction
- Best of both tools' strengths

### 6.7 Finding Hidden Data Sources (Efficient Alternative)

Instead of rendering full pages, locate where dynamic sites store data:

**Location 1: Embedded JSON in Script Tags**
- Data often stored as JavaScript variables in `<script>` tags
- View page source (Ctrl+U) and search for content
- Look for patterns: `var data = {...}` or `window.__DATA__ = {...}`

**Extraction Pattern:**
```python
import json
import re

# Find script containing data
script = soup.find('script', string=re.compile('var data'))
if script:
    # Extract JSON using regex
    json_text = re.search(r'var data = (\{.*?\});', script.string).group(1)
    data = json.loads(json_text)
```

**Location 2: XHR/Fetch API Requests**
1. Open developer tools → Network tab
2. Filter by "XHR" or "Fetch"
3. Trigger content load (scroll, click)
4. Inspect requests for JSON data endpoints
5. Extract data directly from API responses

**Benefits of Direct Data Access:**
- No browser automation overhead
- Faster than headless browsing
- Clean structured data (JSON)
- Reduced server load on target site

## 7. Advanced Scraping Considerations

### 7.1 Handling Multiple Elements on a Page

**Multiple Tables:**
```python
tables = soup.find_all('table', class_='wikitable')
target_table = tables[1]  # Access by index
```

**Nested Elements:**
```python
# Navigate parent-child relationships
card = soup.find('div', class_='course-card')
title = card.find('h5').text
price = card.find('a', class_='btn').text
```

### 7.2 Data Cleaning Techniques

**Common Issues:**
- Leading/trailing whitespace
- HTML entities (`&amp;`, `&lt;`)
- Inconsistent formatting
- Empty values

**Cleaning Methods:**
```python
# Remove whitespace
clean_text = element.text.strip()

# Remove specific characters
clean_text = text.replace('\n', ' ').replace('\t', '')

# Extract numeric values
price_text = "$20.50"
price_number = float(price_text.replace('$', ''))
```

### 7.3 Anti-Scraping Measures

| Measure | Description | Mitigation |
|---------|-------------|------------|
| **CAPTCHAs** | Human verification challenges | Headless browsers, solving services |
| **Rate Limiting** | IP-based request throttling | Request delays, IP rotation |
| **IP Blocking** | Banning scraper IP addresses | Proxy rotation, residential IPs |
| **Dynamic Content** | JavaScript-rendered content | Selenium, Playwright |
| **Honeypots** | Hidden traps for bots | Careful element selection |

### 7.4 Ethical and Legal Considerations

**Robots.txt:**
- File indicating which pages can be scraped
- Located at `domain.com/robots.txt`
- Should be respected ethically

**Best Practices:**
1. **Rate Limiting**: Add delays between requests (1-3 seconds)
2. **User-Agent**: Identify your scraper properly
3. **Terms of Service**: Review website ToS
4. **Copyright**: Don't redistribute scraped content
5. **Server Load**: Avoid overloading target servers

## 8. Automation and Scheduling

### 8.1 Cron Jobs

**Definition**: Time-based job scheduler for automating script execution.

**Syntax Pattern:**
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

**Common Examples:**
```bash
# Every hour
0 * * * * /usr/bin/python3 /path/to/scraper.py

# Daily at 8 AM
0 8 * * * /usr/bin/python3 /path/to/scraper.py

# Every Monday at 9 AM
0 9 * * 1 /usr/bin/python3 /path/to/scraper.py
```

### 8.2 Monitoring and Alerting

**Use Cases:**
- Price drop notifications
- Stock availability alerts
- Content change detection

**Implementation:**
- Compare current data with previous scrape
- Send email/SMS notifications on changes
- Log all scrapes for audit trail

## 9. Key Takeaways

### Core Concepts Summary

1. **HTML Structure Understanding**: Essential for locating data
2. **Beautiful Soup Methods**: `find()`, `find_all()`, `.text`, attributes
3. **CSS Class Filtering**: Use `class_` with underscore in Python
4. **Table Scraping**: Navigate `<tr>` and `<td>` tags systematically
5. **Data Structuring**: Use Pandas for tabular data
6. **Ethical Scraping**: Respect robots.txt and rate limits
7. **Automation**: Cron jobs enable scheduled scraping
8. **Dynamic Content**: Selenium for JavaScript-rendered sites; find hidden data sources when possible

### Common Mistakes to Avoid

- Scraping without checking robots.txt
- Using default HTML parser for broken HTML (use lxml)
- Forgetting the underscore in `class_`
- Not handling exceptions (network errors, missing elements)
- Scraping too fast and getting blocked
- Not cleaning extracted data
- Using Selenium when direct API/data source access is available

### Next Steps for Advanced Learning

- **Selenium**: For JavaScript-heavy websites
- **Scrapy**: For large-scale professional scraping
- **APIs**: Preferred over scraping when available
- **Proxy Management**: For bypassing IP blocks
- **Data Pipelines**: Building end-to-end data workflows

## 10. Quick Reference Guide

### Beautiful Soup Method Quick Reference

| Task | Method | Returns |
|------|--------|---------|
| First element by tag | `soup.find('tag')` | Single element or None |
| All elements by tag | `soup.find_all('tag')` | List of elements |
| By class | `soup.find('tag', class_='name')` | Matching element(s) |
| By ID | `soup.find('tag', id='name')` | Single element |
| By attribute | `soup.find('tag', attrs={})` | Matching element(s) |
| Get text | `element.text` or `element.get_text()` | String |
| Get attribute | `element['attr']` or `element.get('attr')` | String or None |
| Parent element | `element.parent` | Parent node |
| Children | `element.children` | Iterator of children |

### HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Success |
| 301/302 | Redirect | Follow redirect |
| 403 | Forbidden | Check headers/permissions |
| 404 | Not Found | Verify URL |
| 429 | Too Many Requests | Add delays |
| 500 | Server Error | Retry later |
| 503 | Service Unavailable | Server overload |

### Selenium Element Location Methods

| Method | Usage | Returns |
|--------|-------|---------|
| `find_element(By.ID, 'id')` | Locate by ID attribute | Single element |
| `find_element(By.CLASS_NAME, 'class')` | Locate by class name | Single element |
| `find_element(By.TAG_NAME, 'tag')` | Locate by HTML tag | Single element |
| `find_element(By.CSS_SELECTOR, 'css')` | Locate by CSS selector | Single element |
| `find_element(By.XPATH, 'xpath')` | Locate by XPath expression | Single element |
| `find_elements(...)` | Plural versions return lists | List of elements |

**Note:** Import `By` from `selenium.webdriver.common.by`

### Dynamic Content Scraping Decision Tree

```
Need to scrape a website?
        │
        ▼
Is content visible with JavaScript disabled?
        │
    ┌───┴───┐
   Yes      No
    │        │
    ▼        ▼
Standard   Is data embedded in
scraping     page source as JSON?
(Requests)        │
              ┌──┴──┐
             Yes    No
              │      │
              ▼      ▼
        Extract    Use Selenium
        JSON       (browser
        data       automation)
```
