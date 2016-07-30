from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='./chromedriver')
main_url = 'https://www.amazon.com/s/ref=sr_st_review-rank?rh=n%3A165796011%2Cn%3A!165797011%2Cn%3A166777011%2Cn%3A166779011&qid=1469816677&sort=review-rank'
driver.get(main_url)

for page in range(3,15):
    time.sleep(1)
    i = 1
    while i < 400:
        i = i + 1
        s =  '//*[@id="result_{0}"]/div/div[3]/div[1]/a'.format(i)
        i = i + 1
        try:
            print driver.find_element_by_xpath(s).get_attribute("href")
        except:
            continue
    driver.find_element_by_xpath('//*[@id="pagn"]/span['+str(page) +']/a').click()
    time.sleep(7)
    print 'next'
