__author__ = 'George Stepiko'
from model.record import Record


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
        wd.find_element_by_xpath('//img[@title="Edit"]').click()
        self.fill_record_form(upd_group)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    # deletion
    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first record
        self.app.select_first()
        # delete first element if selected successfully
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # deletion confirmation
        wd.switch_to_alert().accept()

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select all the records...
        wd.find_element_by_id("MassCB").click()
        # ... and delete them
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # confirmation
        wd.switch_to_alert().accept()

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

    def provide(self, count=1):
        wd = self.app.wd
        self.app.open_home_page()
        records_delta = count - len(wd.find_elements_by_name("selected[]"))
        if records_delta > 0:
            for item in range(records_delta):
                self.create(Record(firstname='dummy'))
            print('No enough records found so ' + str(records_delta) + ' new dummy record(-s) created')
        else:
            print('Enough records for the test, nothing to create here, (Check: ' + str(records_delta) + ').')
