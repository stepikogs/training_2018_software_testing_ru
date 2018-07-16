__author__ = 'George Stepiko'
from sys import maxsize


class Record:
    # do not allow to add new properties after __init__
    # synthetic (service) not-in-web-form properties start with underscore
    __slots__ = "firstname", \
                "middlename", \
                "lastname", \
                "nickname", \
                "photo", \
                "title", \
                "company", \
                "address", \
                "home", \
                "mobile", \
                "work", \
                "fax", \
                "email", \
                "email2", \
                "email3", \
                "homepage", \
                "bday", \
                "bmonth", \
                "byear", \
                "aday", \
                "amonth", \
                "ayear", \
                "address2", \
                "phone2", \
                "notes", \
                "id", \
                "_phones_from_home", \
                "_emails_from_home", \
                "_phones", \
                "_emails"

    # constructor with optional arguments
    # argument not defined in kwargs will be None
    def __init__(self, **kwargs):

        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.middlename = kwargs.get('middlename')
        self.nickname = kwargs.get('nickname')
        self.photo = kwargs.get('photo')
        self.title = kwargs.get('title')
        self.company = kwargs.get('company')
        self.address = kwargs.get('address')
        self.home = kwargs.get('home')
        self.mobile = kwargs.get('mobile')
        self.work = kwargs.get('work')
        self.fax = kwargs.get('fax')
        self.email = kwargs.get('email')
        self.email2 = kwargs.get('email2')
        self.email3 = kwargs.get('email3')
        self.homepage = kwargs.get('homepage')
        self.bday = kwargs.get('bday')
        self.bmonth = kwargs.get('bmonth')
        self.byear = kwargs.get('byear')
        self.aday = kwargs.get('aday')
        self.amonth = kwargs.get('amonth')
        self.ayear = kwargs.get('ayear')
        self.address2 = kwargs.get('address2')
        self.phone2 = kwargs.get('phone2')
        self.notes = kwargs.get('notes')
        # memo: id is hidden in form so could not be set
        self.id = kwargs.get('id')
        # properties not available in record form start from underscore
        self._phones = ('home',
                        'mobile',
                        'work',
                        'phone2')
        self._emails = ('email',
                        'email2',
                        'email3')

    def __repr__(self):
        return '%s: %s %s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        # id will be None  fro new-created object as unable to set it properly
        # firstname/lastname could be None if not updated; '' value will be asserted from list
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.firstname == other.firstname or (self.firstname is None and other.firstname == '')) and \
               (self.lastname == other.lastname or (self.lastname is None and other.lastname == ''))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
