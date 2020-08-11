# -*- coding: UTF-8 -*-

class Person:
    department = 'School of Information'  # a class variable

    def set_name(self, new_name):  # a method
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))
# Christopher Brooks live in Ann Arbor, MI, USA and works in the department School of Information
