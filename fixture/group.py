__author__ = 'George Stepiko'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    # navigation
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
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    # modification
    def modify_first(self, field, value):
        wd = self.app.wd
        self.open_groups_page()
        # check and select first element
        if not self.app.select_first():
            # nothing to do as not found
            print("No elements found so nothing to modify")
        else:
            # modify first element if selected successfully
            wd.find_element_by_name("edit").click()
            self.app.update_text_field(field, value)
            wd.find_element_by_name("update").click()
            self.return_to_groups_page()

    # deletion
    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # check and select first element
        if not self.app.select_first():
            # nothing to do as not found
            print("No elements found so nothing to delete")
        else:
            # delete first element if selected successfully
            wd.find_element_by_name("delete").click()
            self.return_to_groups_page()
