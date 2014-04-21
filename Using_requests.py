import requests                                                                 
import json                                                                     

r = requests.get("http://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json")
data_as_json = json.loads(r.content)
symbol = []
openPrice = []
highPrice = []
ex_date = []
i = 0
htmlstuff='<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable,th,td\n{\nborder:1px solid black;\nborder-collapse:collapse;\n}\nth,td\n{\npadding:5px;\n}\n</style>\n</head>\n\n<body>\n<table style="width:300px">\n<tr>\n  '

listofheaders=['Symbol','Open','High','Latest_Exp_date']

for header in listofheaders:
    htmlstuff=htmlstuff+'<th>'+str(header)+'</th>\n'
    
htmlstuff = htmlstuff+ '</tr>\n'

for stock_info in data_as_json['data']:
                      
    
    for key, value in stock_info.items():                                       
        key_parts = key.split('; ')
        key_parts = [part.lower() for part in key_parts]
        
        if "symbol" in key_parts:
            symbol.append(value)
        
        if "openprice" in key_parts:
            openPrice.append(value)
               
        if "highprice" in key_parts:
            highPrice.append(value)
            
        if "lastcorpannouncementdate" in key_parts:
            ex_date.append(value)
            
print symbol
print openPrice
print highPrice
print ex_date

while i <= 9:
    htmlstuff = htmlstuff+ '<tr>\n'
    htmlstuff = htmlstuff + '<td>' + (symbol[i]) + '</td>\n'
    htmlstuff = htmlstuff + '<td>' + (openPrice[i]) + '</td>\n'
    htmlstuff = htmlstuff + '<td>' + (highPrice[i]) + '</td>\n'
    htmlstuff = htmlstuff + '<td>' + (ex_date[i]) + '</td>\n'
    htmlstuff = htmlstuff+ '</tr>\n'
    i+=1
htmlstuff+='</table>\n</body>\n\n</html>'

f=open('created_html.html','w')
f.write(htmlstuff)
f.close()  