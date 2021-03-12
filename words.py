from selenium import webdriver
import time
import json

words = []

numwords = int(input("Enter total number of words: "))
for i in range(1, numwords + 1):
    words.append(input("Enter word #" + str(i) + ": "))

driver = webdriver.Chrome('chromedriver.exe', service_log_path = 'NUL')
driver.get('https://www.wordsapi.com/')
print("")

for word in words:
    driver.find_element_by_id('word').clear()
    driver.find_element_by_id('word').send_keys(word)
    driver.find_element_by_id('getWord').click()
    
    time.sleep(0.1)

    try:
        data = json.loads(driver.find_element_by_class_name('hljs').text)
        print(word)
        print("")
        print(data['results'][0]['partOfSpeech'])
        print(data['results'][0]['definition'])
        print(data['results'][0]['examples'][0])
        print("")
        print("")

    except:
        print("For some reason we could not get the word " + '"' + word + '"')
        print("This might occur due to incorrect spelling or an error in the database")

driver.close()
input("Press any key to close . . .")
