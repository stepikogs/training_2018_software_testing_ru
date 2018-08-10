__author__ = 'George Stepiko'

from pony.orm import *
from datetime import datetime
from model.group import Group
from model.record import Record
# from pymysql.converters import decoders
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class OrmFixture:
    db = Database()

    class OrmGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        group_name = Optional(str, column='group_name')
        group_header = Optional(str, column='group_header')
        group_footer = Optional(str, column='group_footer')
        records = Set(lambda: OrmFixture.OrmRecord, table='address_in_groups', column='id',
                      reverse='groups', lazy=True)

    class OrmRecord(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: OrmFixture.OrmGroup, table='address_in_groups', column='group_id',
                     reverse='records', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql',
                     host=host,
                     database=name,
                     user=user,
                     password=password,
                     conv=conv
                     # conv=decoders
                     )
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id),
                         group_name=group.group_name,
                         group_header=group.group_header,
                         group_footer=group.group_footer)
        return list(map(convert, groups))

    def convert_records_to_model(self, records):
        def convert(record):
            return Record(id=str(record.id),
                         firstname=record.firstname,
                         lastname=record.lastname)
        return list(map(convert, records))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in OrmFixture.OrmGroup))

    @db_session
    def get_record_list(self):
        return self.convert_records_to_model(select(r for r in OrmFixture.OrmRecord if r.deprecated is None))

    @db_session
    def get_records_in_group(self, group):
        orm_group = list(select(g for g in OrmFixture.OrmGroup if g.id == group.id))[0]
        return self.convert_records_to_model(orm_group.records)

    @db_session
    def get_records_not_in_group(self, group):
        orm_group = list(select(g for g in OrmFixture.OrmGroup if g.id == group.id))[0]
        return self.convert_records_to_model(select(r for r in OrmFixture.OrmRecord
                                                    if r.deprecated is None and orm_group not in r.groups))
