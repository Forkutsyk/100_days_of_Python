# numbers = [number*2 for number in range(1, 5)]
# print(numbers)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# uppercase_names = [name.upper() for name in names if len(name) > 5]
# print(uppercase_names)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

result = {something: len(something) for something in words}
print(result)
