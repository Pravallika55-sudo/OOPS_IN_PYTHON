#ALL ABOUT OOPS(PROGRAMMING PARADIGM THAT ORGANIZES CODE USING OBJECTS AND CLASSES)
#PROCEDURAL ORIENTED -FOCUS ON ONLY FUNCTIONS
#oops-Focuses on objects that contain both data and behavior
"""creating class"""
#class is a blue brint--->used to create object of a class
#object--->instance of a class
"""class Student: #class created
    Name="sai"
    RollNo=777
O=Student()#obj for given class
print(O.Name)"""
#Modifying Attributes
"""class Student: 
    Name="sai"
    RollNo=777
O=Student()
print("before modifying ",{O.Name})
O.Name="Pa1"
print("after modifying",{O.Name})"""
#Attributes--->also called varaibles belong to class or an object(4types)
#Instance attribute-belong to specific Obj
"""class Instance:
    def __init__(self,name,age):
        self.name=name#Instance attribute
        self.age=age#Instance attribute
O=Instance("pa1",19)
print(O.name)#pa1
print(O.age)#19
O.name="sai"
print(O.name)#Modified instance attribute"""
#Dynamically also we can add Instance Attribute
"""class Instance:
    pass
I=Instance()
I.Name="pa1"
I.Age=19
print(I.Name)
print(I.Age)
del I
print(I.Name)"""
#class Attributes-belong to only class
"""class ClassA:
    Name="pa1"#class Attributes
    Age=19#class Attributes
A=ClassA()
print(A.Name)
A.Name="sai"#Modifying class Attributes
print(A.Name)#Accessing class Attributes"""
#Public-Can be access anywhere
"""class Public:
    def __init__(self,name):
        self.name=name
P=Public("charan")
print(P.name)"""
#Private-can only access inside class
"""error --->class Private:
     def __init__(self):
         self.__name=name
         self.__age=age
P=Private()
print(P.__name)  AttributeError
Python prevents direct access
"""
#to access attributes in private
"""class Private:
    def __init__(self):
        self.name="private"
    def display(self):
        print(self.name)
P=Private()
P.display()"""
#------Attributes completed--------------#
#Inheritance ----one class to acquire the properties (attributes) and behaviors or actions(methods) of another class
"""class Animal:
    def eat(self):
        print("animal is eating")
class Dog(Animal):
    pass
D=Animal()
D.eat()"""
"""class Teacher:
    def __init__(self,name):
        self.name=name
class Student(Teacher):
    def display(self):
        print("this is child class")
S=Student("RAM")
S.display()
print(S.name)#Accessing parent class Attributes via child class obj"""
#Constructor Inheritance
"""class Parent:
    def __init__(self,name):
        self.name=name
class Child(Parent):
    pass
P=Parent("Ram")
print(P.name)#Child automatically inherits parent constructor if it doesn't have its own constructor
"""
# what if Child class have constructor(super)
"""class Parent:
    def __init__(self,name):
        self.name=name
class Child(Parent):
    def __init__(self,name):
        super().__init__(name)#calls parent constructor 
        print("this is child class")
P=Child("Pa1")
print(P.name)
class Dog:
    def eat(self):
        print("dog is eating")
class Cat(Dog):
    def sleep(self):
        super().eat()
        print("sleeping")
C=Cat()
C.eat()
C.sleep()"""
"""#MethodOverriding
class Method:
    def eat(self):
        print("eating1")
class child(Method):
    def eat(self):
        print("eating2")
E=child()
E.eat()#eating2
class Method:
    def eat(self):
        print("eating1")
class child(Method):
    def eat(self):
        super().eat()
        print("eating2")
E=child()
E.eat()#both eating printed"""
#Types of INHERITANCE
#Single Inheritance==1 child class inherits from parent class
"""class Parent:
    def details(self,name,age):
        self.name=name
        self.age=age
    def Own(self,name,age):
        print({self.name},"Owns a car at the age of", {self.age})
class Child(Parent):
    def Det(self,name):
        print("My parent name is",{self.name})
C=Child()
C.details("pa1",20)
C.Det("pa1")
C.Own("pa1",19)
print(C.name)"""
#Multiple Inheritance--->single child inherits its properties from more than 1 parent child
"""class Gf:
    def GrandF(self):
        print("Gfather has bike")
class Father:
    def father(self):
        print("father has bike")
class Child(Father,Gf):
    print("Child also have a bike")
C=Child()
C.GrandF
C.father()
"""
"""class Father:
    def __init__(self):
        print("father has bike")
class Mother:
    def __init__(self):
        print("Mother has scooty")
class Child(Mother,Father):
    def __init__(self):
        super().__init__()
        print("child has both")
C=Child()#only Mother has scooty printed as it was called first in child
#To call both constructors(CaLl manually by its names)
class A:
    def __init__(self):
        print("A CLASS")
class B:
    def __init__(self):
        print("B CLASS")
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("both a and b are called")
c=C()#all print statements are o/p"""
"""multi level inheritance: one class inherits properties from 1 class that class inherits properties from one class(Gf--->father--->child)"""
"""class Gf:
    def house(self):
        print("Gf has house")
class Father(Gf):#inherited from above class
    def bike(self):
        print("father has a bike")
class child(Father):#inherited from above class
    def cycle(self):
        print("child has bike")
C=child()
C.cycle()
C.bike()
C.house()"""
#MULTI LEVEL INHERITENCE(using constructors)
"""class Gf:
    def __init__(self):
        print("I AM First")
class Father(Gf):
    def __init__(self):
        super().__init__()
        print("I Am Second")
class Child(Father):
    def __init__(self):
        super().__init__()
        print("I AM third")
C=Child()"""
#Heirarichal- two childsacquires properties from parent class
"""class Parent:
    def Scooty(self):
        print("I have a scooty")
class Child1(Parent):
    def details(self):
        print("i can access scooty")
class Child2(Parent):
    def det(Parent):
        print("i can also access scooty")
C=Child1()
C.details()
C=Child2()
C.Scooty()
C.det()"""
"""#C.details()#AttributeError: 'Child2' object has no attribute 'details'
#using constructor
class Parent:
    def __init__(self):
        print("I have a scooty")
class Child1(Parent):
    def details(self):
        super().__init__()
        print("i can access scooty")
class Child2(Parent):
    def det(Parent):
        super().__init__()
        print("i can also access scooty")
C=Child1()
C.details()"""
#hybrid-->combination of any 2 or 3 inheritances
"""class A:
    def Feature1(self):
        print("feature1")
class B(A):#single or multiple
    def Feature2(self):
        print("feature2")
class C:#parent
    def Feature3(self):
        print("feature3")
class D(B,C):
    def Feature4(self):
        print("Feature4")
d=D()
d.Feature4()
d.Feature3()"""
#Encapsulation--Binding variables and functions into single unit while restricting access to some parts.
"""Encapsulation is done using:
•	Public members
•	Protected members
•	Private members"""
#PUBLIC-can access anywhere(inside or outside or derived)
"""class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name",self.name)
b=A("pa1")
b.show()
b.name="ram"## Can be modified directly
b.show()"""
#Protect--can access inside the class and also in child classes
"""class A:
    def __init__(self,name):
        self._name=name
    def show(self):
        print("Parentname",self._name)
class B(A):
    def change_name(self,new_name):
        self._name=new_name
O=B("pavan")
O.show()
print(O._name)"""
#Private-Private mem can be accessed only within the class where they are defined
"""class A:
    def __init__(self,name):
        self.__name=name
        print("my name is",self.__name)#private
    def display(self):
        print("display")
a=A("sai")"""
#================================
#ENCAPSULATION BEST EXAMPLE+++++
#================================
"""class Bankaccount:
    def __init__(self,name,pin,balance):
        self.name=name#public
        self._balance=balance#protect
        self.__pin=pin#private
    def deposit(self,amount):
        self._balance+=amount
        print("deposited amount is",{self._balance})
    def withdraw(self,amount,pin):
        if pin==self.__pin:
            if amount<=self._balance:
                self._balance-=amount
                print("the money after deduction is",{self._balance})
            else:
                print("No enough mny")
        else:
            print("enter valid pin")
    def Checkbal(self,pin):
        if pin==self.__pin:
            print("Available balance are",self._balance)
        else:
            print("wrong pin")
        
            
        
B=Bankaccount("pa1",1899,5000)
B.deposit(1000000000000)
B.withdraw(5000,1899)
B.Checkbal(1899)"""
#Abstraction-
        #Abstraction means hiding internal implementation details and showing only the essential features to the user.
#two types--->1.abstract-declaration only in parent class,implemention was given by child
#2.concretemethod-both declaration,implementation done by parent class only,child can easily use it
"""from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start():
        pass

class Car(Vehicle):
    def start(self):
        print("driving")
class Bike(Vehicle):
    def start(self):
        print("enjoying")
C=Car()
C.start()
B=Bike()
B.start()"""
#Abstract method-concrete
"""from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def start(self):
        pass
    def dog(self):
        print("dog barks")#concrete method
class B(A):
    def start(self):
        print("cat says meow")
class C(B):
    def duck(self):
        print("duck dik dik")
b=B()
b.start()
c=C()
c.duck()
    """
#polymorphism-->one thing in many forms
#operator overloading
"""class Number:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        a=self.a+other.a
        b=self.b+other.b
        c=self.c+other.c
        res=Number(a,b,c)
        return res
n1=Number(1,2,3)
n2=Number(4,5,6)
n3=n1+n2
print(n1.a,n2.b,n3.c)"""
#method overloading---Multiple methods having the same name but different parameters
"""class A:
    def __add__(self,a,b):#method over written
        print(a+b)
    
    def __add__(self,a,b,c):
        print(a+b+c)
a=A()
a.__add__(8,9,10)"""
#Method Overloading Using Default Arguments

"""class A:
    def add(self,a,b,c=0):
        print(a+b+c)
a=A()
a.add(10,20)
a.add(10,20,30)"""
#Method Overloading Using *args
"""class A:
    def add(self,*args):
        print(sum(args))
a=A()
a.add(10,20,30)"""
#method overriding-child class overrides the parent class
"""class A:
    def sound(self):
        print("a makes sound")#overrided
class C(A):
    def sound(self):
        print("c makes sound")#print
c=C()
c.sound()"""
#Polymorphism using common method
class A:
    def sound(self):
        print("dog barks")
class B:
    def sound(self):
        print("meow barks")
class C:
    def sound(self):
        print("duck barks")
    animals=[A(),B()]
    for animal in animals:
        animal.sound()

    



        
              





        
    



    




    




    






