# ShadowBot V1.X.X
### KAVACH-2023 PSID: KVH-006 (Dark Web Crawler)

ShadowBot is a simple Python web crawler that searches for and extracts.onion links from a given parent URL. It makes HTTP requests with the requests library, parses HTML content with BeautifulSoup, and configures a SOCKS5 proxy with PySocks to connect to the Tor network.

Features:
- Crawls web pages to find .onion links
- Uses a SOCKS5 proxy to access the Tor network
- Supports infinite recursion limit
- Allows users to display crawled .onion links


```python
git clone https://github.com/c4rb0nx1/ShadowBot.git
cd ShadowBot
pip install -r requirements.txt
```

Usage:
```python
python3 shadowbot.py
```
License

This project is released under the MIT License.

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
