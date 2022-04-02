import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.implicitly_wait(5)

def new_post(username,password,file,text):

	browser.get('https://www.instagram.com/')


	coockies_button=browser.find_element_by_xpath("/html/body/div[4]/div/div/button[2]")
	coockies_button.click()



	sleep(2)

	username_input = browser.find_element_by_css_selector("input[name='username']")
	password_input = browser.find_element_by_css_selector("input[name='password']")

	username_input.send_keys(username)
	password_input.send_keys(password)

	login_button = browser.find_element_by_xpath("//button[@type='submit']")
	login_button.click()

	sleep(2)

	post_button= browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
	post_button.click()


	sleep(2)

	#pc_access= browser.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
	#pc_access.click()


	element = browser.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/form/input")
	element.send_keys(file)

	crop_button=browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button")
	crop_button.click()

	original_size = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]")
	original_size.click()


	i=0

	while i < 2 :

		next_button =  browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
		
		sleep(1)

		next_button.click()

		i+=1

		sleep(1)

	text_area = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
	text_area.click()
	text_area.send_keys(text)


	share_button=browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
	share_button.click()


usrname='laf1_pensa'
pswd = 'Massimopaola95€'
file_dir="/media/leonardo/864E-9799/botmag.png"

caption='Magnussen VS Bottas \nSaudi Arabia GP Qualifying \n\n #formula1\n#jeddah\n#telemetry\n#saudiarabia\n#haasf1\n#skysport\n#motorsport.com\n@haasf1team\n@alfaromeoorlen\n@kevinmagnussen\n@valtteribottas\n@skysportf1\n@f1'


#usrname=input("Username: ")
#pswd = getpass.getpass("Password:  ")
#file_dir=input("File directory: ")
#caption=input("Caption: ")

new_post(usrname,pswd,file_dir,caption)

