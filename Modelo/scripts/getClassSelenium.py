from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()  # Replace with the appropriSate WebDriver for your browser
driver.implicitly_wait(5)  # Set the waiting time to 5 seconds

url = "https://www.bas.ac.uk/"
driver.get(url)

articles = driver.find_elements(By.CSS_SELECTOR, "article.item.text-center")

actions = ActionChains(driver)


time.sleep(2)  # Wait for 2 seconds (adjust as needed)


for article in articles:
    print(article.text.strip())
    actions.move_to_element(article).perform()

driver.save_screenshot("C:/Users/progr/Downloads/articles.png")
driver.quit()
