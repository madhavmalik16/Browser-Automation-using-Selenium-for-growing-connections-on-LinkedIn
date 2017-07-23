#importing the necessary package
from selenium import webdriver

#importing the time function for controlling the time in which the browser will sleep
import time


#making a function for logging in
def login_LinkedIn(myemail, mypassword):

	#importing the executable path of the webdriver that is installed on our machine
	chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')

	#using the url of the LinkedIn website for our bot
	url = 'https://www.linkedin.com/'

	#running the given url using the chromedriver software
	#from selenium package
	chromedriver.get(url)

	#Maximising the window that is opened by the cheomdriver
	chromedriver.maximize_window()

	# printing using chromedriver
	# print chromedriver.page_source

	#finding the elements using the XPath
	#There are other techniques also for finding elements like by source or by html but here I am doing it by XPath


	#The XPath of the email button is = //*[@id="login-email"]
	email = chromedriver.find_element_by_xpath('//*[@id="login-email"]')
	#Sending the email using the send_keys function
	email.send_keys(myemail)

	#The XPath of the password button is = //*[@id="login-password"]
	password = chromedriver.find_element_by_xpath('//*[@id="login-password"]')
	#Sending the password using the send_keys function
	password.send_keys(mypassword)


	#Signing in
	#The Xpath of the sign in button is = //*[@id="login-submit"]
	sign_in = chromedriver.find_element_by_xpath('//*[@id="login-submit"]')
	#clicking the button
	sign_in.click()

	#time function for controlling the browser sleep time
	time.sleep(10)


#calling the function created
login_LinkedIn('Enter your email here','Enter your password here')

#searching for the people with specific skills
#The XPath of the search button is = //*[@id="a11y-ember925"]
search_input = chromedriver.find_element_by_xpath('//*[@id="main-search-box"]')
search_input.send_keys('Enter the name of the field here on the basis of which you want to search people') 

#The XPath of the search button is = //*[@id="nav-search-controls-wormhole"]/button
search_button = chromedriver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button')
#clicing the button
search_button.click()

#The XPath of the people button is = //*[@id="ember801"]/div[3]/div[3]/div/ul/li[2]/button
people_only = chromedriver.find_element_by_xpath('//*[@id="ember801"]/div[3]/div[3]/div/ul/li[2]/button')
#clicking the button
people_only.click()

#time function for controlling the browser sleep time
time.sleep(10)


#the number of results that come after typing the field
search_result = chromedriver.find_element_by_xpath('//*[@id="results_count"]/div/p/strong[1]')
search_result_num = int(search_result.get_attribute("textContent").replace(',',''))

#filtering the number of people in each page
page_num = search_result_num/10

#updating the current url
url = chromedriver.current_url

for page in range(1, page_num+1):
	new_url = url + '&page_num={0}'.format(page)
	chromedriver.get(new_url)

	#The XPath of 2nd connection is = //*[@id="ember6430"]/fieldset/ol/li[2]/label
	connect_connection = chromedriver.find_element_by_xpath('//*[@id="ember6430"]/fieldset/ol/li[2]/label')
	#clicking the button
	connect_connection.click()

	#time function for controlling the browser sleep time
	time.sleep(10)

	#finding the connect button by class name
	connecting_to_all = chromedriver.find_element_by_class_name('primary-action-button')
	for a in connecting_to_all
		a.click()
		time.sleep(3)


#after execution exiting the chromedriver
chromedriver.quit()

