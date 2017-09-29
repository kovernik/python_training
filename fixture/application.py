from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(
                wd.find_elements_by_xpath("//input[@value='Delete']"))):
            wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(
                wd.find_elements_by_xpath("//input[@value='Delete']"))):
            wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
