from selenium import webdriver


class SeleniumDemo(object):
    def __init__(self):
        self.login_url = 'http://127.0.0.1:8000/admin/login/'
        self.list_product_url = 'http://127.0.0.1:8000/admin/employee/product/'
        self.add_employee_url = 'http://127.0.0.1:8000/admin/employee/employee/add/'
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get(self.login_url)
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
        username.send_keys('admin')
        password.send_keys('123456')
        submit.click()

    def query_product(self):
        if self.browser.current_url != self.add_employee_url:
            self.browser.get(self.add_employee_url)

    def add_employee(self):
        # 若因为网速原因页面尚未跳转成功，就开始获取元素，将导致获取不到元素，此种情况发生概率较高，此时有两种解决方法：
        # 1. 线程 sleep 一定时间之后再获取元素，除了给客户演示项目操作之外，其它时候均不推荐此做法
        # 2. 判断浏览器地址栏地址是否发生变化，若地址尚未变为目标页面的地址，则首先打开目标页面，再开始获取元素
        add_btn = self.browser.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a')
        add_btn.click()
        if self.browser.current_url != self.add_employee_url:
            self.browser.get(self.add_employee_url)
        code = self.browser.find_element_by_name('code')
        code.send_keys('004')
        name = self.browser.find_element_by_name('name')
        name.send_keys('xiao')
        save = self.browser.find_element_by_name('_save')
        save.click()


if __name__ == '__main__':
    sd = SeleniumDemo()
    sd.login()
    sd.add_employee()
    # sd.query_product()
