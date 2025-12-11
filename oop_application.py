'''
Task 01
Apply the 4 pillars of OOP in classes, and push the file into github and share your repo's link.
'''
#Taif AlQarni
#OOP practice

class Programming_languages:
    def __init__(self, ctreator, year):
    #Encapsulation --> making varibles private
        self._ctreator = ctreator
        self._year = year

    def get_langCreator(self):
        return self._ctreator
#abstraction rule each class will abstrct this
    def learn_me(self):
        return 'choose what to learn'



#inheritance --> inherit the parent (Programming_languages)
class Python_language(Programming_languages):
    # polymorphism
    def learn_me(self):
        return print("this is python language")

class Java_language(Programming_languages):
    # polymorphism
    def learn_me(self):
        return print("this is java language")
    pass

#outputdata

python = Python_language("Guido van Rossum", 1991)
java = Java_language("James Gosling", 1995)

languges = [python, java]
for l in languges:
    print("Creator: ", l.get_langCreator())
    print(l.learn_me()) 
    

