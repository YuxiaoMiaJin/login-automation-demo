
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_login(username, password):
# 初始化 Chrome 浏览器
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开测试页面
        driver.get("https://the-internet.herokuapp.com/login")

    # 输入用户名和密码
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)

    # 点击登录按钮
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    # 等待页面跳转
        time.sleep(10)

    # 获取提示信息并验证
        message = driver.find_element(By.ID, "flash").text
        if "You logged into a secure area!" in message:
            print("登录成功！")
        else:
            print("登录失败，提示信息为：",message)
            raise AssertionError("登录失败，断言失败！")
        time.sleep(10)
        driver.quit()

        #assert "You logged into a secure area!" in message

        #print("登录测试成功！")

        # 关闭浏览器
    except Exception as e:
        print("执行过程中出错：",e)
    try:
        driver.quit()
    except:
       pass
if __name__ == "__main__":
    test_login("tomsmith", "SuperSecretPassword!")
    test_login("tomsmith", "WrongPassword!")

