import my_Modules
import requests

my_Modules.hello()
r= requests.get("https://www.google.com")
print(r.text)