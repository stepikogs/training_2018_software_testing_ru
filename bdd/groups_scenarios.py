__author__ = 'George Stepiko'

from pytest_bdd import scenario
from .groups_steps import *


@scenario('groups.feature',
          'Add new group',
          example_converters=dict(name=str,
                                  header=str,
                                  footer=str))
def test_add_group():
    pass


@scenario('groups.feature',
          'Delete a group',
          example_converters=dict(name=str,
                                  header=str,
                                  footer=str))
def test_delete_group():
    pass
