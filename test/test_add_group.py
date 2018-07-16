# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlength):
    symbols = string.ascii_letters + string.digits  # + ' '*10 fixme: work with multi-space
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [
    Group(group_name="testgroup",                    # full group
          group_header="testheader",
          group_footer="testfooter"),
    Group(),                                         # default group
    Group(group_name="name_assigned",                # group with invalid input
          jeegurda='incorrect',
          group_header='header_assigned'),
    Group(group_name="",                             # group with empty values
          group_header="",
          group_footer="")
    ] + [
    Group(group_name=random_string('name', 10),      # group with random values
          group_footer=random_string('footer', 10),
          group_header=random_string('header', 10))
    for i in range(5)                                # 5 random groups in total
    ]


# test methods
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
