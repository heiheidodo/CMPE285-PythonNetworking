import urllib, urllib2, requests, json
import pandas as pd
from datetime import datetime

def internet_connection():
  try:
    urllib2.urlopen("http://www.google.com", timeout=1)
    return True
  except urllib2.URLError as err:
    return False
  
print("Input: (if you want to quit the program, please enter :q)")
symbol = raw_input("Please enter a symbol: \n");
while (symbol != ":q"):
  link = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol=" + symbol + "&callback=myFunction"
  
  if (internet_connection):   
    #f = requests.get(link)         
    #print (f.text)
    #print(type(f))
  
    f = urllib.urlopen(link)
    stock  = f.read()
    stock = stock[stock.find("(")+1:stock.find(")")]
    #print stock
  
    data = json.loads(stock)

    if (data.get('Message') != None):
      print("Warning:")
      print(data['Message'])
        
    else:
      print("Output:")
      ticker = data['Symbol']
      company_name = data['Name']

      date = data['Timestamp']
      #dateTime = datetime.strptime(date, '%b %d, %-I:%M%p %Z')
      print(date)
      print(company_name + " (" + ticker + ")")
      change = "%.2f" % data['Change']
      changePercent =  "%.2f" % data['ChangePercent']
      if (change[:1] != "+" and change[:1] != "-"):
          change = "+" + change
      if (changePercent[:1] != "+" and changePercent[:1] != "-"):
          changePercent = "+" + changePercent   
      change = "%.2f"%data['LastPrice'] + " " + change + " (" + changePercent  + "%)"
      print(change)
      
    print
    print("Input:")
    symbol = raw_input("Please enter a symbol:\n");
      
  else:
    print("Warning:")
    print("No Internet Connection!")
    break
    
