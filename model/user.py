from sys import maxsize


class User:
    def __init__(self, name=None, surname=None, email=None, mobile=None, phone=None, company=None, address=None,
                 middle=None, nickname=None, id=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.mobile = mobile
        self.phone = phone
        self.company = company
        self.address = address
        self.middle = middle
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
