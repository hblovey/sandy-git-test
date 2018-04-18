#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Pageinfo import get_pageinfo
from Userinfo import get_userinfo
from Emailinfo import get_emailinfo
from Getfilepath import get_path
from Report import Log
from Sendemail import send_email
from yanzhengma import *
from PIL import Image
import pytesseract


def open_browser():
    handle=webdriver.Firefox()
    return handle

def get_url(handle,arg):
    handle.maximize_window()
    handle.get(arg['url'])
    handle.implicitly_wait(5)
#    time.sleep(3)
#点击登陆按钮
def click_button(handle,arg):
    handle.find_element_by_xpath(arg['login_xpath']).click()
    time.sleep(1)




#获取页面元素
def get_element(handle,arg):
    userEle=handle.find_element_by_id(arg['user_id'])
    pwdEle=handle.find_element_by_id(arg['pwd_id'])
    loginEle=handle.find_element_by_id(arg['login_id'])
#    photoinputEle = handle.find_element_by_xpath(arg['photoinput_xpath'])
    return userEle,pwdEle,loginEle,#photoinputEle
#输入账号密码
def send_keys(elelist,arg):
    keyword=['user','password']
    i=0
    for key in keyword:
        elelist[i].clear()
        elelist[i].send_keys(arg[key])
        i+=1

    time.sleep(2)


#判断是否有验证码
def isElementExist(handle,element):
    flag = True
    try:
        handle.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        return flag

def save_photo_and_send(handle):
    #保存验证码图片
    handle.save_screenshot('C:\\Users\LENOVO\\PycharmProjects\\autotest\\XIAOMI\\abc.png')  # 截取当前网页，该网页有我们需要的验证码
    imgelement = handle.find_element_by_xpath(".//*[@id='captcha-img']")  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (
        int(location['x']), int(location['y']), int(location['x'] + size['width']),
        int(location['y'] + size['height']))
    # 写成我们需要截取的位置坐标
    i = Image.open("C:\\Users\LENOVO\\PycharmProjects\\autotest\\XIAOMI\\abc.png")  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('C:\\Users\LENOVO\\PycharmProjects\\autotest\\XIAOMI\\abcd.png')
    photoresult= photoshibie()
    print photoresult
    print 'photoresult:%s' ,'photoresult'
    handle.find_element_by_xpath(".//*[@id='captcha-code']").clear()
    handle.find_element_by_xpath(".//*[@id='captcha-code']").send_keys(photoresult)
#点击登录
def login01(elelist):
        elelist[2].click()
#判断并生成测试报告
def check_result(handle,arg,log,arg2):
    try:
        re=False
        Error=handle.find_element_by_xpath(".//*[@id='login-main-form']/div/div[4]/div/span")
        log.log_write('username:%s pwd:%s photofail:%s'%(arg2['user'],arg2['password'],Error.text))
        print ('验证码失败')
        Error1=handle.find_element_by_xpath(arg['error_xpath'])
        log.log.log_write('username:%s pwd:%s loginfail:%s'%(arg2['user'],arg2['password'],Error1.text))
        print('登陆失败')
    except:
        re=True
        log.log_write('username:%s pwd:%s pass'%(arg2['user'],arg2['password']))
        print('登陆成功')
    return re
#退出登录
def login_out(handle,arg):
    ele=handle.find_element_by_class_name(arg['logout_class'])
    ActionChains(handle).move_to_element(ele).perform()
    handle.find_element_by_link_text('退出登录').click()
    time.sleep(5)

def close_browse(handle):
    time.sleep(3)
    handle.quit()


if __name__=='__main__':
#获取信息
    email_path=r'.\emailMsg.txt'
    page_path=r'.\PageMsg.csv'
    file_path = r'.\Log'
    page_dict=get_pageinfo(page_path)
    user_list=get_userinfo()
    email_dict=get_emailinfo(email_path)
    email_path=get_path(file_path)
#执行用例
    d=open_browser()
    get_url(d,page_dict)
    click_button(d,page_dict)

    elelist=get_element(d,page_dict)
    log = Log()
    for i in user_list:
        send_keys(elelist,i)
        flag = isElementExist(d,".//*[@id='captcha-code']")
        if flag:
            save_photo_and_send(d)
        login01(elelist)
        re=check_result(d,page_dict,log,i)
        #if re:#如果登陆成功就退出登陆，重新输入账号密码
         #   login_out(d,page_dict)
         #   click_button(d,page_dict)
         #   elelist = get_element(d, page_dict)
         #   time.sleep(2)
    log.log_close()
    close_browse(d)
    #send_email(email_dict,email_path)


