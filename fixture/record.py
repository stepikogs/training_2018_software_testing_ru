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
        self.fill_record_form(record)
        # submit data to new record
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def fill_record_form(self, record):
        drops = {"bday": 1,  # attribute: form ID dictionary to process them in different way
                 "bmonth": 2,
                 "aday": 3,
                 "amonth": 4}
        upload = "photo"  # upload field is special as well
        # fill text fields
        for att in record.__slots__:
            value = getattr(record, att)
            if str(att) not in drops and str(att) not in upload:  # if field is not drop-down one (aka set date)
                self.app.update_text_field(field=att, value=value)
            elif str(att) in drops:
                self.set_date(form=drops[att], value=value)  # drop-down fields processed
            elif str(att) in upload:
                self.app.upload_file(field=att, path=value)
            else:
                print('There is no way to reach this!')

    # modification
    def modify_first(self, upd_group):
        wd = self.app.wd
        # check and select first element
        if not self.edit_first():
            # nothing to do as not found
            print("No elements found so nothing to modify")
        else:
            # modify first element if selected successfully
            self.fill_record_form(upd_group)
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

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        if not wd.find_elements_by_id("MassCB"):  # make sure we have any records to delete
            print()  # just new line here
            print(str("delete_all_groups: Nothing to do here"))
        else:
            wd.find_element_by_id("MassCB").click()  # select all the records...
            wd.find_element_by_xpath('//input[@value="Delete"]').click()  # ... and delete them
            wd.switch_to_alert().accept()  # confirmation

    # service methods
    def set_date(self, form, value):
        """
        helps work with drop-down fields and allows to add these attributes to the 'Record' class

        :param form: just formid to (a) specify where to paste value and (b) designate value type form form ID
        :param value: day/month value to use
        """
        wd = self.app.wd
        if value:
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
