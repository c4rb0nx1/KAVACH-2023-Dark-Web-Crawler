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
count = 1
while not queue.empty() and len(visited) < MAX_RECURSION:    
    # Get next URL from queue
    try:
        url = queue.get()
        # Skip URL if already visited
        if url in visited:
            continue

        # Print progress
        print(f"Crawling {count} : {url}...")

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
        count+=1
    except KeyboardInterrupt:
        print("\n\n\n---------------------------------------------------------------------------")
        print("\nKeyboardInterrupt detected! Exiting the program.")
        try:
            final_links = [i for i in tot_web if '.onion' in i]
        except TypeError:
            pass
        finally:
            print("\nTotal links crawled",len(tot_web))
            print("\nTotal onion links :",len(final_links))
            print("\n---------------------------------------------------------------------------")
            command = input('''y: display onion links and continue crawling \nd: continue without displaying onion links\nx:exit crawling (y/d/x) : ''')
            if(command == 'y'):
                [print(i) for i in final_links]
                print("\n continuing to Crawl chief :) \n")
            elif command == 'd':
                pass
            else:
                print("Night Night :) im going back to the shadows!")
                break
    except:
        print("Access Denied")

    
