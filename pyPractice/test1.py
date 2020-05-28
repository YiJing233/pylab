# python 第五章 pizza

available_items = ('mushroom','olives','green papers',
                    'pineapple')
requested_toppings = ['mushroom','papers','pineapple']
for requested_topping in requested_toppings:
    if requested_topping in available_items:
        print("Adding "+ requested_topping.title() +".")
    else:
        print("Sorry,we don't have "+requested_topping +".")

print("Finished making your pizza!")

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.taillenth = 0

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
    def infor(self):
        print(self.name.title() + "'s age is " + 
                                    str(self.age))
    
    def update_age(self,new_age):
        self.age = new_age

    def update_taillenth(self,taillenth):
        if taillenth >= self.taillenth:
            self.taillenth = taillenth
        else :
            print("You cannot roll back the taillenth!")

    def increse_age(self,app):
        self.age += app 
    
my_dog = Dog('amy',3)

my_dog.sit()

print("My dog's name is " + my_dog.name.title() 
                        +" and its age is " 
                        + str(my_dog.age) + ".")

my_dog.roll_over()

your_dog = Dog('bob',2)

your_dog.sit()
your_dog.roll_over()

my_dog.update_age(5)
my_dog.infor()

my_dog.update_taillenth(2)
print("Taillenth is " + str(my_dog.taillenth) + "cm.")

my_dog.increse_age(3)
my_dog.infor()