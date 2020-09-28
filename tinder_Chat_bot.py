from selenium import webdriver

from time import sleep

from secrets import username, password

from random import random

import requests, os

import keyboard


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.begining = True
        
    def login(self):
        self.driver.get('https://tinder.com')
    
        sleep(3)

        #Login windows are now random and different designs can appear, this suits the different scenarios
        try:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()

            # switch to login popup
            base_window = self.driver.window_handles[0]
            self.driver.switch_to_window(self.driver.window_handles[1])

            #Enter login info
            entr_email = self.driver.find_element_by_xpath('//*[@id="email"]')
            entr_email.send_keys(username)

            entr_pw = self.driver.find_element_by_xpath('//*[@id="pass"]')
            entr_pw.send_keys(password)

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()
        
        except Exception:
            leave = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            leave.click()

            connect = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            connect.click()

            moreOptions = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            moreOptions.click()

            sleep(2)
            fb_btn2 = ('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
            fb_btn2.click()

            # switch to login popup
            base_window = self.driver.window_handles[0]
            self.driver.switch_to_window(self.driver.window_handles[1])

            #Enter login info
            entr_email = self.driver.find_element_by_xpath('//*[@id="email"]')
            entr_email.send_keys(username)

            entr_pw = self.driver.find_element_by_xpath('//*[@id="pass"]')
            entr_pw.send_keys(password)

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()


        sleep(1.6)

        self.driver.switch_to_window(base_window)

        popup_cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_cookie.click()

        sleep(1.8)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        popup_2.click()

        sleep(3.4)

        self.driver.refresh() #After few trials the app will block the swipes, simply refresh to reactivate
 
        sleep(2.2)

        self.driver.switch_to_window(base_window)

        print('- | - Login completed')






    def auto_chat(self):     #Algorithm to launch the automated chat
        try:
            while True:
                rand = random() #Randomness to avoid bot detection

                print(rand)
            
                profile = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]/a/div[1]')
                profile.click()

                sleep(2.5)
                
                if rand < 0.20:
                    keyboard.write('I write poems, but it feels useless here :/ ')
                elif rand < 0.40:
                    keyboard.write('I am something in between a meme Lord and a poet')
                elif rand < 0.60:
                    keyboard.write('Being a poet seems like something useless nowadays, women use to be sensible the beauty of words. I cannnot tell if that is still the case...')
                elif rand < 0.80:
                    keyboard.write('If I shall be completely honest, I wrote you this message with an automated program I coded in Python. And I really think Im a cool guy for doing this')
                else:
                    keyboard.write('Angels were made after your portrait <3')

                sleep(0.8)

                send = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
                send.click()

                sleep(1.3)

                leave = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[1]/a/button')
                leave.click()

                return_to_messages = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
                return_to_messages.click()

                sleep(1.2)
            
        except keyboard.press('space'):
            print('Interrupted')






bot = TinderBot()
bot.login()
bot.auto_chat()