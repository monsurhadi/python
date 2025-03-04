#1
car=['marcedys','ferrari','lambo']
print(car)
#2
print(car[2]) #indexing start from 0
#3 backward indexing start from -1
print(car[-1])
print(car[-3])
#4
message=f"My first car will be a {car[-1].title()}"
print(message)
#5
print(f'{message} so i have to be very rich')
#6 adding an element in a list at end of the list
car.append('ducati')
print(car)
#7 adding element to the list with no elememt
message=[]
message.append('hello')
message.append('hi')
message.append('hola')
print(message)
#8 inserting elememnt in list in any place by indexing
car.insert(0,'honda')
car.insert(2,'audi')
print(car)
#9 removing element from list
del car[0]
del car[4]
print(car)
#10 removing item by pop fun and work with the removed item
print(car) #here list has 4 item
car_pop=car.pop()
print(car) #here the last item has been removed by pop func
print(car_pop) #here i am working with the removed item
print(car.pop()) #poped another item and printed without variable
#11
car.pop() #here i am only removing the last item making the list with 2 item
print(car)
#12
print(f'I want to bye a {car_pop.title()}.')
#13 pop by indexing
car1=car.pop(0)
print(car1)
#14 removing an item on list without knowing the index
new_car=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
new_car.remove('ducati')
print(new_car)
#15
expensive_car=new_car.remove('lambo')
print(f'{expensive_car} is very expensive.') 
#here expensive_car variable assign none cz remove fun make it none.
#16
expensive_car='audi'
new_car.remove(expensive_car)
print(f'{expensive_car.title()} is very expensive.')
#17 sort list in alphabetical order
car3=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
car3.sort()
print(car3)
#18 reverse alphabetic order
car3.sort(reverse=True) #car3.sort(reverse=1)   is also right
print(car3)
car3.sort(reverse=False) #car3.sort(reverse=0)  is also right
print(car3) #here False make the argument reverse oposite as maintaining alphabetic order.
#19 sort an list without removing the orginal order by sorted func
car4=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
print(f'here is the orginal order:{car4}')
print(f'here is the sorted order:{sorted(car4)}') # sorted(car4)  is the argument to sort temporary.
print(f'here is the orginal order again:{car4}')
#20 reversing a list order
car4.reverse()
print(car4) # it simply reverse the orginal list order
#21 finding length of a list
print(len(car4)) #python start counting of a list item from 1 so it is perfect length.
#End