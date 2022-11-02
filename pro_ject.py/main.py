from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.set.or.th/th/market/product/stock/quote/ppm/price"
req = requests.get(url)

print(req)

req.encoding = "utf-8"
soup = BeautifulSoup(req.text , 'html.parser')
#print(soup.prettify())

courses = soup.find(span = "hebid-volume d-flex align-items-center mb-2 fs-13px")
print(courses)




#course_list = []
#for course in courses :
    #course_list.append(course.string)
#print(course_list)


#csv.col = [["price"], []]