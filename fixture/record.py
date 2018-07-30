__author__ = 'George Stepiko'

from model.record import Record
import re


class RecordHelper:

    def __init__(self, app):
        self.app = app

    # creation
    def create(self, record):
        wd = self.app.wd
        self.app.open_home_page()
        # init new record
        wd.find_element_by_link_text("add new").click()
        self.fill_form(record)
        # submit data to new record
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.rec_cash = None

    # view
    def open_view_by_index(self, index):
        wd = self.app.wd
        return wd.find_elements_by_xpath('//img[@title="Details"]')[index].click()

    def get_phones_from_view(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_view_by_index(index)
        record = Record()
        full_info = wd.find_element_by_id('content').text
        # get phones info   todo: refactor to support backward checks (the only _phones_from_view Record property here)
        setattr(record, 'home', re.search('H: (.*)', full_info).group(1))
        setattr(record, 'mobile', re.search('M: (.*)', full_info).group(1))
        setattr(record, 'work', re.search('W: (.*)', full_info).group(1))
        setattr(record, 'phone2', re.search('P: (.*)', full_info).group(1))
        return record

    # modification
    def open_edit_by_index(self, index):
        wd = self.app.wd
        return wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()

    def get_info_from_edit(self, index, htmlized=False):
        # wd = self.app.wd
        self.app.open_home_page()
        # create dummy record as source of fields - any property is None
        record = Record()
        self.open_edit_by_index(index=index)
        # read the form and return the 'Record' object updated
        return self.read_form(record, htmlized)

    def modify_by_index(self, upd_record, index):
        wd = self.app.wd
        self.open_edit_by_index(index=index)
        # wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()
        self.fill_form(upd_record)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.rec_cash = None

    def modify_first(self, upd_record):
        self.modify_by_index(upd_record=upd_record, index=0)

    # deletion
    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first record
        self.app.select_by_index(index=index)
        # delete first element if selected successfully
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # deletion confirmation
        wd.switch_to_alert().accept()
        self.rec_cash = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select all the records...
        wd.find_element_by_id("MassCB").click()
        # ... and delete them
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # confirmation
        wd.switch_to_alert().accept()
        self.rec_cash = None

    # load
    rec_cash = None

    def get_list(self):  # todo: remove outdated (commented) lines here
        wd = self.app.wd
        self.app.open_home_page()
        self.rec_cash = []
        for element in wd.find_elements_by_xpath('//*[@id="maintable"]/tbody/tr[@name="entry"]'):
            # dummy record to append cash
            record_to_cash = Record()
            setattr(record_to_cash, 'id', element.find_element_by_name('selected[]').get_attribute('value'))
            setattr(record_to_cash, 'firstname', self.record_cell_value(element, 3))
            setattr(record_to_cash, 'lastname', self.record_cell_value(element, 2))
            setattr(record_to_cash, 'address', self.record_cell_value(element, 4))
            # synthetic properties for phones and emails
            record_to_cash._emails_from_home = self.record_cell_value(element, 5)
            record_to_cash._phones_from_home = self.record_cell_value(element, 6)
            self.rec_cash.append(record_to_cash)
        return list(self.rec_cash)

    # service methods
    @staticmethod
    def record_cell_value(element, cell):
        return element.find_element_by_xpath('td[%s]' % cell).text

    def fill_form(self, record):
        # todo make 'drops' and 'upload' as another '_xxx' Record properties (common through class so could be set)
        drops = {"bday": 1,  # attribute: form ID dictionary to process them in different way
                 "bmonth": 2,
                 "aday": 3,
                 "amonth": 4}
        upload = "photo"  # upload field is special as well
        # fill text fields
        for att in record.__slots__:
            # ignore both id as hidden and all the synthetic '_xxx' fields unable to pass to form
            if att is not 'id' and not re.match('_.+', att):
                value = getattr(record, att)
                # if field is not drop-down one (aka set date)
                if str(att) not in drops and str(att) not in upload:
                    self.app.update_text_field(field=att, value=value)
                elif str(att) in drops:
                    # drop-down fields processed
                    self.set_date(form=drops[att], value=value)
                elif str(att) in upload:
                    self.app.upload_file(field=att, path=value)
                else:
                    print('There is no way to reach this!')

    def read_form(self, record, htmlized=False):
        drops = {"bday": 1,  # attribute: form ID dictionary to process them in different way
                 "bmonth": 2,
                 "aday": 3,
                 "amonth": 4}
        upload = "photo"  # upload field is special as well
        # read text fields, ignore not-text ones
        for att in record.__slots__:
            # ignore fields unable to read from web-form
            if not re.match('_.+', att):
                # for now we need text fields only to verify
                if str(att) not in drops and str(att) not in upload:
                    # read value from the field requested
                    field_value = self.app.read_text_field(field=att)
                    field_value = self.app.htmlize_it(field_value) if htmlized else field_value
                    # print(att, value)  # debug print
                    # set 'att' property with 'field_value' value
                    setattr(record, att, field_value)
                # drop-downs and upload fields are ignored for now
                else:
                    pass  # todo: non-text fields would be processed one day
        # return the 'Record' object updated with real text fields values in properties
        return record

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

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def provide(self, requested=1, record=Record(firstname='dummy')):
        self.app.open_home_page()
        records_delta = requested - self.count()
        if records_delta > 0:
            for item in range(records_delta):
                self.create(record)
            print('No enough records found so ' + str(records_delta) + ' new dummy record(-s) created')
        else:
            print('Enough records for the test, nothing to create here, (Check: ' + str(records_delta) + ').')
