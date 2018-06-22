__author__ = 'George Stepiko'


class RecordHelper:

    def __init__(self, app):
        self.app = app

    # creation
    def create(self, record):
        wd = self.app.wd
        self.app.open_home_page()
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
        self.app.return_to_home_page()

    # modification
    def modify_first(self, field, value):
        wd = self.app.wd
        # check and select first element
        if not self.edit_first():
            # nothing to do as not found
            print("No elements found so nothing to modify")
        else:
            # modify first element if selected successfully
            self.app.update_text_field(field, value)
            wd.find_element_by_name("update").click()
            self.app.return_to_home_page()

    # deletion
    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # check and select first element
        if not self.app.select_first():
            # nothing to do as not found
            print("No elements found so nothing to delete")
        else:
            # delete first element if selected successfully
            wd.find_element_by_xpath('//input[@value="Delete"]').click()
            # deletion confirmation
            wd.switch_to_alert().accept()

    # service methods
    def set_date(self, wd, form, value):
        """
        helps work with drop-down fields and allows to add these attributes to the 'Record' class

        :param wd: webdriver
        :param form: just formid to (a) specify where to paste value and (b) designate value type form form ID
        :param value: day/month value to use
        """
        if form in (1, 3):
            value += 2
        elif form in (2, 4):
            value += 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" +
                                        str(value) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[" + str(form) + " ]//option[" +
                                     str(value) + "]").click()

    def edit_first(self):
        """
        for records table only
        Very naive check if items list is not empty to modify items
        works both for groups and records

        :return:
            True if it exists (item is opened for edit as well)
            False if no elements found
        """
        wd = self.app.wd
        if not wd.find_elements_by_xpath('//img[@title="Edit"]'):
            return False
        else:
            wd.find_element_by_xpath('//img[@title="Edit"]').click()
            return True
