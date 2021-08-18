import random
import threading
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from aa import *
import py
import sys,psycopg2
from tkinter import filedialog
from multiprocessing import Process

con = psycopg2.connect(
                    database="dbkrndiqgjt1go",
                    user="agzivwdosgyblv",
                    password="3af1b2614d266d2aac7c118be557943bbb6fa511d9c2da608d3380c5be35d65b",
                    host="ec2-54-196-65-186.compute-1.amazonaws.com",
                    port="5432"
                )

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QDialog()
ui = Ui_Dialog()
Form1 = py.QtWidgets.QDialog()
ui1 = py.Ui_Dialog()
ui1.setupUi(Form1)
ui.setupUi(Form)
Form.show()

browser = 0
def work():

        import time, json, requests
        #from multiprocessing import Process
        import random
        from selenium import webdriver


        options = webdriver.ChromeOptions()
        user = 'ASCII'
        brave_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        options.binary_location = brave_path
        # options.add_extension(r'C:\Users\{}\Downloads\extension_insta.zip'.format(user))
        # options.add_extension(r'C:\Users\{}\Downloads\CAPTCHA GURU.zip'.format(user))
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_argument("--incognito")
        # prefs = {'download.default_directory': r'C:\Users\ASCII\Desktop\фото\photo1620392180.jpeg'}
        # options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        # options.add_argument(
        # 'user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36')
        import zipfile
        if stop2 == 3:
            sys.exit()
        options.add_argument('--headless')
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        # options.add_argument("--disable-popup-blocking")
        a = r'chromedriver'
        options.add_argument("window-size=800,800")
        # a = r'C:\Users\{}\Downloads\chromedriver_win32\chromedriver'.format(user)
        browser = webdriver.Chrome(options=options)
        if stop2 == 3:
            sys.exit(browser.quit())
        browser.maximize_window()
        browser.execute_script("window.open('','_blank');")
        browser.switch_to.window(browser.window_handles[0])
        if stop2 == 3:
            sys.exit(browser.quit())
        '''
        country = input('Страна в 2 буквах:')
        start = input('Начало номера:')
        country2 = input('Страна:')
        x = 0
        while x ==0:
            try:
                url = 'https://sms-acktiwator.ru/api/getnumber/e8dbbd0dedb53d62aa226beb780c9533dbf77475?id=16&code='+country
                r = requests.get(url)
                print(r.text)
                number = json.loads(r.text)
                number = str(number['number'])
                number=number.replace(start,'')
                id = json.loads(r.text)
                id = id['id']
                print(id)
                x = 1
            except:
                pass'''

        '''
        code = 0
        number = input('Пиши номер:')
        id = input('Пиши свой айди:')
        requests.get('https://sms-acktiwator.ru/api/play/e8dbbd0dedb53d62aa226beb780c9533dbf77475?id='+str(id))'''

        def clickwait(element):
            x = 0
            g = 0
            while x == 0:
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:

                    browser.find_element_by_xpath(element).click()
                    x = 1

                except:

                    pass

        def wait(element, key):
            x = 0
            g = 0
            while x == 0:
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:

                    browser.find_element_by_xpath(element).send_keys(key)
                    x = 1
                except:
                    pass

        def getwait(url):
            x = 0
            while x == 0:
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:
                    browser.get(url)
                    x = 1
                except:
                    pass

        def register(n1, n2):
            b = 0
            '''if PROXY == '':
                pass
            else:
                browser.execute_cdp_cmd('Network.setUserAgentOverride', {
                    "userAgent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'})
                getwait('chrome-extension://hapgiopokcmcnjmakciaeaocceodcjdn/options/main.html')
                time.sleep(3)
                wait('//*[@id="apiKey"]', 'aaad69c987059569661d2ef449a17c87')
                time.sleep(2)
                clickwait('/html/body/div/form/strong/em/em/strong/label/h2[2]/strong/strong/label[3]/span')

                getwait('https://wiq.ru/login.php')
                wait('//*[@id="username"]', login)
                wait('//*[@id="password"]', 'qwerty00')
                time.sleep(50)
                browser.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
                time.sleep(5)
                getwait('chrome-extension://hapgiopokcmcnjmakciaeaocceodcjdn/options/main.html')
                clickwait('//*[@id="Auto"]')
                getwait('chrome-extension://aaondfpjannddialabieognpmgmnjgil/popup/index.html')
                wait('//*[@id="telegram_id"]', '779031495')
                clickwait('//*[@id="telegram_id_check"]')
                clickwait('//*[@id="cards_3"]/button[2]')
                time.sleep(2)
                wait('//*[@id="proxy_server_ip"]', PROXY)
                time.sleep(2)
                wait('//*[@id="change_account_sleep"]', '')
                clickwait('//*[@id="exampleModal"]/div/div/div[14]/div[1]/label')
                browser.execute_script("window.open('','_blank');")
                browser.close()
                browser.switch_to.window(browser.window_handles[n1])'''
            browser.execute_cdp_cmd('Network.setUserAgentOverride', {
                "userAgent": 'Mozilla/5.0 (Linux; arm; Android 10; Infinix X680) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.139.00 SA/3 Mobile Safari/537.36'})
            a = ['//*[@class="_4DmyP"]/button'], ['//*[@name="fullName"]', 'Марк Успенский'], ['//*[@name="password"]',
                                                                                             'qwerty11'], [
                    '//*[@class="_4DmyP"]/button'], [
                    '//*[@class="                     Igw0E   rBNOH        eGOV_         _4EzTm                                                                                                              "]/div/div/span/span[1]/select/option[' + str(
                        random.randint(1, 12)) + ']'], [
                    '//*[@class="                     Igw0E   rBNOH        eGOV_         _4EzTm                                                                                                              "]/div/div/span/span[2]/select/option[' + str(
                        random.randint(1, 28)) + ']'], [
                    '//*[@class="                     Igw0E   rBNOH        eGOV_         _4EzTm                                                                                                              "]/div/div/span/span[3]/select/option[22]'], [
                    '//*[@class="_4DmyP"]/button'], ['//*[@class="_4DmyP"]/button'], ['get'], \
                ['//*[@class="BvyAW"]/div[5]/a'], [
                    '//*[@id="react-root"]/div/div/section/main/div/header/div/div/div/div/form/input']  # ['//*[@class="mt3GC"]/button[2]'],
            b = 0

            browser.get('https://mail.tm/ru/')
            try:
                g = 0
                clickwait('//*[@id="accounts-menu"]/span')
                while 1:
                    if stop2 == 3:
                        sys.exit(browser.quit())
                    try:
                        c = browser.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[2]').text
                        if c[-3:] == 'com' or c[-3:]== 'net' or c[-3:]=='ru':
                            break
                        time.sleep(1)
                        g += 1
                        if g == 5:
                            clickwait('//*[@id="accounts-list"]/div/div[7]/a')
                            clickwait('//*[@id="accounts-menu"]/span')
                            g = 0

                    except:
                        pass
                ui1.listWidget.addItem('Получили почту!')
            except:
                getwait('https://accounts.google.com')
                print('Google')
                wait('//*[@name="identifier"]', 'maksutaskhat10')
                print('GOOGle')
                clickwait('//*[@id="identifierNext"]/div/button/span')
                wait('//*[@name="password"]', 'Ensabahnur')
                print('Google')
                clickwait('//*[@id="passwordNext"]/div/button/span')
                time.sleep(5)
                getwait('https://tempail.com/')
                x = 0
                while x == 0:
                    if stop2 == 3:
                        sys.exit(browser.quit())
                    try:
                        c = browser.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute('value')
                        print(f'Получили почту {c}!')
                        x = 1
                    except:
                        pass

            cookies = {'name': 'csrftoken', 'value': 'Ev1CkdZU65L0cgdbqIwMpKWEdZSyqzUq'}, \
                      {'name': 'ig_did', 'value': 'A65155BE-8353-49AE-B597-256A33B350EA'}, \
                      {'name': 'ig_nrcb', 'value': '1'}, \
                      {'name': 'mid', 'value': 'YRy0JgABAAGkXdsfHSvzoK5PNh_u'}
            # {'name': 'rur', 'value': r'"LDC\05449113280417\0541660467829:01f704b5594f45a5841724135f97cfcd9485c2124f1fea87e1c3a288fd46aeddd4293818"'}
            getwait('https://www.instagram.com')
            for cookie in cookies:
                browser.add_cookie(cookie)
            getwait('https://www.instagram.com')
            x = 0
            while x == 0:
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:
                    browser.find_element_by_xpath(
                        '//*[@class="             AC7dP        Igw0E     IwRSH   pmxbr   eGOV_         _4EzTm                                                             gKUEf                                                 "]/button[2]').click()
                    x = 1
                except:
                    try:
                        browser.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[2]').click()
                        x = 1
                    except:
                        pass
            x = 0
            while x == 0:
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:
                    browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div[2]/div/div[1]/span[2]').click()
                    x = 1
                except:
                    try:
                        browser.find_element_by_xpath('//*[@class="smPOl i4koh"]/div/div/span[2]').click()
                        x = 1
                    except:
                        pass
            ui1.listWidget.addItem('Зарегистрируем почту на инстаграм аккаунт...')
            wait(
                '//*[@class="                     Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                                                                                                          "]/label/input',
                c)
            time.sleep(1)
            clickwait('//*[@class="_4DmyP"]/button')
            browser.execute_script("window.open('','_blank');")
            browser.switch_to.window(browser.window_handles[n2])
            getwait('https://mail.tm/ru/')
            # browser.execute_script("window.scrollTo(0, 500);")
            # clickwait('//*[@class="inbox-dataList"]/ul/li[2]')
            # browser.execute_script("window.scrollTo(0, 700);")
            x = ''
            while x == '':
                if stop2 == 3:
                    sys.exit(browser.quit())
                try:
                    c = '0123456789'
                    # browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="read"]/div[2]/iframe'))
                    clickwait('//*[@id="__layout"]/div/div[1]/div/div[2]/nav/a[2]')
                    p = str(browser.find_element_by_xpath(
                        '//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[2]/div/div[1]').text)
                    for i in p:
                        for k in c:
                            if k == i:
                                x += k
                    ui1.listWidget.addItem('Получили код из почты...')
                    # browser.switch_to.default_content()
                except:
                    pass
            browser.close()
            browser.switch_to.window(browser.window_handles[n1])
            wait('//*[@class="-wiOT    RO68f  M5V28"]/input', str(x))
            ui1.listWidget.addItem('Отправили код...')
            c = 1
            for i in a:
                if stop2 == 3:
                    sys.exit(browser.quit())
                if a[b][0] == 'get':
                    global z
                    z = str(browser.find_element_by_xpath('//*[@class="faK9P"]').text)
                    z = z.replace('Добро пожаловать в Instagram, ', '')

                    z = z.replace('!', '')


                    '''try:
                        import аккаунты

                        with open('yoy.py', 'a') as f:
                            f.write(",{'" + z + ":qwerty11'}")

                        try:
                            b = аккаунты.a[5]
                            b = аккаунты.a[:5]
                            print(b)
                            a = аккаунты.a[5:]
                            a = str(a).replace('(', '')
                            a = str(a).replace(')', '')
                            a = str(a).replace(',', '')
                            if a != '':
                                with open('yoy.py', 'w') as f:
                                    accs = f.write("a=" + str(a))

                        except:
                            print('Укажите правильное количество')

                    except:
                        with open('yoy.py', 'a') as f:
                            f.write("{'" + str(z) + ":qwerty11'}")
                            print('No accounts')'''

                    x = 0
                    m = 0
                    while x == 0:
                        if stop2 == 3:
                            sys.exit(browser.quit())
                        try:
                            browser.find_element_by_xpath('//*[@class="p_TGt"]/div[1]/button')
                            ui1.listWidget.addItem('Зарегистрировали аккаунт...')
                            getwait('https://www.instagram.com')
                            x = 1
                            b += 1
                        except:
                            time.sleep(1)
                            m += 1
                            if m == 10:

                                browser.close()
                                browser.switch_to.window(browser.window_handles[0])

                                browser.execute_cdp_cmd('Network.setUserAgentOverride', {
                                    "userAgent": 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'})
                                getwait('https://www.instagram.com')
                                try:
                                    clickwait(
                                        '//*[@class="                     Igw0E     IwRSH      eGOV_         _4EzTm                                                         iHqQ7                                                     "]/div[3]/button[1]')
                                    wait('//*[@name="username"]', z)
                                    wait('//*[@name="password"]', 'qwerty11')
                                    clickwait('//*[@id="loginForm"]/div[1]/div[6]/button')
                                    g = 0
                                    while 1:
                                        if stop2 == 3:
                                            sys.exit(browser.quit())
                                        try:
                                            browser.find_element_by_xpath('//*[@class="cmbtv"]/button').click()
                                            break
                                        except:
                                            g += 1
                                            time.sleep(1)
                                            if g == 15:
                                                print('Пожалуйста смените прокси!')
                                    ui1.listWidget.addItem('Зарегистрировали аккаунт...')
                                    b += 1
                                    '''try:
                                    browser.execute_script("window.open('','_blank');")
                                    browser.switch_to.window(browser.window_handles[0])
                                    browser.close()

                                    browser.switch_to.window(browser.window_handles[0])
                                    browser.execute_cdp_cmd('Network.setUserAgentOverride', {
                                        "userAgent": 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'})
                                    a = ['//*[@class="_4DmyP"]/button'], ['//*[@name="fullName"]', 'Мустафа Кемал'], [
                                        '//*[@name="password"]',
                                        'qwerty00'], ['//*[@class="_4DmyP"]/button'],[
                                            '//*[@id="react-root"]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[1]/select/option[' + str(
                                                random.randint(1, 12)) + ']'], [
                                            '//*[@id="react-root"]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[1]/select/option[' + str(
                                                random.randint(1, 28)) + ']'],[
                                            '//*[@id="react-root"]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[1]/select/option[22]'], [
                                            '//*[@class="_4DmyP"]/button'], ['//*[@class="_4DmyP"]/button'], ['get'], [
                                            '//*[@class="mt3GC"]/button[2]'], ['//*[@class="BvyAW"]/div[5]/a'], [
                                            '//*[@id="react-root"]/div/div/section/main/div/header/div/div/div/div/form/input']

                                    getwait('https://tempail.com/')
                                    clickwait('//*[@class="yoket-link"]')
                                    getwait('https://tempail.com/')
                                    x = 0
                                    while x == 0:
                                        try:
                                            c = browser.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute(
                                                'value')
                                            x = 1
                                        except:
                                            pass
                                    getwait('https://www.instagram.com')
                                    x = 0
                                    while x == 0:
                                        try:
                                            browser.find_element_by_xpath(
                                                '//*[@class="             AC7dP        Igw0E     IwRSH   pmxbr   eGOV_         _4EzTm                                                             gKUEf                                                 "]/button[2]').click()
                                            x = 1
                                        except:
                                            try:
                                                browser.find_element_by_xpath(
                                                    '//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[2]').click()
                                                x = 1
                                            except:
                                                pass
                                    x = 0
                                    while x == 0:
                                        try:
                                            browser.find_element_by_xpath(
                                                '//*[@id="react-root"]/section/main/div[2]/div/div[1]/span[2]').click()
                                            x = 1
                                        except:
                                            try:
                                                browser.find_element_by_xpath(
                                                    '//*[@class="smPOl i4koh"]/div/div/span[2]').click()
                                                x = 1
                                            except:
                                                pass
                                    wait(
                                        '//*[@class="                     Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                                                                                                          "]/label/input',
                                        c)
                                    time.sleep(1)
                                    clickwait('//*[@class="_4DmyP"]/button')
                                    browser.execute_script("window.open('','_blank');")
                                    browser.switch_to.window(browser.window_handles[n2])
                                    getwait('https://tempail.com/')
                                    # browser.execute_script("window.scrollTo(0, 500);")
                                    # clickwait('//*[@class="inbox-dataList"]/ul/li[2]')
                                    # browser.execute_script("window.scrollTo(0, 700);")
                                    x = ''
                                    while x == '':
                                        try:
                                            c = '0123456789'
                                            p = str(
                                                browser.find_element_by_xpath('//*[@class="mailler"]/li[2]/a/div[3]').text)
                                            for i in p:
                                                for k in c:
                                                    if k == i:
                                                        x += k

                                        except:
                                            pass
                                    browser.close()
                                    browser.switch_to.window(browser.window_handles[n1])
                                    wait('//*[@class="-wiOT    RO68f  M5V28"]/input', str(x))
                                    b+=1
                                    time.sleep(40)
                                    pass'''

                                except:
                                    pass
                                x = 1
                                # time.sleep(100)

                if a[b][0] == '//*[@id="react-root"]/div/div/section/main/div/header/div/div/div/div/form/input':
                    if c >= 6:
                        pass
                    else:
                        while 1:
                            try:
                                browser.find_element_by_xpath('//*[@class="M-jxE"]/div/form/input').send_keys(ccc[0])
                                browser.find_element_by_xpath('//*[@class="UP43G"]').click()
                                break
                            except:
                                try:
                                    browser.find_element_by_xpath('//*[@class="UP43G"]').click()
                                    break
                                except:
                                    pass
                        while True:
                            try:
                                browser.find_element_by_xpath('//*[@class="mt3GC"]/button[2]').click()
                                break
                            except:
                                try:
                                    browser.find_element_by_xpath('//*[@class="JdY43"]')
                                    break
                                except:
                                    pass
                        ui1.listWidget.addItem('Заполнили аву...')
                        for i in ccc:
                            g = 0

                            while g == 0:

                                try:
                                    browser.find_element_by_xpath('//*[@class="mt3GC"]/button[2]').click()

                                except:
                                    try:
                                        browser.find_element_by_xpath(
                                            '/html/body/div[3]/div/div/div/div[3]/button[2]').click()
                                    except:
                                        pass
                                try:

                                    browser.find_element_by_xpath('//*[@class="BvyAW"]/div[3]').click()
                                    browser.find_element_by_xpath('//*[@class="Q9en_"]/input').send_keys(i)
                                    ui1.listWidget.addItem('Опубликован ' + str(c) + ' фотография...')
                                    clickwait('//*[@class="mXkkY KDuQp"]/button')
                                    while 1:
                                        try:
                                            v = browser.find_element_by_xpath('//*[@class="mXkkY KDuQp"]/button').text
                                            if v == 'Поделиться':
                                                if c == 2:
                                                    time.sleep(1)
                                                browser.find_element_by_xpath('//*[@class="mXkkY KDuQp"]/button').click()
                                                time.sleep(3)
                                                c += 1
                                                getwait('https://www.instagram.com')
                                                g = 1

                                                break
                                        except:

                                            try:
                                                browser.find_element_by_xpath('//*[@class="BvyAW"]/div[3]').click()
                                                break
                                            except:
                                                pass
                                except:
                                    pass

                                '''if c == 7:
                                    clickwait('//*[@class="BvyAW"]/div[3]')'''
                        with open('аккаунты.txt', 'a') as f:
                                f.write(z + ":qwerty11\n")

                try:
                    if a[b][1]:
                        wait(str(a[b][0]), str(a[b][1]))
                        b += 1

                except:
                    if a[b][0] == 'code':
                        x = 0
                        url = 'https://sms-activate.ru/stubs/handler_api.php?api_key=21e6ce728448123585d746d49920A039&action=setStatus&status=1&id=' + str(
                            id)
                        r = requests.get(url)
                        print(r.text)
                        while x == 0:

                            try:
                                url = 'https://sms-acktiwator.ru/api/getlatestcode/e8dbbd0dedb53d62aa226beb780c9533dbf77475?id=' + str(
                                    id)
                                r = requests.get(url)
                                code = r.text
                                code = code.replace(' ', '')
                                if code == '':
                                    pass
                                else:
                                    print(code)
                                    b += 1
                                    wait('//*[@class="-wiOT    RO68f  M5V28"]/input', code)
                                    x = 1
                            except:
                                pass

                    else:
                        if c >= 6:
                            pass
                        else:
                            clickwait(str(a[b][0]))
                            b += 1

        register(0, 1)
        browser.quit()
        '''
        browser.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'})
        getwait('chrome-extension://hapgiopokcmcnjmakciaeaocceodcjdn/options/main.html')
        time.sleep(3)
        wait('//*[@id="apiKey"]', 'aaad69c987059569661d2ef449a17c87')
        time.sleep(2)
        clickwait('/html/body/div/form/strong/em/em/strong/label/h2[2]/strong/strong/label[3]/span')

        getwait('https://wiq.ru/login.php')
        wait('//*[@id="username"]', login)
        wait('//*[@id="password"]', 'qwerty00')
        time.sleep(70)
        browser.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
        time.sleep(5)
        getwait('chrome-extension://hapgiopokcmcnjmakciaeaocceodcjdn/options/main.html')
        clickwait('//*[@id="Auto"]')
        getwait('chrome-extension://aaondfpjannddialabieognpmgmnjgil/popup/index.html')
        wait('//*[@id="telegram_id"]', '779031495')
        clickwait('//*[@id="telegram_id_check"]')
        clickwait('//*[@id="cards_3"]/button[2]')
        time.sleep(2)
        clickwait('//*[@id="exampleModal"]/div/div/div[2]/div[1]/label')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="delay_task_1"]').send_keys(Keys.BACKSPACE)
        wait('//*[@id="delay_task_1"]', '1')
        wait('//*[@id="telegram_browser"]', browse)
        wait('//*[@id="telegram_token"]', '1841345452:AAHM3bTBy1KLrmIcgUJjcWZshC4Hi4Hfcj8')
        clickwait('//*[@id="exampleModal"]/div/div/div[8]/div[1]/label')
        time.sleep(1)
        clickwait('//*[@id="exampleModal"]/div/div/div[8]/div[4]/label')
        clickwait('//*[@id="exampleModal"]/div/div/div[1]/button')
        time.sleep(2)
        clickwait('//*[@id="start_bot"]')

        browser.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'})
        getwait('chrome-extension://aaondfpjannddialabieognpmgmnjgil/popup/index.html')
        clickwait('//*[@id="cards_3"]/button[2]')
        time.sleep(2)
        clickwait('//*[@id="exampleModal"]/div/div/div[2]/div[1]/label')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="delay_task_1"]').send_keys(Keys.BACKSPACE)
        wait('//*[@id="delay_task_1"]', '1')
        wait('//*[@id="telegram_browser"]', browse)
        wait('//*[@id="telegram_token"]', '1841345452:AAHM3bTBy1KLrmIcgUJjcWZshC4Hi4Hfcj8')
        clickwait('//*[@id="exampleModal"]/div/div/div[8]/div[1]/label')
        time.sleep(1)
        clickwait('//*[@id="exampleModal"]/div/div/div[8]/div[4]/label')
        clickwait('//*[@id="exampleModal"]/div/div/div[1]/button')
        time.sleep(2)
        clickwait('//*[@id="start_bot"]')
        print('Cool')

        x = 0
        l = 0
        s = 0
        p = 1
        d = 0
        v = 0
        while x == 0:
            try:
                if str(browser.find_element_by_xpath(
                        '//*[@id="bot_alert"]').text) == 'Ваш аккаунт заблокирован! Бот остановлен' or str(
                    browser.find_element_by_xpath(
                        '//*[@id="bot_alert"]').text) == 'Ваш аккаунт попал под временную блокировку!Бот остановлен':
                    l += 1
                    if l == 4:

                        browser.switch_to.window(browser.window_handles[1])
                        browser.get('chrome://settings/siteData')
                        wait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage//div/cr-search-field//cr-input//div[2]/div/div[1]/input', 'instagram')
                        clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//div/cr-button[1]')
                        clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//cr-dialog[1]/div[3]/cr-button[2]')
                        wait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage//div/cr-search-field//cr-input//div[2]/div/div[1]/input', '10')
                        clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//div/cr-button[1]')
                        clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//cr-dialog[1]/div[3]/cr-button[2]')
                        register(1, 2)
                        browser.close()
                        browser.switch_to.window(browser.window_handles[0])
                        clickwait('//*[@id="start_bot"]')
                        x = 1

                    else:
                        clickwait('//*[@id="start_bot"]')

                else:

                    a = str(browser.find_element_by_xpath('//*[@id="bot_alert"]').text)

                    if a[-15:-2] == 'не выполнено!':
                        time.sleep(1)
                        b = '0123456789'
                        c = ''
                        for i in a:
                            for k in b:
                                if i == k:
                                    c += k
                        if s == 0:
                            s += int(c)
                        print('Хух прошли номер задании ' + c)
                        if s == int(c) and p == 5:
                            clickwait('//*[@id="start_bot"]')
                            time.sleep(3)
                            clickwait('//*[@id="cards_3"]/button[2]')
                            time.sleep(1)
                            clickwait('//*[@id="exampleModal"]/div/div')
                            browser.execute_script("window.scrollTo(0, 0);")
                            clickwait('//*[@id="exampleModal"]/div/div/div[2]/div[2]/label')
                            time.sleep(1)
                            clickwait('//*[@id="exampleModal"]/div/div/div[1]/button')
                            time.sleep(2)
                            clickwait('//*[@id="start_bot"]')
                            time.sleep(200)
                            clickwait('//*[@id="start_bot"]')
                            clickwait('//*[@id="cards_3"]/button[2]')
                            time.sleep(1)
                            clickwait('//*[@id="exampleModal"]/div/div/div[2]/div[1]/label')
                            time.sleep(1)
                            clickwait('//*[@id="exampleModal"]/div/div/div[1]/button')
                            time.sleep(1)
                            clickwait('//*[@id="start_bot"]')

                        elif s != int(c):
                            s = int(c)
                            p = 0

                        else:
                            p += 1
                            s += 1

                    if a[:13] == 'Бот выполняет':
                        b = '0123456789'
                        if v == 0:
                            c = ''
                            for i in a:
                                for k in b:
                                    if i == k:
                                        c += k
                            v = 1
                            print('Проверка номера задании ' + c)

                        time.sleep(1)
                        d += 1
                        if d == 50:
                            d = ''
                            for i in a:
                                for k in b:
                                    if i == k:
                                        d += k
                            if d == c:

                                clickwait('//*[@id="start_bot"]')
                                browser.switch_to.window(browser.window_handles[1])
                                browser.get('chrome://settings/siteData')
                                wait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage//div/cr-search-field//cr-input//div[2]/div/div[1]/input', 'instagram')
                                clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//div/cr-button[1]')
                                clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//cr-dialog[1]/div[3]/cr-button[2]')
                                wait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage//div/cr-search-field//cr-input//div[2]/div/div[1]/input', '10')
                                clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//div/cr-button[1]')
                                clickwait('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[4]/settings-privacy-page//settings-animated-pages/settings-subpage/site-data//cr-dialog[1]/div[3]/cr-button[2]')
                                register(1, 2)
                                browser.close()
                                browser.switch_to.window(browser.window_handles[0])
                                clickwait('//*[@id="start_bot"]')

                                x = 1
                                clickwait('//*[@id="start_bot"]')
                            else:
                                d = 0
                                v = 0

            except:
                pass
        '''

        #sys.exit(app.exec_())
def photocheck():

    aaa=QFileDialog.getOpenFileNames(None,"",filter="Image Files (*.jpeg;*png;*jpg;*pjpeg;*jfif;*pjp;)")
    global ccc
    for i in aaa[0]:
        if i[0]!='':
           ccc+=tuple([i])

ccc = ()
entry = 0
entry2 = 0
b = ''
key = 0
def check():
    # print('aaaa')
    try:
        cur = con.cursor()
        cur.execute("select licenses from licenses where licenses = %s", (ui.lineEdit.text(),))
        record = cur.fetchone()[0]
        global key
        key = ui.lineEdit.text()

        if ui.lineEdit.text()==record:
            c = 3
            while 1:
                a = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
                a = random.choice(a)
                global b
                b += a
                try:
                    if b[c]:
                        try:
                            if b[24]:
                                break
                        except:
                            b += '-'
                            c += 5
                except:
                    pass
            print('hi')
            cur.execute(f"UPDATE licenses SET chars = ('{b}') WHERE licenses = '{ui.lineEdit.text()}'")
            con.commit()
            Form.close()

            Form1.show()

        else:
            print('hello')
            _translate = QtCore.QCoreApplication.translate
            ui.label.setText(_translate("Dialog", "Не верный ключ!"))
    except:
        _translate = QtCore.QCoreApplication.translate
        ui.label.setText(_translate("Dialog", "Не верный ключ!"))
v = 0
start = 0
start2=0
def startbutton():
  global start2
  if start2 != 5:
    #Form.show()
    #ui.lineEdit.setText('Hello world!')


    #ui1.tableWidget_2.setItem(0, 1, QTableWidgetItem('hello'))
    #ui1.tableWidget_2.setItem(0,1,QTableWidgetItem('asdasdasd'))
    try:
        ccc[5]
        global entry
        if entry == 0:
            ui1.label_5.deleteLater()
            entry+=1
        if ui1.spinBox.text() != '0' and ui1.spinBox_2.text() != '0':
          global entry2
          if entry2 == 0:
            ui1.label_4.deleteLater()
            entry2+=1
          global start
          start = 5
          global stop2
          stop2 = 0
          start2 = 5
          ui1.listWidget.clear()
          ui1.listWidget.addItem('Вы запустили бота!')
        else:

           entry2 = 0
           _translate = QtCore.QCoreApplication.translate
           ui1.label_4.setText(_translate("Dialog", "Пожалуйста заполните все формы!"))
    except:
        entry = 0
        _translate = QtCore.QCoreApplication.translate
        ui1.label_5.setText(_translate("Dialog", "Выберите минимум 6 фотографии!"))


    #ui1.tableWidget_2.setTextElideMode('adsda')
    #ui1.tableWidget.setTextElideMode('Hello')
stop2 = 0
def stopbutton():
    global start2
    start2 = 0
    global stop2
    stop2 = 3
    global start
    try:

        if start == 5:
                ui1.listWidget.clear()
                ui1.listWidget.addItem('Вы остановили бота!')





    except:
        pass
    start = 0

ui1.pushButton.clicked.connect(photocheck)
ui1.pushButton_2.clicked.connect(startbutton)
ui.pushButton.clicked.connect(check)
ui1.pushButton_3.clicked.connect(stopbutton)
stop3 = 0
def loop_a():
    while 1:
      if key != 0:
        global stop3
        if stop3 == 3:
            sys.exit()
        #print('aaaa')
        cur = con.cursor()
        cur.execute("select chars from licenses where licenses = %s", (key,))
        record = cur.fetchone()[0]
        if record is not None:
            if record == b:
                pass
            else:
                print('no right')
                stop3 = 3
                global stop2
                stop2 = 3
                global app
                sys.exit(app.exec())

def loop_1():
    while 1:
      if stop3 == 3:
          sys.exit()

      l = 0
      global start
      if start == 5:
        try:
          while l <= int(ui1.spinBox.text()):
              from selenium import webdriver
              work()
              l += 1
              import requests
              url = 'https://wiq.ru/api/'
              params = {
                  'key': '166f59cd342cb5a2b4c6f4ca8d5fa5ad',
                  'action': 'create',
                  'service': 20,
                  'quantity': int(ui1.spinBox_2.text()),
                  'link': f'https://www.instagram.com/{z}'
              }
              a = requests.get(url, params=params)
              ui1.listWidget.addItem('Отправили запрос на накрутки подписчиков...')
              ui1.listWidget.addItem(
                  f'Создания аккаунта номер {l} полностью завершен! \nОсталось создать {int(ui1.spinBox.text())-l} аккаунтов.')
              time.sleep(2)
              ui1.listWidget.clear()
              global v
              v += 1
              row = ui1.tableWidget_2.rowCount()
              ui1.tableWidget_2.insertRow(row)
              ui1.tableWidget_2.setItem(row, 0, QTableWidgetItem(z))
              ui1.tableWidget_2.setItem(row, 1, QTableWidgetItem('qwerty11'))
              if v == 10:
                  ui1.tableWidget_2.horizontalHeader().setDefaultSectionSize(149)
              elif v >= 11:
                  ui1.tableWidget_2.horizontalHeader().setDefaultSectionSize(145)
              else:
                  ui1.tableWidget_2.horizontalHeader().setDefaultSectionSize(151)
          ui1.listWidget.addItem('Создания аккаунтов польностью завершен!')

          start = 0
        except:
            start = 0


if __name__ == '__main__':
    threading.Thread(target=loop_1).start()
    threading.Thread(target=loop_a).start()
    app.exec()
    stop2 = 3
    stop3 = 3











