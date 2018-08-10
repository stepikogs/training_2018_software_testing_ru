__author__ = 'George Stepiko'


from fixture.orm import OrmFixture
from model.group import Group

db = OrmFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    lala = db.get_records_not_in_group(Group(id='118'))
    for item in lala:
        print(item)
    print(len(lala))
finally:
    pass
