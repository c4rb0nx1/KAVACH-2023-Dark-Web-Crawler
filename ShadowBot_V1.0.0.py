#This is a dark web crawler....make sure your TOR is configured..up...and running fine.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from queue import Queue
import socks
import socket
import signal


# Configure the SOCKS proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

url = input("Enter Your Parent URL: ")

# Initialize queue and add starting URL
queue = Queue()
queue.put(url)
visited = set()
tot_web = set()


final_links = []

# Set recursion limit
MAX_RECURSION = float('inf') #setting recursion limit to infinity!

    
# Get next URL from queue
try:
    while not queue.empty() and len(visited) < MAX_RECURSION:
        url = queue.get()
        # Skip URL if already visited
        if url in visited:
            continue

        # Print progress
        print(f"Crawling {url}...")

        # Add URL to visited set
        visited.add(url)

        # Send GET request and parse HTML content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract links from HTML content
        for link in soup.find_all("a"):
            # Get absolute URL
            href = link.get("href")
            if href is not None:
                href = urljoin(url, href)

                # Add URL to queue if it hasn't been visited yet
                if href not in visited:
                    queue.put(href)
            tot_web.add(href)
except KeyboardInterrupt:
    print("\n\n\n---------------------------------------------------------------------------")
    print("\nKeyboardInterrupt detected! Exiting the program.")
    final_links = [i for i in tot_web if '.onion' in i]
    print("\nTotal links crawled",len(tot_web))
except:
    print("Access Denied")
finally:
    print("\nTotal onion links :",len(final_links))
    print("\n---------------------------------------------------------------------------")
    display = input("display onion links (y/n) : ")
    if(display == 'y'):
        [print(i) for i in final_links]
    print("Night Night :)")
