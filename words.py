import subprocess

try:
    subprocess.run('pip install Selenium')
except:
    pass
else:
    print("Selenium is not installed. Downloading it now.")


from selenium import webdriver

words = []
numwords = int(input("Enter total number of words: "))
for i in range(1, numwords + 1):
    words.append(input("Enter word #" + str(i) + ": "))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', service_log_path = 'NUL', options=options)

print("")

for word in words:
    print(word)
    
    try:
        driver.get('https://yourdictionary.com/' + word)
        print(driver.find_element_by_class_name('pos').text)
        print(driver.find_element_by_class_name('definition').text)

        driver.get('https://sentence.yourdictionary.com/' + word)
        print(driver.find_element_by_class_name('sentence-item').text)
    
    except:
        print("An error occured when getting data for this word")

    
    print("")

driver.close()
input("Press any key to close . . .")
