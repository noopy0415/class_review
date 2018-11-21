class Customer(object):
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka")
    ken.full_name()

    tom = Customer(first_name="Tom", family_name="Ford")
    tom.full_name()
