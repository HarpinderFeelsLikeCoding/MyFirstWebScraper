import requests
from bs4 import BeautifulSoup

#url of th website to scrape
url = "https://weather.com/weather/today/l/b1449bff7d5c0f525164af0b1af9842fc0a2d930c270ed059a6220e71ee4b72a"

#fetch the html content, bs4 looks for thing based off the thml structure mainly
response = requests.get(url)

#parse the html content
soup = BeautifulSoup(response.content, "html.parser")

text = soup.get_text()
#extract specific data
#temperature = soup.find("div", class_="HourlyForecast--adWrapper--ZMPAH").text
#condition = soup.find("div", class_="condition").string

#print(f"Temperature: {temperature}")
#print(f"Condition: {condition}")
print(text)
print('\n\n')
print(soup.get_text())
