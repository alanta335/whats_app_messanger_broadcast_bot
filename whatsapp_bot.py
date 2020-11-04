from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 


driver = webdriver.Chrome() 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group in the a.txt file each person or group to send should be written in line by line(1 person or group to send per line in a.txt file)
f = open("a.txt","r+")
for line in f.readlines():
    target = line.rstrip("\n")
    # Replace the below string with your own message 
    string = "Message sent using Python!!!"

    x_arg = '//span[contains(@title,' +'"'+ target +'"'+')]'
    group_title = wait.until(EC.presence_of_element_located(( 
        By.XPATH, x_arg))) 
    group_title.click() 
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath)))
    # replace 1 in 'range(1)' 
    for i in range(1): 
        input_box.send_keys(string + Keys.ENTER) 
        time.sleep(1) 
