from selenium.webdriver.common.by import By
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):

    browser.get(link)

    browser.implicitly_wait(10)
    # Ожидание появления искомого элемента кнопки
    button_name = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    with open("button_name.txt", "w+") as f:
        f.write(button_name.text)
    # Запись текста с искомого элемента кнопки в файл для проверки