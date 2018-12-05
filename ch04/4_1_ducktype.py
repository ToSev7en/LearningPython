
class Duck:
    def say(self):
        print('I am a duck')


class Cat:
    def say(self):
        print('I am a cat')


class Dog:
    def say(self):
        print('I am a dog')


animal = Cat
animal().say()

animal_lst = [Duck, Cat, Dog]

for animal in animal_lst:
    animal().say()

a = ['s','c','p']
b = ['r','e','w']
named_tuple = set()
named_tuple.add('q')
named_tuple.add('z')
named_tuple.add('o')

a.extend(b)
print(a)

a.extend(named_tuple)
print(a)