__author__ = 'George Stepiko'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.record import RecordHelper


class Application:

    # fixture methods
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.record = RecordHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            print('fixture is not valid, re-create.')
            return False

    def destroy(self):
        self.wd.quit()

    # common methods
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def select_first(self):
        """
        Very naive check if items list is not empty to modify items
        works both for groups and records

        :return:
            True if it exists (item is selected as well)
            False if no elements found
        """
        wd = self.wd
        wd.find_element_by_name("selected[]").click()

    def update_text_field(self, field, value):
        """
        updates field with value
        field if assumed to be text and exists

        :param field:
        :param value:
        :return:
        """
        wd = self.wd
        if value:  # is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)
            print(field + ' property is set as "' + str(value) + '".')  # str(value) as value could be INT for years
        else:
            print(field + ' property has been PASSED as None (check: ' + str(value) + ').')

    def upload_file(self, field, path):
        """
        uploads file in easy way

        :param field: button to submit a file
        :param path: absolute path to file
        :return:
        """
        wd = self.wd
        if path:
            wd.find_element_by_name(field).send_keys(path)
        else:
            print('Nothing to upload')
