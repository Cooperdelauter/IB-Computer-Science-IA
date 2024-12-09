from bs4 import BeautifulSoup
import requests

url = "https://www.surelockedin.com/escaperoomnearme.html"


result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

firstsearch = doc.find_all(["div"], class_ ="wcustomhtml")

print(firstsearch)


