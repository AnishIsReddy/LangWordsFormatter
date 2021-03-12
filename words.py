from selenium import webdriver
import time
import json

words = []

numwords = int(input("Enter total number of words: "))
for i in range(1, numwords + 1):
    words.append(input("Enter word #" + str(i) + ": "))

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.wordsapi.com/')

for word in words:
    driver.find_element_by_id('word').clear()
    driver.find_element_by_id('word').send_keys(word)
    driver.find_element_by_id('getWord').click()
    
    time.sleep(0.1)

    data = json.loads(driver.find_element_by_class_name('hljs').text)

    try:
        print(word)
        print("")
        print(data['results'][0]['partOfSpeech'])
        print(data['results'][0]['definition'])
        print(data['results'][0]['examples'][0])
        print("")
        print("")

    except:
        print("For some reason we could not get the word " + '"' + word + '"')
        print("This might occur due to bad spelling or an error pulling data")


input("Type any key to close . . .")