import undetected_chromedriver
import time


def undetected(link):
    driver = undetected_chromedriver.Chrome()
    driver.get(link)
    time.sleep(5)

    html_code = driver.page_source
    driver.close()
    driver.quit()
    return html_code
