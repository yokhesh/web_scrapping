import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get("http://publicrecords.countyofkings.com/RealEstate/SearchResults.aspx")
driver.find_element_by_xpath('//a[contains(text(), "Click here to acknowledge the disclaimer and enter the site")]').click()
deltime = WebDriverWait(driver,30).until(lambda driver: driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div[3]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input"))
deltime1 = WebDriverWait(driver,30).until(lambda driver: driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div[3]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[4]/table/tbody/tr/td[1]/input"))
#deltime.clear()
fromdate = "06/01/2016"
deltime.send_keys(fromdate)
time.sleep(1)
#deltime1.clear()
todate = "06/09/2016"
deltime1.send_keys(todate)
driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div[3]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr/td").click()

#Getting the number of pages
WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div[3]/table/tbody/tr[4]/td/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[3]"))
pg = driver.find_elements_by_xpath('//select[@id="cphNoMargin_cphNoMargin_OptionsBar1_ItemList"]')
page_no  = [x.text for x in pg]
sp_pageno = [i.split() for i in page_no]
sp_pageno = [j for i in sp_pageno for j in i]
total_pages = len(sp_pageno)/2
filename = "assignment1.csv"
f = open(filename, "w")
headers = "Date, document_number,document_type, Role, Person_name, APN, County, State\n"
f.write(headers)
f.close()
# Getting the values and entering them inside a csv file
for x in range(int(total_pages)):
    c_name = driver.find_elements_by_xpath('//tr[@id ]')
    c_name1 = [x.text for x in c_name]
    del c_name1[-1]
    del c_name1[0:3]
    len_of_each_page = int(len(c_name1))
    dat_filed = []
    dat_filed1 = []
    instrument_book_page = []
    instrument_book_page1 = []
    pname = []
    role = []
    document_type = []
    document_type1 = []
    county = []
    state = []
    apn = []
    apn1 = []
    for y in range(len_of_each_page):
        a = c_name1[y]
        b = a.split(" ")
        apne = a.split("\n")
        apne1 = apne[-1].split("Temp")
        apn.append(apne1[0])
        c = b[1]
        d = c.split("\n")
        dat_filed.append(d[1])
        instrument_book_page.append(d[0])
        e = a.split("[R]")
        fe = e[1].split("\n[E]")
        g = fe[0].strip()
        pname.append(g)
        h = fe[1].split("\n")
        i = h[0].strip()
        pname.append(i)
        dt = e[0].split("2016")
        dt1 = dt[1].strip()
        document_type.append(dt1)
    if x < ((int(total_pages))-1):
        driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div[3]/table/tbody/tr[3]/td/div/table/tbody/tr/td[5]/table/tbody/tr/td[1]/div/table/tbody/tr/td[1]/input[3]").click()
    for q in dat_filed:
        dat_filed1.extend([q,q])
    for qr in instrument_book_page:
        instrument_book_page1.extend([qr,qr])
    for qre in document_type:
        document_type1.extend([qre,qre])
    for qrei in apn:
        apn1.extend([qrei,qrei])
    ro = (int(len(pname)))/2
    for ro1 in range(int(ro)):
        ab = "Grantor"
        bc = "Grantee"
        role.append(ab)
        role.append(bc)
    for ad in range(int(len(pname))):
        pname[ad] = pname[ad].replace("(+)","")
        pname[ad] = pname[ad].strip()
        co = "Kings"
        county.append(co)
        st = "CA"
        state.append(st)
    with open("assignment1.csv","a") as scorefile:
        scorefileWriter = csv.writer(scorefile,lineterminator='\n')
        scorefileWriter.writerows(zip(dat_filed1,instrument_book_page1,document_type1,role,pname,apn1,county,state))
    time.sleep(5)
scorefile.close()

