__author__ = 'George Stepiko'

from model.group import Group
import random
import string


constant = [
    Group(group_name="name1",
          group_header="header1",
          group_footer="footer1"),
    Group(group_name="name2",
          group_header="header2",
          group_footer="footer2")
]

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

