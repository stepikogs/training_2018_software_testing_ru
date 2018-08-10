__author__ = 'George Stepiko'


from fixture.orm import OrmFixture

db = OrmFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    lala = db.get_record_list()
    for item in lala:
        print(item)
    print(len(lala))
finally:
    pass
