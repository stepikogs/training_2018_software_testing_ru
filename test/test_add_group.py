# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_add_def_group(app):
    app.group.create(Group())


def test_add_group_wrong_attributes(app):
    # preparation phase
    group = Group(group_name="name_assigned", jeegurda='incorrect', group_header='header_assigned')
    # creation phase
    app.group.create(group)


def test_add_empty_group(app):
    app.group.create(Group(group_name="",
                           group_header="",
                           group_footer=""))


def test_add_group(app):
    app.group.create(Group(group_name="testgroup",
                           group_header="testheader",
                           group_footer="testfooter"))
