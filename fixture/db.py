__author__ = 'George Stepiko'

import pymysql.cursors
from model.group import Group


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

    def destroy(self):
        self.connection.close()
