### WEB SCRAPPING USING PYTHON

import requests
from bs4 import BeautifulSoup   

#URL of the Web page to scrap
url = "https://www.python.org"

#Sending a get request to the web page
response=requests.get(url)

#To check if the request is successful
if response.status_code == 200:
    #Parse the HTML content of the page
    soup=BeautifulSoup(response.text,'html.parser')

    #Extracting all the text from the page
    page_text=soup.get_text()

    #Extracting all the links from the page
    links= [a['href']for a in soup.find_all('a',href=True)]

    #Extracting all the images from the page
    images = [img['src']for img in soup.find_all('img',src=True)]

    #Printing the extracted data
    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)
    
    print("\nImages:")
    for image in images:
        print(image)

else:
    print(f"Failed to retrieve the web page. Status code:{response.status_code}")