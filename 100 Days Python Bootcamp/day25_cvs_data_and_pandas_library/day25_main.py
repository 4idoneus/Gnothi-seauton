
import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].tolist()
# avg = sum(temp_list)/ len(temp_list)
# print(avg)
# #Instead of this we can just do this.
# average = data["temp"].mean()
# max = data["temp"].max()
# print(average)
# print(max)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# print((monday_temp  * (9/5) + 32))

#Creating DataFrame fom scratch
data_dict = {
    "players": ["Aidoneus","Asterion","Gale","Shadowheart","Làzel",],
    "kills": [130,5000,100,750,1200],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)