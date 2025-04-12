import requests

def search_pastebin(target):
    url = f"https://pastebin.com/api_public.php?method=pasteSearch&query={target}"
    response = requests.get(url)
    return response.text

# Example usage:
target = "google.com"
leaks = search_pastebin(target)
print(leaks)
