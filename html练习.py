#任务1：百度自由搜索
from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("http://www.baidu.com")

# 窗口最大化
chromeDriver.maximize_window()

#寻找搜索输入框
chromeDriver.find_element_by_id("kw").send_keys("java")

# 点击百度一下按钮
chromeDriver.find_element_by_id("su").click()

time.sleep(3)
# 退出浏览器
chromeDriver.quit()

#任务2：滑动验证其他的都用自动化来做
#上传文件和下拉列表
driver = webdriver.Chrome()
driver.get(r"D:\Python自动化测试\自动化测试\day01\练习的html\上传文件和下拉列表/autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("哈哈哈")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\360downloads\阿狸.jpeg")
driver.find_element_by_xpath("//*[@id='buttonID']").click()

#弹框的验证

driver.get(r"D:\Python自动化测试\自动化测试\day01\练习的html\弹框的验证/dialogs.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='confirm']").click()
driver.switch_to.alert.dismiss() # 取消
#driver.switch_to.accept.dismiss()#确定

#跳转页面

driver = webdriver.Chrome()
driver.get(r"D:\Python自动化测试\自动化测试\day01\练习的html\跳转页面/pop.html")
driver.maximize_window()
sreach_windows = driver.current_window_handle  #获得当前窗口句柄
driver.find_element_by_xpath("//*[@id='goo']").click()

all_handles = driver.window_handles  #返回所有窗口的句柄到当前会话
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle) #用于切换到相应的窗口
        driver.find_element_by_id("kw").send_keys("java")
        driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()

#任务3：京东搜索一个商品，点击详情
driver = webdriver.Chrome()
driver.get("http://www.JD.com")
driver.maximize_window()
sreach_windows = driver.current_window_handle  #获得当前窗口句柄
driver.find_element_by_xpath("//*[@id='key']").send_keys("iphone13")
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button").click()
time.sleep(10)
driver.quit()