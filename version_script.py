import requests

print(requests.__version__)

google_homepage = requests.get("https://www.google.com")
