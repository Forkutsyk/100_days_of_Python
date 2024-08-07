import pandas

# TASK: Count all squirrels with primary color grey, cinnamon, black and then create a new cvs from that

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

brown_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == 'Gray'])
cinnamon_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "count": [brown_fur_count, cinnamon_fur_count, black_fur_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.cvs")


