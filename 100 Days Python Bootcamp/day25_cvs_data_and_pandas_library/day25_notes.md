#### Handling CSV DATA
Python has usage for many things ut one of the most popular usages is handling data.
When we are handling data as we saw before ,day 24, it's long to get a single file to clean up.
So there is other helpers we can use. When the data format of our data is .cvs we can use local library csv.
 ###### Example
From this
```python
with open("weather_data.csv") as data_file:
    data_list = data_file.readlines()
   
print(data_list)
```
To this
```python
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temps = []
    for row in data:
        if data.line_num == 1:
            continue
        else:
            temps.append(int(row[1]))
print(temps)
```
#### Pandas
But it's a lot of code to get just the temp numbers as an integer.
lucky for us there is a better way. With the help of this black and white fluffy friends. We can handle data way better with less code.
Let me introduce to you pandas. The package all data lovers adore.
Because it turns the code above to this and get the same result but better.
```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(data)
```
In pandas there is a two important data,object, type 
1. Data Frame = This is kinda equivalent of your whole table.
2. Series = This is the column of your tables. And series are the equivalent of a list

There is a lot of thing we can do in pandas. And there is a lot of method we can use . So the documentation reading is 
so important. pandas documentation link: [Pandas Documentation](https://pandas.pydata.org/docs/index.html)
###### Example
```python
import pandas

data = pandas.read_csv("weather_data.csv")
#To turn your dataFrame to dictionary
data_dict = data.to_dict()
print(data_dict)
#To turn your series to list
temp_list = data["temp"].tolist()
avg = sum(temp_list)/ len(temp_list)
print(avg)
#Instead of this we can just do this.
average = data["temp"].mean()
print(average)
```