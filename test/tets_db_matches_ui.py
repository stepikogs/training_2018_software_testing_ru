__author__ = 'George Stepiko'
from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_list()

    def cleaner(group):
        return Group(id = group.id, group_name=app.htmlize_it(group.group_name))
    db_list = map(cleaner, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
