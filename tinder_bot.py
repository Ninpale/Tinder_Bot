from selenium import webdriver

from time import sleep

from secrets import username, password

from keras.layers import Dense

from beauty_predict import scores

from random import random

import requests, os

import keyboard


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def download_image(source, destination):
    img_data = requests.get(source).content
    with open(destination, 'wb') as out:
        out.write(img_data)

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.threshold = 5.5 
        self.begining = True
        
    def login(self):
        self.driver.get('https://tinder.com')
    
        sleep(3)

        #moreOptions = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        #moreOptions.click()

        #sleep(2)

        #fb_btn2 = ('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        #fb_btn2.click()

        #Login windows are now random and different designs can appear, you can choose the path above or below

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        entr_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        entr_email.send_keys(username)

        entr_pw = self.driver.find_element_by_xpath('//*[@id="pass"]')
        entr_pw.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2.1)

        self.driver.switch_to_window(base_window)

        popup_cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_cookie.click()

        sleep(1.8)

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        popup_2.click()

        sleep(3.4)

        self.driver.refresh() #After few trials the app will block the swipes, simply refresh to reactivate
 
        sleep(2.2)

        self.driver.switch_to_window(base_window)

        print('Login completed')








    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            rand = random() #Randomness to avoid bot detection
            if rand < 0.82:
                sleep(1.78)
            if rand < 0.38:
                sleep(1.12)
            else: 
                sleep(1.21)   

            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def choose(self):       #Algorithm to choose the who to swipe right
        scrs = self.current_scores()
        choice = "DISLIKE"
        if len(scrs) == 0:
            self.dislike()
        elif [scr > self.threshold for scr in scrs] == len(scrs) * [True]:
            self.like() 
            choice = "LIKE" 
        else:
            self.dislike()

        print("Scores : ",
              scrs,
              " | Choice : ",
              choice,
              " | Threshold : ",
              self.threshold)

    def ai_swipe(self):     #Algorithm to launch the swipes
        from random import random
        while True:
             
            if rand < 0.82:
                sleep(1.78)
            if rand < 0.38:
                sleep(1.12)
            else: 
                sleep(1.21)

            try:
                self.choose()
            except Exception as err:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                         print("Error: {0}".format(err))

        keyboard.wait('Ctrl') #Algo will stop when you hit 'Ctrl' on your keyboard










    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def get_image_path(self):
        body = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body')
        bodyHTML = body.get_attribute('innerHTML')
        startMarker = '<div class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;'
        endMarker = '&'

        if not self.begining:
            urlStart = bodyHTML.rfind(startMarker)
            urlStart = bodyHTML[:urlStart].rfind(startMarker)+len(startMarker)
        else:
            urlStart = bodyHTML.rfind(startMarker)+len(startMarker)

        self.begining = False
        urlEnd = bodyHTML.find(endMarker, urlStart)
        return bodyHTML[urlStart:urlEnd]

    def current_scores(self):
        url = self.get_image_path()
        outPath = os.path.join(APP_ROOT, 'images', os.path.basename(url))
        download_image(url, outPath)
        return scores(outPath)





bot = TinderBot()
bot.login()
bot.ai_swipe()