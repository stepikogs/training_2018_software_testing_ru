__author__ = 'George Stepiko'


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
        for att in group.__slots__:  # get attributes from __slots__
            value = getattr(group, att)
            self.app.update_text_field(field=att, value=value)
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
            self.app.update_text_field(field, value)  # 'None' check is inside
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

    def delete_all(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = wd.find_elements_by_name("selected[]")  # create 'selected[]' list to delete them
        if not groups:  # nothing to do if no groups found
            print()  # just new line here
            print(str("delete_all_groups: Nothing to do here"))
        else:
            for item in groups:
                item.click()  # select any group found
            wd.find_element_by_name("delete").click()  # delete all the groups selected
            self.return_to_groups_page()
