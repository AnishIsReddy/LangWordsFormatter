import subprocess

try:
    subprocess.run('pip install Selenium',  capture_output = True)
except:
    pass

from selenium import webdriver

words = []
numwords = int(input("Enter total number of words: "))
for i in range(1, numwords + 1):
    words.append(input("Enter word #" + str(i) + ": "))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', service_log_path = 'NUL', options=options)

print("")

out = []

for word in words:
    print(word)
    out.append(word + "\n")
    
    try:
        driver.get('https://yourdictionary.com/' + word)
        print(driver.find_element_by_class_name('pos').text)
        out.append(driver.find_element_by_class_name('pos').text + "\n")

        print(driver.find_element_by_class_name('definition').text)
        out.append(driver.find_element_by_class_name('definition').text + "\n")

        driver.get('https://sentence.yourdictionary.com/' + word)
        out.append(driver.find_element_by_class_name('sentence-item').text + "\n")
    
    except:
        print("An error occured when getting data for this word")
        out.append("An error occured when getting data for this word\n")

    
    print("")
    out.append("/n")

driver.close()

f = open("output.txt", "w")
f.writelines(out)
f.close()
input("Press any key to close . . .")
