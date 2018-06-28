__author__ = 'George Stepiko'


class Record:

    # do not allow to add new properties after __init__
    __slots__ = "firstname", \
                "middlename", \
                "lastname", \
                "nickname", \
                "photo",\
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
                "notes"

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
