class Person:
    def __init__(self, name, age, address):
        # Private attributes
        self._name = name
        self._age = age
        self._address = address

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_address(self, address):
        self._address = address

#
person1 = Person(name="Faraz", age=25, address="Lahore Pakistan")

#set attrib
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())

#modify
person1.set_name("Haris kay")
person1.set_age(30)
person1.set_address("Landi kotal")

# Accessing modified attributes
print("\n Modification:")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())
