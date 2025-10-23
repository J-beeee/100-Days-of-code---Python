import pandas

data = pandas.read_csv("squirrel_data.csv")
black_squirrels = sum(data["Primary Fur Color"] == "Black")
gray_squirrels = sum(data["Primary Fur Color"] == "Gray")
cinnamon_squirrels = sum(data["Primary Fur Color"] == "Cinnamon")
color_list = {
    "Fur Color": ["black", "gray", "cinnamon"],
    "Count": [black_squirrels, gray_squirrels, cinnamon_squirrels],
}


data = pandas.DataFrame(color_list)
data.to_csv("test")
print(data)
