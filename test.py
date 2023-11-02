import csv

data = [
    ["movie","rating"],
    ["starwars","4"],
    ["Jurassic Park","5"],
    ["Oppenheimer", "4"]
]

# a+ --> append
# w--> write
with open("movies.csv","a+",newline='') as info:
    content = csv.writer(info)
    content.writerows(data)