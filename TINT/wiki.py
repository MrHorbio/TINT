import requests
from bs4 import BeautifulSoup

def get_wikipedia_company_info(company_name):
    # Search for the company's Wikipedia page
    search_url = f"https://en.wikipedia.org/wiki/{company_name.replace(' ', '_')}"
    response = requests.get(search_url)

    # Check if the page exists
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the title of the page (company name)
        title = soup.find('h1', {'id': 'firstHeading'}).text

        # Find the first paragraph of the company (summary/description)
        first_paragraph = soup.find('p')

        # Extract the paragraph text
        description = first_paragraph.text if first_paragraph else "No description available."

        # Get the infobox (details like founded year, location, etc.)
        infobox = soup.find('table', {'class': 'infobox'})

        company_details = {}

        if infobox:
            rows = infobox.find_all('tr')
            for row in rows:
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    key = th.text.strip()
                    value = td.text.strip()
                    company_details[key] = value

        return {
            'Company Name': title,
            'Description': description,
            'Details': company_details
        }
    else:
        return f"Error: {response.status_code} - Page not found."

# Example usage
company_name = "hackerone"  # Adjust company name as needed
company_info = get_wikipedia_company_info(company_name)

# Debugging: Print company_info to check if it's a dictionary or an error string
print(company_info)

# Proceed if company_info is a dictionary
if isinstance(company_info, dict):
    print(f"Company Name: {company_info['Company Name']}")
    print(f"Description: {company_info['Description']}")
    print("Company Details:")
    for key, value in company_info['Details'].items():
        print(f"{key}: {value}")
else:
    print("Error fetching company info:", company_info)
