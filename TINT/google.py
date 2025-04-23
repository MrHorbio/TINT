import requests
from bs4 import BeautifulSoup
import time
import random

def google_scrape(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    search_url = f"https://www.google.com/search?q={query}"

    # Send a request to Google with headers to simulate a browser request
    response = requests.get(search_url, headers=headers)

    # If the request is successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all search result links
        search_results = []
        for item in soup.find_all('div', class_='tF2Cxc'):
            title = item.find('h3')
            link = item.find('a')['href']
            snippet = item.find('div', class_='VwiC3b')

            # Only store the results with valid data
            if title and link:
                search_results.append({
                    "Title": title.text.strip(),
                    "Link": link.strip(),
                    "Snippet": snippet.text.strip() if snippet else "No description available"
                })
        
        return search_results
    else:
        return f"Error: Unable to retrieve data. Status code: {response.status_code}"

# Example usage
company_name = "o7services"
company_info = google_scrape(company_name)

# Print search results
for result in company_info:
    print(f"Title: {result['Title']}")
    print(f"Link: {result['Link']}")
    print(f"Snippet: {result['Snippet']}\n")
    
    # Add a small delay to avoid overloading the server
    time.sleep(random.uniform(1, 2))  # Random delay between 1 and 2 seconds
