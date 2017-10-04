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
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
<<<<<<< HEAD
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
=======
        return self.id == other.id and self.name == other.name
>>>>>>> c8e04c222356b95426d33d47a7b22fd59ac42272
