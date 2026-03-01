import random


def get_numbers_ticket(min, max, quantity):
        numbers = []
        if min >= 1 and max <=1000 and quantity <= (max - min + 1) :
           numbers = random.sample(range(min, max + 1), quantity)
           numbers.sort()
           return numbers
          
        else:            
             return numbers
        

result = get_numbers_ticket(1, 1000, 100)

print("Ваші лотерейні числа:", result)

