class Stundent:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, first, second, third):
        return (int(first) + int(second) + int(third)) / 3
        
john = Stundent('John', '21', 'Computing')
print(john.name, john.age, john.class_)
print(john.average_test_score(input('first num '), input('second num '), input('third num ')))
