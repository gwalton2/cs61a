from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(r'C:\Users\walto\Downloads\Selenium Webdrivers\chromedriver_win32\chromedriver.exe', chrome_options = chrome_options)

"""driver.get("https://www.google.com")
elem = driver.find_element_by_css_selector('#lst-ib')
elem.clear()
elem.send_keys("elon musk")
elem.send_keys(Keys.RETURN)
driver.close()"""

"""from selenium import webdriver
import time


day = int(time.strftime('%e')) + 7
try:
	driver.find_element_by_link_text(str(day)).click()
except:
	edge = 1
	while True:
		try:
			driver.find_element_by_link_text(str(day-edge)).click()
			break
		except:
			edge +=1
	driver.find_element_by_css_selector('#s-lc-rm-cal > div > div > a.ui-datepicker-next.ui-corner-all > span').click()
	driver.find_element_by_link_text(str(edge)).click()

time.sleep(3)
driver.quit()


import time
date = time.strftime('%A, %B%e, %Y')
x=time.strftime('%A')
while x != 'Wednesday':
	x=time.strftime('%A')
print(2)

elem = driver.find_element_by_css_selector('#lst-ib')
elem.clear()
elem.send_keys("elon musk")
elem.send_keys(Keys.RETURN)
driver.close()
[title='"+time+"']

#if __name__ == "__main__":
	#get = Parallel(n_jobs=len(info))(delayed(user)(l[0], l[1], l[2], l[3], l[4]) for l in info)	


user_data = [x for x in input("Enter either floor '4' or '5', the first user's username, password, and the room they would like to book seperated by commas. Example: 4, oskibear, Iamoski14, Egret"+'\n').split(", ")]
user = 1
while user_data[0] != 'done':
	times = [x for x in input("Enter the times(up to two) you want user #"+str(user)+" to book seperated by commas. IMPORTANT: You can only book times back-to-back. Example: 3:00pm, 4:00pm"+'\n').split(", ")]
	_thread.start_new_thread(book_room, (times, user_data[0], user_data[1], user_data[2], user_data[3] ))	#by using the thread class, the code does not wait for this line of code to complete before moving on, allowing the user to make multiple calls to book_room before midnight
	user += 1
	user_data = [x for x in input("Enter either floor '4' or '5', the next user's username, password, and the room they would like to book seperated by commas. Example: 4, oskibear, Iamoski14, Egret. If you are done then enter 'done'"+'\n').split(", ")]"""






	

	


	