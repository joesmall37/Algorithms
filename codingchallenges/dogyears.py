def dog_years(name, age):
   dog_age = str(age * 7)
   greeting = "Hello " + name + " You are " + str(age) + " years old in human years but you are " + dog_age + " years old in dog years"
   return greeting

print(dog_years("sam", 10))
