from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://brainlox.com/courses/category/technical')

time.sleep(5)  

try:
    page_source = driver.page_source

    with open('page_source.html', 'w', encoding='utf-8') as file:
        file.write(page_source)
    
    print("Page source saved successfully to 'page_source.html'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(2)  # Optional: Pause to see the output
    driver.quit()
