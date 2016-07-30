import time
import csv
from modules import login
from modules import gather_merchants
from modules import deduplicate
from modules import spam
import json

##############Merchant Retrieval, Deduplication and Mail Methods#############
def main():
    #Login
    #driver = login.login(EMAILS[0], PASSWORD)

    #Get Merchant Names
    #gather_merchants.gather_merchants(driver)

    #Deduplicate Merchant List
    #deduplicate.deduplicate()


    #Spam
    #Iterates over blocks of 3(15)urls, then moves on to next email address
    iterate_and_spam(start_at)

#############################################################################

with open('parameters.json') as json_file:
    parsed_json = json.load(json_file)

EMAIL_1 = parsed_json["email_1"]
EMAIL_2 = parsed_json["email_2"]
EMAIL_3 = parsed_json["email_3"]
EMAIL_4 = parsed_json["email_4"]
EMAIL_5 = parsed_json["email_5"]
EMAIL_6 = parsed_json["email_6"]
EMAIL_7 = parsed_json["email_7"]
EMAIL_8 = parsed_json["email_8"]
EMAIL_9 = parsed_json["email_9"]
EMAIL_10 = parsed_json["email_10"]
PASSWORD = parsed_json["generic_password"]
DELAY = parsed_json["delay_in_seconds"]
EMAILS = [EMAIL_1,EMAIL_2,EMAIL_3,EMAIL_4,EMAIL_5,EMAIL_6,EMAIL_7,EMAIL_8,EMAIL_9,EMAIL_10]
start_at = 0

def row_count_deduplicated():
    with open('./files/companies_out_deduplicated.csv', 'r') as deduplicated_csv:
        reader = csv.reader(deduplicated_csv, delimiter=',', quotechar='"')
        data = list(reader)
        row_count = len(data)
        return row_count

def iterate_and_spam(start_at):
    total_blocks = (row_count_deduplicated() / 15) + 1
    block = 0
    while block < total_blocks:
        try:
            driver.close()
        except:
            pass
        driver = login.login(EMAILS[block], PASSWORD)
        spam.spam(driver, DELAY, start_at)
        block = block + 1
        start_at = block*15

if __name__ == '__main__':
    main()
