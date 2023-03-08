''' Class lesson '''

class Study_class():    
    def __init__(self, firstname, lastname):  # Q: How to create init which is not requiered arguments?
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "call of string in class Study_class"
    
    x = 1

    def some_method(self):
        print (f"Hello {self.firstname} {self.lastname}")

    def meth_with_one_property(self):
        print(f'Bye, {self.firstname}')





clas_inst = Study_class

print(clas_inst(1, 2))
