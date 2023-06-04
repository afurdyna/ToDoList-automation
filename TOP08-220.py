from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Otwórz stronę: https://todolist.james.am/#/
driver = webdriver.Chrome()
driver.get("https://todolist.james.am/#/")
title = driver.title
assert title == "To Do List"
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-todo")))

# 2. W polu "What need's to be done?" wpisz pierwsze zadanie
task_1 = "zrobić zakupy"
text_box = driver.find_element(By.CLASS_NAME, "new-todo")
text_box.send_keys(task_1 + Keys.ENTER)
assert driver.find_element(By.XPATH, f'//label[text()="{task_1}"]').is_displayed() == True

# 3. Upewnij się czy domyślnie wybraną opcją filtrowania jest opcja "all"
assert driver.find_element(By.CSS_SELECTOR, ".filters .selected").text == "All"

# 4. W polu "What need's to be done?" wpisz drugie zadanie 
task_2 = "ugotować obiad"
text_box.send_keys(task_2 + Keys.ENTER)

# 5. Oznacz zadanie "zrobić zakupy" jako wykonane
driver.find_element(By.XPATH, f'//label[text()="{task_1}"]/../input').click()

# 6. Zmień filtr na "active"
driver.find_element(By.LINK_TEXT, "active").click()
assert driver.find_element(By.CSS_SELECTOR, ".filters .selected").text == "active"
tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-list .view")
assert len(tasks) == 1
assert tasks[0].text == task_2

# 7. Zmień filtr na "Completed"
driver.find_element(By.LINK_TEXT, "Completed").click()
assert driver.find_element(By.CSS_SELECTOR, ".filters .selected").text == "Completed"
tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-list .view")
assert len(tasks) == 1
assert tasks[0].text == task_1