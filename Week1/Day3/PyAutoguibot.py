import pyautogui
import time
from datetime import datetime 
date = datetime.now().strftime("%Y-%m-%d")  # Gets the current date in YYYY-MM-DD format
pyautogui.hotkey('win', 'r', interval=0.15)  # Opens Run dialog
time.sleep(1)  # Waits for the Run dialog to open
pyautogui.write('chrome', interval=0.15)  # Types 'chrome' in the Run dialog
pyautogui.press('enter')  # Presses Enter to open Chrome

time.sleep(1)  # Waits for Chrome to open
#pyautogui.hotkey('ctrl', 't', interval=0.15)  # Opens a new tab in Chrome
pyautogui.write('https://www.w3schools.com/python/', interval=0.15)  # Types the URL in the address bar
pyautogui.press('enter')  # Presses Enter to navigate to the website
#pyautogui.scroll(-1000)  # Scrolls page down to load more content
#pyautogui.press('enter')
time.sleep(1)  # Waits for the page to load  
pyautogui.hotkey('ctrl', 'a', interval=0.15)  # Selects all content on the page
pyautogui.hotkey('ctrl', 'c', interval=0.15)  # Copies the selected content
pyautogui.hotkey('ctrl', 'w', interval=0.15)  # Closes the current tab

pyautogui.hotkey('win', 'r', interval=0.15)  # Opens Run dialog again
time.sleep(0.5)  # Waits for the Run dialog to open   
pyautogui.write('excel', interval=0.15)  # Types 'excel' in the Run dialog
pyautogui.press('enter')  # Presses Enter to open Excel
time.sleep(3)  # Waits for Excel to open
pyautogui.press('enter')  # Opens a new workbook in Excel
time.sleep(1)  # Waits for the new workbook to open
pyautogui.press('enter')
time.sleep(1)  # Waits for the new workbook to open
pyautogui.write('Date', interval=0.15)  # Types 'Date' in the first cell
pyautogui.press('tab')  # Moves to the next cell
pyautogui.write('Information', interval=0.15)  # Types 'Information' in the second cell
pyautogui.press('tab')  # Moves to the next row
pyautogui.write('Note', interval=0.15)  # Types 'Note' in the first cell of the second row
pyautogui.press('enter')  # Moves to the next cell
pyautogui.write(date, interval=0.15)  # Types the current date in the first cell of the second row
pyautogui.press('tab')  # Moves to the next cell
pyautogui.hotkey('ctrl', 'v', interval=0.15)  # Pastes the copied content into Excel
time.sleep(4)  # Waits for the content to be pasted
pyautogui.press('right')  # Moves to the next cell
pyautogui.write('Information copied from w3schools.com', interval=0.15)  # Types a note in the next cell
pyautogui.hotkey('ctrl', 's', interval=0.15)  # Opens the Save dialog
pyautogui.press('right')  # Moves to the filename field in the Save dialog
pyautogui.press('down')  # Moves to the filename field in the Save dialog
pyautogui.press('down') 
pyautogui.press('down') 
pyautogui.press('down') 
pyautogui.press('down') 
pyautogui.press('down')  # Moves to the filename field in the Save dialog
pyautogui.press('enter')  # Presses Enter to select the filename field
time.sleep(0.5)  # Waits for the Save dialog to be ready
pyautogui.write(f'daily_report_{date}.xlsx', interval=0.15)  # Types the filename in the Save dialog
pyautogui.screenshot(f'daily_report_{date}.png')
pyautogui.press('enter')  # Presses Enter to save the file