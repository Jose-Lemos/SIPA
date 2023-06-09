from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  # Replace with the appropriSate WebDriver for your browser
driver.implicitly_wait(5)  # Set the waiting time to 5 seconds

url = "https://www.bas.ac.uk/"
driver.get(url)

articles = driver.find_elements(By.CSS_SELECTOR, "article.item.text-center")


actions = ActionChains(driver)


time.sleep(2)  # Wait for 2 seconds (adjust as needed)


for article in articles:
    print(article.text.strip())
    print(article.get_attribute("outerHTML"))
    print("TAg IMG"+article.find_element(By.TAG_NAME,"img").get_attribute("outerHTML"))  #Para los links e imágenes
    tag = BeautifulSoup(""+article.get_attribute("outerHTML"), "html.parser")
    links = tag.find_all('a')
    imgs = tag.find_all('img')

    for link in links:
        print(link.get("href"))

    for img in imgs:
        print(img.get("src"))
    #print("BeautifullSoup"+tag.get_text())
    #actions.move_to_element(article).perform()
    

driver.save_screenshot("C:/Users/progr/Downloads/articles.png")
driver.quit()
