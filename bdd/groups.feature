Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group
  Then the new group list is equal to the old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |


Scenario: Delete a group
  Given a non-empty group list
  Given a random group
  When I delete the group
  Then Groups list is same but with no group deleted