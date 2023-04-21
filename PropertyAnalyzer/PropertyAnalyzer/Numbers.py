def get_even_numbers(numbers):
  evenNumbers=[]
  for num in numbers:
      if num % 2 == 0:
          evenNumbers.append(num)
  return evenNumbers

numbers=[1,2,3,4,5,6,7,8,9,10]


evenNumbers=get_even_numbers(numbers)
print(evenNumbers)