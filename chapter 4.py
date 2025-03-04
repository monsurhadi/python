#1 loop
cars=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
for car in cars:  #here list element of cars are assigned in car variable by each at a time.
    print(car) #then by print fun we print the each item one by one
#2
print("   ") #spacing
cars=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
for variable in cars: #here variable in cars is correct but car in cars is a convention for easiness.
    print(variable)
#3 adding note by each item
cars=['honda', 'marcedys', 'audi', 'ferrari', 'lambo', 'ducati']
for car in cars:
    print(f"{car.title()},that is a nice car.")
    print(f"I can't wait to bye it\n")
print('out of the for lop')
#4
