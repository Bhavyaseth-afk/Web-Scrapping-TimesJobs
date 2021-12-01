from os import read
from bs4 import BeautifulSoup


with open('home.html' , 'r') as x:
    content  = x.read()
     
    soup = BeautifulSoup(content , 'lxml')
    # courses_tags = soup.find_all("h5")
    
    # for course in courses_tags:
    #     print(course.text)
    
    course_cards = soup.find_all('div' , class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        
        print(f"{course_name} costs {course_price}")
        
        