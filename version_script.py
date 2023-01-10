import requests

print("Requests library version: ", requests.__version__)

google_homepage = requests.get("https://www.google.com")

python_script = requests.get("https://raw.githubusercontent.com/Tommy-Sand/cmput404_lab1/main/version_script.py")

print("Python script source code: ")
print(python_script.text)
