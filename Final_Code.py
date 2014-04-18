

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

# Start the WebDriver and load the page
wd = webdriver.Firefox()
wd.get('http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G&utm_campaign=website&utm_source=sendgrid.com&utm_medium=email')

# Wait for the dynamically loaded elements to show up
#WebDriverWait(wd, 10).until(
    #EC.visibility_of_element_located((By.CLASS_NAME, "pricerow")))

# And grab the page HTML source
html_page = wd.page_source
#wd.quit()

htmlstuff='<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable,th,td\n{\nborder:1px solid black;\nborder-collapse:collapse;\n}\nth,td\n{\npadding:5px;\n}\n</style>\n</head>\n\n<body>\n<table style="width:300px">\n<tr>\n  '

listofheaders=['Symbol','Open','High','Latest_Exp_date']

for header in listofheaders:
    htmlstuff=htmlstuff+'<th>'+str(header)+'</th>\n'
    
htmlstuff = htmlstuff+ '</tr>\n'

# Now you can use html_page as you like
soup = BeautifulSoup(html_page)
table = soup.find("table", attrs = {"id":"topGainers"})
print "success"
records = []
#print table
for row in table.findAll('tr')[1:]:
    cols = row.findAll('td')
    #print cols
    some = [cols[0], cols[5], cols[6], cols[9]]
    #print some
    htmlstuff = htmlstuff+ '<tr>\n'
    for td in some:
        
        
        if td.find(text = True):
                text = ''.join(td.find(text = True))
                #text1 = text.encode('ascii')
                htmlstuff = htmlstuff + '<td>' + str(text) + '</td>\n'
                
        else:
                continue
    
    htmlstuff = htmlstuff+ '</tr>\n'

htmlstuff+='</table>\n</body>\n\n</html>'

f=open('created_html.html','w')
f.write(htmlstuff)
f.close()


