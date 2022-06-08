from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PHONE = '1234567890'  # 手机号
PWD = 'xxxxxxxxxxxxx'  # 密码

# 关闭代理与无用chrome.exe，按需屏蔽
os.system(r'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
os.system('taskkill /f /im chrome.exe')
os.system('taskkill /f /im spider.exe')

chrome_options = Options()
chrome_options.add_experimental_option('w3c', True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
chrome_options.binary_location = r"C:\Program Files (x86)\Tencent\QQBrowser\chrome.exe"
wd = webdriver.Chrome(r'C:\Program Files (x86)\Tencent\QQBrowser\chromedriver.exe', options=chrome_options)
ac = ActionChains(wd)

print('开始运行')
wd.get('https://www.yibanyun.cn/yibiaodan/yibiaodan/join/id/240.html')  # 原166

while True:
    try:
        wd.implicitly_wait(6)
        wd.find_element(By.CSS_SELECTOR, 'input[id="account-txt"]').send_keys(PHONE)
        wd.find_element(By.CSS_SELECTOR, 'input[id="password-txt"]').send_keys(PWD)
        sleep(0.2)
        wd.find_element(By.CSS_SELECTOR, 'a[id="login-btn"]').click()
        print('登录成功')
        sleep(8)
        break
    except Exception:
        wd.execute_script("window.open('https://www.yibanyun.cn/yibiaodan/yibiaodan/join/id/216.html')")
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        sleep(5)


try:
    ok = wd.find_elements(By.CSS_SELECTOR, 'button[class="submitBtn oauth_check"]')
    if ok:
        ok[0].click()
        sleep(3)
    # 这里老版本驱动问题导致判定很迷，所以用这种笨方法
    try:
        area = WebDriverWait(wd, 6, 0.2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请选择地区"]')))
    except TimeoutException:
        area = wd.find_element(By.CSS_SELECTOR, 'input[placeholder="请选择地区"]')
    try:
        area.click()
    except Exception:
        pass
    try:
        area.send_keys(Keys.ENTER)
    except Exception:
        pass
    try:
        wd.execute_script("arguments[0].click();", area)
    except Exception:
        pass
    WebDriverWait(wd, 6, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="mui-poppicker mui-active"]')))
    wd.implicitly_wait(6)
    area1 = wd.find_elements(By.XPATH, '//div[@class="mui-picker"][1]//li')
    print('定位1：成功')
    sleep(1)
    for i in range(19):
        area1[1+i].click()
        sleep(0.3)
    area2 = wd.find_elements(By.XPATH, '//div[@class="mui-picker"][3]//li')
    print('定位2：成功')
    for i in range(6):
        area2[1+i].click()
        sleep(0.3)
    wd.find_element(By.XPATH, '//button[contains(text(),"确定")]').click()
    sleep(1)
    wd.find_element(By.CSS_SELECTOR, 'input[value="体温正常"]').click()
    # wd.find_element(By.CSS_SELECTOR, 'input[value="否"]').click()
    wd.find_elements(By.CSS_SELECTOR, 'input[value="是"]')[0].click()  # 新增
    wd.find_elements(By.CSS_SELECTOR, 'input[value="否"]')[1].click()  # 新增
    for i in range(2):
        green = wd.find_elements(By.CSS_SELECTOR, 'input[value="绿色"]')[i]
        wd.execute_script("arguments[0].click();", green)
    for i in range(5):
        no = wd.find_elements(By.CSS_SELECTOR, 'input[value="无"]')[i]
        wd.execute_script("arguments[0].click();", no)
    wd.find_element(By.CSS_SELECTOR, 'textarea[name="form_item_val_13"]').send_keys(' ')  # 原12
    submit = wd.find_element(By.CSS_SELECTOR, 'input[name="submit_btn"]')
    try:
        submit.click()
    except Exception:
        pass
    try:
        submit.send_keys(Keys.ENTER)
    except Exception:
        pass
    try:
        wd.execute_script("arguments[0].click();", submit)
    except Exception:
        pass
    print('打卡成功')
except Exception as result:
    if wd.find_elements(By.XPATH, '//h4[text()="您已经达到每天提交次数"]'):
        print('已经打过卡了')
        input('（回车结束程序）\n')
    else:
        print(result)
        print('打卡失败或出错,请重开')
        input('（回车结束程序）\n')

sleep(5)
wd.quit()
