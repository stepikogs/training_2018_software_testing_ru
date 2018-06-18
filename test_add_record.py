# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from record import Record

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddRecord(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_record(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_record(wd, Record(firstname="testname",
                                      lastname="testlast",
                                      midname="testmid",
                                      nickname="testnick",
                                      title="testtitle",
                                      company="testcompany",
                                      address="testaddr",
                                      phone="testphone",
                                      mobile="testmob",
                                      work="testwork",
                                      fax="testfax",
                                      mail1="tesmmail1",
                                      mail2="testmail2",
                                      mail3="testmail3",
                                      page="testpage",
                                      bday=12,
                                      bmon=2,
                                      byear="1986",
                                      aday=13,
                                      amon=8,
                                      ayear="2003",
                                      second_address="testsecaddr",
                                      second_phone="testhomesec",
                                      notes="testnotes"
                                      ))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_record(self, wd, record):
        # init new record
        wd.find_element_by_link_text("add new").click()
        # fill text fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(record.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(record.midname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(record.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(record.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(record.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(record.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(record.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(record.phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(record.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(record.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(record.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(record.mail1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(record.mail2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(record.mail3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(record.page)
        # fill birth date in human-readable format
        self.set_date(wd, form=1, value=record.bday)
        self.set_date(wd, form=2, value=record.bmon)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(record.byear)
        # fill anniversary date in human-readable format
        self.set_date(wd, form=3, value=record.aday)
        self.set_date(wd, form=4, value=record.amon)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(record.ayear)
        # continue with test fields
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(record.second_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(record.second_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(record.notes)
        # submit data to new record
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def set_date(self, wd, form, value):
        if form in (1, 3):
            value += 2
        elif form in (2, 4):
            value += 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" + str(value) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" + str(value) + "]").click()

    def set_day(self, wd, form, day):
        value = str(day + 2)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" + value + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" + value + "]").click()

    def set_mon(self, wd, form, mon):
        value = str(mon + 1)
        if not wd.find_element_by_xpath(
                "//div[@id='content']/form/select[" + str(form) + " ]//option[" + value + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[" + str(form) + " ]//option[" + value + "]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
