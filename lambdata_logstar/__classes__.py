import pandas as pd


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0

    def recieve_upvotes(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100

    def __repr__(self):
        return '({}, {})'.format(self.name, self.upvotes)
        

class Animal:
    """ General representation of animals"""
    
    def __init__(self, name, weight, diet_type):
        self.name = name
        self.weight = weight
        self.diet_type = diet_type
    
    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + 'is delisccous, yum'

class Tiger(Animal):
    """ representastion of tiger, subclass of animal"""
    
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes

    def say_great(self):
        return 'ITS GREEEEEEAAAT'

    def run(self):
        return 'SKANMPERWOOOOOSH!'