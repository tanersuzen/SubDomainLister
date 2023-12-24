import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"Unused domain: {word}")
        pass

target_input = input("Enter your target website: ")

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip() #erase the blanks in the doc
        url = "http://" + word + "." + target_input
        response = make_request(url)
        if response:
            print(f"Found Subdomain: {url}")