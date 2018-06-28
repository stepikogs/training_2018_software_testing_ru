__author__ = 'George Stepiko'


class Group:

    # do not allow to add new properties after __init__
    __slots__ = 'group_name', \
                'group_header', \
                'group_footer'

    # constructor with optional arguments
    # argument not defined in kwargs will be None
    def __init__(self, **kwargs):
        self.group_name = kwargs.get('group_name')
        self.group_header = kwargs.get('group_header')
        self.group_footer = kwargs.get('group_footer')
