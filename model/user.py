from sys import maxsize


class User:
    def __init__(self, firstname=None, lastname=None, email=None, mobilephone=None, homephone=None, workphone=None,
                 secondaryphone=None, company=None, address=None, middle=None, nickname=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobilephone = mobilephone
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.company = company
        self.address = address
        self.middle = middle
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
