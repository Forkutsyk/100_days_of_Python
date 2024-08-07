# import csv
import pandas

# with open('weather_data.csv', 'r') as weather:
#     data = weather.readlines()

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

data = pandas.read_csv('weather_data.csv')

# temp_list = data['temp'].to_list()
# average_temp = data['temp'].mean()
# print(round(average_temp, 2))
# print(data['temp'].max())
#
# print(data.condition)

# //Get data in Row//
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5)+32)


# create Data_Frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.cvs")
