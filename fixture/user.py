from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        # init user creation
        wd.find_element_by_link_text("add new").click()
        # fill user form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middle)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def fill_contact_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("title", address.title)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("company", address.company)
        self.change_field_value("home", address.home)
        self.change_field_value("email", address.email)
        self.change_field_value("address2", address.address)

    def modify(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # fill user form
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middle)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        # submit user modify
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def modify_first_user(self, new_user_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_user_form(new_user_data)
        wd.find_element_by_name("update").click()
        self.app.open_home_pagereturn_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_user_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        user = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            name = cells[2].text
            surname = cells[1].text
            user.append(User(id=id, name=name, surname=surname))
        return user
