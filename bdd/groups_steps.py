__author__ = 'George Stepiko'

from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()


# @given('a group with <name>, <header> and <footer>')
@given('a group with <name>, <header> and <footer>')
def my_group(name, header, footer):
    return Group(group_name=name,
                 group_header=header,
                 group_footer=footer)


@when('I add the group')
def add_group(app, my_group):
    app.group.create(my_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, my_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(my_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_list(db, app):
    app.group.provide()
    return db.get_group_list()


@given('a random group')
def random_one(non_empty_list):
    return random.choice(non_empty_list)


@when('I delete the group')
def delete_group(random_one, app):
    app.group.delete_by_id(random_one.id)


@then('Groups list is same but with no group deleted')
def verify_group_deleted(db, non_empty_list, random_one, app, check_ui):
    old_groups = non_empty_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_one)
    assert old_groups == new_groups
    if check_ui:
        # fixme does not work with multi and traveling spaces
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)
