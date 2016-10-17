#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Plant(object):
    def __init__(self, name):
        self.name = name
        print self.name, "is here"

    def make_oxygen(self):
        print self.name,'makes oxygen'


class Animal(object):
    def __init__(self, name):
        self.name = name
        print self.name, 'is here'

    def say(self, something):
        print self.name , 'says', something


class Dog(Animal):
    def __init__(self, name):
        self.name = name     
        super(Dog, self).__init__(name)

    def run(self, somewhere):
        print self.name, 'runs to', somewhere


class PlantFish(Plant, Animal):    
    def __init__(self, name):
        self.name = name
        super(PlantFish, self).__init__(name)


dog = Dog("Lucky")
dog.say('hello')
dog.run('park')


plant_fish = PlantFish("Super")
plant_fish.say('hi')
plant_fish.make_oxygen()

print '-' * 20

def make_sound(obj):
    obj.say('ok')


make_sound(Dog('Lucky'))
make_sound(PlantFish('Super'))

