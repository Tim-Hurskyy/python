all_food = []
food = input (f'Enter food on any letter ').lower()
all_food.append(food)
letter = food[-1]
fails = 0

while food != 'x':
  food = input (f'Enter food on letter "{letter}" or "x" for exit ').lower()
  if food == 'x':
    break
  if food[0] != letter:
    print('wrong first letter')
    fails+= 1
    break
  if food in all_food:
    print('sorry you have wrote that food')
    fails+= 1
  else:
    all_food.append(food)
    #all_food+= (food)
    letter = food[-1]
  if fails == 3:
    print('you failed')
    break
eaten = ', '.join(all_food)
print ('Game Over!')
print(f'you have eaten: {eaten}.')
