total_sum = 0 
even_sum = 0 
odd_sum = 0 

for number in range(1,101):
     if number % 2==0:
          even_sum += number
     else:
          odd_sum += number
print(f"Total sum of even numbers:{even_sum}")
print(f"Total sum of odd numbers:{odd_sum}")
