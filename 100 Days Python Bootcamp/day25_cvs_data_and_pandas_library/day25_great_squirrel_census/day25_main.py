import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour" : ["Grey","Cinnamon","Black"],
    "Count" : [grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")