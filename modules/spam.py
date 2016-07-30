#Send Spam from Deduplicated List
import time
import csv
import traceback
def spam(driver, delay, start_at):
    with open('./files/companies_out_deduplicated.csv','r') as deduplicated_csv:
        my_companies = csv.reader(deduplicated_csv, delimiter=';', quotechar='"')
        i = 0
        iterations = 0
        for my_url in my_companies:
            if i < start_at:
                i = i + 1
                #print "skip"
                continue
            #print "start at", start_at
            #print "iterations", iterations
            if iterations > 14:
                break
            company_name = my_url[1]
            my_url = my_url[0]
            driver.get(my_url)
            try:
                driver.find_element_by_xpath('//*[@id="merchant-info"]/a[1]').click()
            except:
                print "!!!!!!!!!Error while Opening Merchant {0}".format(my_url), company_name
                iterations = iterations + 1
                continue
            try:
                driver.get(driver.find_element_by_xpath('//*[@id="seller-contact-button-announce"]').get_attribute("href"))
                driver.find_element_by_css_selector("span.a-dropdown-prompt").click()
                driver.find_element_by_id("preOrderSubject_4").click()
                driver.find_element_by_name("writeButton").click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="file"]').send_keys('/home/myanime/amazon_script/sheets/AttachmentToSellers.pdf')
                driver.find_element_by_xpath('//*[@id="comment"]').send_keys(\
'''Hi,

I noticed a number of areas your product listings could be greatly improved which would dramatically improve your conversion rates and Amazon search rankings. I'd like to offer you a FREE product listing audit. See the attached PDF for my contact details. 

Kind regards, 
Jazmine''')
                time.sleep(delay)
                iterations = iterations + 1
                #driver.find_element_by_xpath('//*[@id="a-autoid-2"]').click()
                print company_name
                try:
                    with open('./files/spammed.csv', 'a') as spam:
                        spam.write(my_url)
                        spam.write(";")
                        spam.write(company_name)
                        spam.write("\n")
                except:
                    traceback.print_exc()
                    pass
                time.sleep(2)
            except:
                print "!!!!!!!!!Error while Spamming Merchant {0}".format(my_url), company_name
                iterations = iterations + 1
                continue
