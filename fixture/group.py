__author__ = 'George Stepiko'
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    # groups navigation
    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # creation
    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form passing not required fields
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    # modification
    def modify_first(self, upd_group):
        wd = self.app.wd
        self.open_groups_page()
        # edit first group found in list
        wd.find_element_by_name("edit").click()
        # self.app.update_text_field(field, value)  # 'None' check is inside
        self.fill_group_form(upd_group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    # deletion
    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.app.select_first()
        # delete the group selected
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete_all(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = wd.find_elements_by_name("selected[]")  # create 'selected[]' list to delete them
        for item in groups:
            item.click()  # select any group found
        wd.find_element_by_name("delete").click()  # delete all the groups selected
        self.return_to_groups_page()

    # service methods
    def fill_group_form(self, fill_group):
        for att in fill_group.__slots__:  # get attributes from __slots__
            value = getattr(fill_group, att)
            print(att, value)
            self.app.update_text_field(field=att, value=value)

    def provide(self, count=1):
        wd = self.app.wd
        self.open_groups_page()
        groups_delta = count - len(wd.find_elements_by_name("selected[]"))
        if groups_delta > 0:
            for item in range(groups_delta):
                self.create(Group(group_name='dummy_group'))
            print('No enough groups found so ' + str(groups_delta) + ' new dummy group(-s) created')
        else:
            print('Enough groups for the test, nothing to create here, (Check: ' + str(groups_delta) + ').')
