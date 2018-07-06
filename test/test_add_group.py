# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_add_group(app):
    old_groups = app.group.get_list()
    group = Group(group_name="testgroup",
                  group_header="testheader",
                  group_footer="testfooter")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_def_group(app):
#     old_groups = app.group.get_list()
#     group = Group()
#     app.group.create(group)
#     new_groups = app.group.get_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_add_group_wrong_attributes(app):
#     # preparation phase
#     old_groups = app.group.get_list()
#     group = Group(group_name="name_assigned", jeegurda='incorrect', group_header='header_assigned')
#     # creation phase
#     app.group.create(group)
#     new_groups = app.group.get_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_add_empty_group(app):
#     old_groups = app.group.get_list()
#     group = Group(group_name="", group_header="", group_footer="")
#     app.group.create(group)
#     new_groups = app.group.get_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
