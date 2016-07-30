#Gather Merchant Names
import csv
def gather_merchants(driver):
    with open('./files/companies.csv', 'rb') as csvfile:
        companies = csv.reader(csvfile, delimiter=',', quotechar='"')
        for url in companies:
            myurl = url[0]
            driver.get(myurl)
            try:
                amazon_merchant = driver.find_element_by_xpath('//*[@id="merchant-info"]').text
                merchant = driver.find_element_by_xpath('//*[@id="merchant-info"]/a[1]').text
            except:
                with open('./files/companies_out.csv', 'a') as outfile:
                    outfile.write(myurl)
                    outfile.write(";")
                    try:
                        outfile.write("!!!!!NO MERCHANT INFO")
                    except:
                        outfile.write("")
                    outfile.write("\n")
                continue
                
            if "Ships from and sold by Amazon.com" in amazon_merchant:
                continue
            '''
            merchant = merchant.replace(" and Fulfilled by Amazon.","")
            merchant = merchant.replace("Sold by ", "")
            merchant = merchant.replace("Ships from and sold by ", "")
            merchant = merchant.replace(" and Fulfilled by Amazon in easy-to-open packaging.","")
            merchant = merchant.replace(". Gift-wrap available.", "")
            merchant = merchant.replace(" Gift-wrap available.","")
            #merchant = merchant.replace("Gift-wrap available.","")
            #merchant = merchant.replace(".", "")
            '''
            with open('./files/companies_out.csv', 'a') as outfile:
                outfile.write(myurl)
                outfile.write(";")
                try:
                    outfile.write(merchant)
                except:
                    outfile.write("!!!!!ERROR-UNICODE Company name")
                outfile.write("\n")
