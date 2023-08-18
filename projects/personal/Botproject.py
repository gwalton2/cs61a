from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
from Botproject_GUI import BotGui

user = BotGui()

while not user.ready:
	pass

class Bot:

	rooms4 = {'Egret':'Room 409', 'Goldeneye':'Room 411', 'Quail':'Room 431', 'Tern':'Room 433', 'Warbler':'Room 435'}
	rooms5 = {'Hemlock':'Room 503', 'Ironwood':'Room 505', 'Juniper':'Room 509', 'Laurel':'Room 511', 'Mesquite':'Room 513', 'Palm':'Room 517', 'Redwood':'Room 519', 'Tamarack':'Room 521'}

	def __init__(self, times, floor, username, password, room):

		self.times = times
		self.floor = floor
		self.username = username
		self.password = password
		self.room = room

		self.room_dict = None

		self.config_times()

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--incognito')	#forces Chrome to launch directly into incognito mode. Since the driver launches a brand new browser each time this is not necessary. For user's peace of mind. 
		self.driver = webdriver.Chrome(r'C:\Users\walto\Downloads\Selenium Webdrivers\chromedriver_win32\chromedriver.exe') #initializes the chrome webdriver by having the place where the webdriver was downloaded and stored on my computer
		self.wait_midnight()

	#this short loop waits unitl tomorrow to ensure that the rooms are open for booking
	def wait_midnight(self):
		#global time ????
		day, day1 = time.strftime('%e'), time.strftime('%e')
		while day != day1:
			day = time.strftime('%e')
		self.get_floor()
		self.book_rooms()

	def get_floor(self):
		if self.floor == 5:
			self.driver.get('http://berkeley.libcal.com/booking/moffitt-5')
			self.get_next_week()
			self.room_dict = Bot.rooms5
		else:
			self.driver.get('http://berkeley.libcal.com/booking/moffitt-4')
			self.room_dict = Bot.rooms4

	def get_next_week(self):
		day = int(time.strftime('%e')) + 7
		days = self.driver.find_elements_by_link_text(str(day))
		if len(days) == 0:
			time.sleep(.5)
			self.driver.find_element_by_css_selector('#s-lc-rm-cal > div > div > a.ui-datepicker-next.ui-corner-all > span').click() #fix so it waits for it to be clickable
			day = 1
			days = self.driver.find_elements_by_link_text(str(day))
			while(len(days) != 0):
				day+=1
				days = self.driver.find_elements_by_link_text(str(day))
			day-=1
		self.driver.find_elements_by_link_text(str(day))[0].click()	


	#takes the input time and converts it to form used on moffitt website. 1:00pm becomes 1:00pm to 1:50pm
	def config_times(self):
		ind = 0
		for i in self.times:
			if i[1] == ':':
				self.times[ind] = i+' to '+i[:2]+'5'+i[3:]
			else:
				self.times[ind] = i+' to '+i[:3]+'5'+i[4:]
			ind+=1

	#meat of the program. Does most of the work in loading the pages and clicking on things		
	def book_rooms(self):

		#global time ???
		for t in self.times:
			try:
				time.sleep(2) # was .35
				self.driver.find_elements_by_xpath('//a[contains(@title, "'+self.room+', '+self.room_dict[self.room]+', '+t+'")]')[0].click() #Bread and butter of this program. Searches for the element containing the title corresponding to the room/time user chose. 
			except Exception as error:
				print('Error with clicking on room for '+t+' :', error)
		time.sleep(1)
		element = self.driver.find_element_by_css_selector('#rm_tc_cont')
		ActionChains(self.driver).move_to_element(element).click().build().perform() 		
		#WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rm_tc_cont'))).click() #clicks continue

		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s-lc-rm-sub'))).click() #clicks submit form

		try:
			WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#username'))).send_keys(self.username) #fills in username
			self.driver.find_element_by_css_selector('#password').send_keys(self.password)											#fills in password
			self.driver.find_element_by_css_selector('#loginForm > fieldset > p.submit > input.button').click() #clicks submit
		except Exception as error:
			print('Error with sign-in form:', error)
			self.driver.quit()

		try:
			WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_shib_idp_doNotRememberConsent'))).click() #this part deals with the consent form that is unique to a bot's attempt to book for some reason. 
			self.driver.find_element_by_css_selector('body > form > div > div:nth-child(7) > p:nth-child(3) > input[type="submit"]:nth-child(2)').click()
		except Exception as error:
			print('Error with consent form:', error)
			self.driver.quit()

		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s-lc-rm-sub'))).click() #clicks final submit button
		print("Successfully booked time(s) for "+self.username) 
		self.driver.quit() #quits this chrome webdriver instance and closes window

Bot(user.times_list, user.floor, user.username, user.password, user.room)

	