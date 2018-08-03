__author__ = 'George Stepiko'
from model.group import Group


class GroupHelper:

    def __init__(self, app, db):
        self.app = app
        self.db = db

    # groups navigation
    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith('/group.php') and wd.find_elements_by_name('new'):
            return
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
        self.fill_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cash = None

    # modification
    def modify_by_index(self, upd_group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.app.select_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form(upd_group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None

    def modify_by_id(self, upd_group, group_id):
        wd = self.app.wd
        self.open_groups_page()
        self.app.select_by_id(group_id)
        wd.find_element_by_name("edit").click()
        self.fill_form(upd_group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None

    def modify_first(self, upd_group):
        self.modify_by_index(upd_group=upd_group, index=0)

    # deletion
    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.app.select_by_index(index)
        # delete the group selected
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_by_id(self, group_id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.app.select_by_id(group_id)
        # delete the group selected
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_all(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = wd.find_elements_by_name("selected[]")  # create 'selected[]' list to delete them
        for item in groups:
            item.click()  # select any group found
        wd.find_element_by_name("delete").click()  # delete all the groups selected
        self.return_to_groups_page()
        self.group_cash = None

    # load
    group_cash = None

    def get_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cash = []
            for el in wd.find_elements_by_css_selector("span.group"):
                grouptext = el.text
                groupid = el.find_element_by_name('selected[]').get_attribute('value')
                self.group_cash.append(Group(group_name=grouptext,
                                       id=groupid))
        return list(self.group_cash)

    # service methods
    def fill_form(self, fill_group):
        for att in fill_group.__slots__:  # get attributes from __slots__
            if att is not 'id':
                value = getattr(fill_group, att)
                # print(att, value)
                self.app.update_text_field(field=att, value=value)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def provide(self, requested=1, where='db'):
        self.open_groups_page()
        # todo fix the conditions below
        groups_delta = requested - self.count() if where == 'web' else requested - len(self.db.get_group_list())
        if groups_delta > 0:
            for item in range(groups_delta):
                self.create(Group(group_name='dummy_group'))
            print('No enough groups found so ' + str(groups_delta) + ' new dummy group(-s) created')
        else:
            print('Enough groups for the test, nothing to create here, (Check: ' + str(groups_delta) + ').')

