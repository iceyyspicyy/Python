# # get background notification using web scraping and and toastr like libraries
# # bs4 --> beautifulsoup4 for web scraping
# #win11toast --> updated for desktop notification
# #requests for making requests, send HTTP/1.1 requests extremely easily

# import requests
# import bs4 
from win11toast import toast

# #create an object for ToastNotification



# #func for getting data from url

# def getdata(url):
#     r = requests.get(url)
#     return r.text

# htmldata = getdata("https://weather.com/en-IN/weather/today/l/27.72,85.32")
# soup = bs4.BeautifulSoup(htmldata, 'html.parser')
# current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions--tempValue--MHmYY") 
  
# chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions--precipValue--2aJSf") 
# temp = (str(current_temp))
# rain = (str(chances_rain))

# result = temp + rain
# n = toast(result)




# import required libraries 
import requests 
from bs4 import BeautifulSoup 

  
# create an object to ToastNotifier class 

  
# define a function 
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 
  
soup = BeautifulSoup(htmldata, 'html.parser') 
  
current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY") 
  
chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 
  
temp = (str(current_temp)) 
  
temp_rain = str(chances_rain) 
   
result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" + temp_rain[131:-14] 
n = toast("live Weather update",  
             result, duration = 10) 