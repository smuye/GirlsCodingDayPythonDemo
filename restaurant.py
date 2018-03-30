#!/bin/python3

class Restaurant():

 def __init__(self,name,cuisine_type):
  self.name = name
  self.cuisine_type = cuisine_type
  self.number_served = 0
   
 def describe_restaurant(self):
  print(self.name.title()+'主营'+self.cuisine_type)
    
 def open_restaurant(self):
  print(self.name.title()+'餐馆正在营业')

 def served(self):
  print(str(self.number_served)+ '已经接待.')
  
 def set_number_served(self,count):
    if count >= self.number_served:
       self.number_served = count
    else:
      print('搞错了!')
      
 def increment_number_served(self,miles):
   self.number_served += miles
   
   
   

restaurant=Restaurant('haha','hotspot')
restaurant.describe_restaurant()
restaurant.open_restaurant()



restaurant.number_served=20
restaurant.served()

restaurant.set_number_served(10)
restaurant.served()

restaurant.increment_number_served(5)
restaurant.served()
    