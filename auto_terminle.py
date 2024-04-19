import selenium
import time
from termle import Termle

L = 5
ANSWERS_FILENAME = "words/possible_words.txt"
GUESSES_FILENAME = "words/allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

chrome = webdriver.Chrome()
chrome.get("https://www.nytimes.com/games/wordle/index.html")
time.sleep(5)

play_button = chrome.find_element(By.CLASS_NAME, "Welcome-module_button__ZG0Zh")
play_button.click()
time.sleep(2)

'''
try:
	ad_button = chrome.find_element(By.CLASS_NAME, "Skip-module_skipInfo__ZI2vt Skip-module_skipButton__m8KJ8")
	ad_button.click()
	time.sleep(2)

close_button = chrome.find_element_by_css_selector("[aria-label='Close']")
close_button.click()
time.sleep(1)

grid = chrome.find_element(By.CLASS_NAME, "Board-module_board__jeoPS")
grid.click()
'''

actions = ActionChains(chrome)
actions.send_keys(Keys.ENTER).perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()
time.sleep(1)

actions.send_keys("soare").perform()
time.sleep(3)
