__author__ = 'George Stepiko'

import pymysql.cursors
from model.group import Group
from model.record import Record


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (groupid, name, header, footer) = row
                group_list.append(Group(id=str(groupid),
                                  group_name=name,
                                  group_header=header,
                                  group_footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_record_list(self, extended=False):
        record_list=[]
        cursor = self.connection.cursor()
        try:
            if not extended:
                cursor.execute('select id, firstname, lastname from addressbook where deprecated="0000-00-00 00:00:00"')
                for row in cursor:
                    (id, firstname, lastname) = row
                    record_list.append(Record(id=str(id),
                                              firstname=firstname,
                                              lastname=lastname))
            elif extended:
                cursor.execute('select id, firstname, lastname, \
                address, home, mobile, work, phone2, email, email2, email3 \
                from addressbook \
                where deprecated="0000-00-00 00:00:00"')
                for row in cursor:
                    (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3,) = row
                    record_list.append(Record(id=str(id),
                                              firstname=firstname,
                                              lastname=lastname,
                                              address=address,
                                              home=home,
                                              mobile=mobile,
                                              work=work,
                                              phone2=phone2,
                                              email=email,
                                              email2=email2,
                                              email3=email3))
        finally:
            cursor.close()
        return record_list

    def destroy(self):
        self.connection.close()
