import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

async def main():
    url = "https://secure.rec1.com/TX/up-tx/catalog"

    driver = webdriver.Firefox()
    driver.get(url)

    # maximize window
    driver.maximize_window()

    import json

    with open("data.json", "r") as f:
        data = json.load(f)

    time1 = data["time"]
    time2 = data["time2"]
    venue = data["venue"]
    date1 = "04/15/2024"

    email = data["email"]
    password = data["password"]

    venues = {
        "Burleson-East": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[1]/div[1]/div[1]/span[1]",
        "Burleson-West": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[2]/div[1]/div[1]/span[1]",
        "Caruth-East": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[3]/div[1]/div[1]/span[1]",
        "Caruth-West": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[4]/div[1]/div[1]/span[1]",
        "Curtis-East": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[5]/div[1]/div[1]/span[1]",
        "Curtis-West": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[6]/div[1]/div[1]/span[1]",
        "Germany-East": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[7]/div[1]/div[1]/span[1]",
        "Germany-West": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[8]/div[1]/div[1]/span[1]",
        "Smith-East": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[9]/div[1]/div[1]/span[1]",
        "Smith-West": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[1]/div[1]/span[1]",
    }

    calendar_dates = {
        1: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[1]/td[6]/a[1]",
        2: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[1]/td[7]/a[1]",
        3: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[1]/a[1]",
        4: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[2]/a[1]",
        5: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[3]/a[1]",
        6: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[4]/a[1]",
        7: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[5]/a[1]",
        8: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[6]/a[1]",
        9: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[2]/td[7]/a[1]",
        10: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[1]/a[1]",
        11: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[2]/a[1]",
        12: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[3]/a[1]",
        13: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[4]/a[1]",
        14: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[5]/a[1]",
        15: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[6]/a[1]",
        16: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[3]/td[7]/a[1]",
        17: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[1]/a[1]",
        18: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[2]/a[1]",
        19: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[3]/a[1]",
        20: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[4]/a[1]",
        21: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[5]/a[1]",
        22: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[6]/a[1]",
        23: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[4]/td[7]/a[1]",
        24: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[1]/a[1]",
        25: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[2]/a[1]",
        26: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[3]/a[1]",
        27: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[4]/a[1]",
        28: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[5]/a[1]",
        29: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[6]/a[1]",
        30: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[5]/td[7]/a[1]",
        31: "/html[1]/body[1]/div[15]/table[1]/tbody[1]/tr[6]/td[1]/a[1]",
    }

    checkout_dates = {
        16: "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[7]/a[1]",
        17: "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/a[1]",
        18: "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/a[1]",
        19: "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[3]/a[1]",
        20: "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/a[1]",
    }
    time.sleep(10)
    # login
    login = driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/span[2]",
    ).click()
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/form[1]/div[2]/div[1]/input[1]",
    ).send_keys(email)
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/form[1]/div[3]/div[1]/input[1]",
    ).send_keys(password)

    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/form[1]/div[4]/div[1]/button[1]/span[1]",
    ).click()

    time.sleep(5)
    # click on reservations
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/span[1]",
    ).click()

    time.sleep(8)

    # click on tennis
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[3]/div[2]",
    ).click()

    time.sleep(3)

    #click on list view
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[2]/div[1]/button[2]/span[1]"
    ).click()

    time.sleep(3)
    # change the time

    xpath_to_click = ""
    found = False
    for key, value in zip(venues.keys(), venues.values()):
        if key == str(venue):
            xpath_to_click = value
            found = True
            print(xpath_to_click)
            break  # Exit the loop after finding the match


    if found is False:
        print("Error venue not found")
        quit()


    scroll_count = 5  # Change this as needed

    # Scroll down using JavaScript
    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for some time after each scroll to let content load
        driver.implicitly_wait(5)  # You can adjust the wait time as needed

    """# edit time value
    try:
        el = driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[6]/div[1]/div[1]/div[2]/span[2]/span[1]/input[1]",
        )
    except:
        el = driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[6]/div[1]/div[1]/div[2]/span[1]/span[1]/input[1]",
        )

    el.clear()
    el.send_keys(date1)
    """


    time.sleep(3)
    driver.find_element(By.XPATH, xpath_to_click).click()

    time.sleep(5)

    # get today's date
    today = time.localtime(time.time())
    today = today.tm_mday

    today = today+2
    print(today)



    driver.find_element(By.XPATH, checkout_dates[today]).click()
    #driver.find_element(By.PARTIAL_LINK_TEXT)

    time.sleep(3)

    five_thirty = "/html[1]/body[1]/div[17]/div[2]/div[9]"
    six_oclock = "/html[1]/body[1]/div[17]/div[2]/div[10]"
    six_thirty = "/html[1]/body[1]/div[26]/div[2]/div[9]"

    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]"
    ).click()

    time.sleep(2)

    driver.find_element(
        By.CSS_SELECTOR,
        "div[class='selectmenu-items notranslate open'] div[title='06:30 PM']"
    ).click()

    time.sleep(2)

    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[7]/div[4]/div[2]/div[2]/div[5]/div[10]/div[3]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]"
    ).click()

    time.sleep(5)

    driver.find_element(
        "/html[1]/body[1]/div[9]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/a[1]/span[1]"
    ).click()
    
    return