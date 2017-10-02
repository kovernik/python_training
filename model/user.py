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
        return self.id == other.id and self.name == other.name
