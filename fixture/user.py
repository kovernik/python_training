from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_user_creation_page()
        self.fill_user_form(user)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_cache = None

    def open_user_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("middlename", user.middle)
        self.change_field_value("address", user.address)
        self.change_field_value("company", user.company)
        self.change_field_value("home", user.homephone)
        self.change_field_value("mobile", user.mobilephone)
        self.change_field_value("email", user.email)

    def change_field_value(self, field_form, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_form).click()
            wd.find_element_by_name(field_form).clear()
            wd.find_element_by_name(field_form).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def select_modify_user(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def modify_user_by_index(self, index, user):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_modify_user(index)
        # fill contact form
        self.fill_user_form(user)
        # update contact
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.user_cache = None

    def delete(self):
        self.delete_user_by_index(0)

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_index(index)
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.user_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                self.user_cache.append(User(id=id, firstname=firstname, lastname=lastname))
        return list(self.user_cache)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_dy_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_dy_tag_name("a").click()
