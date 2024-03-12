
cities ={"Mumbai","Delhi","Chennai","Banglore","Gujarat",""}
subcities ={"Ghatkopar","Ahamdabad","Ranchi","Panjab","Gujarat"}
States={"Satara","Gujarat","UP","Mhaharashtra","Pune"}
Cities = cities.intersection(subcities)
print(Cities)
cities.update(subcities)
print(cities)
Cities = cities.symmetric_difference(subcities)
print(Cities)
Cities = cities.isdisjoint(subcities)
print(Cities)
a=States.union(cities)
print(a)
Cities = cities.issubset(a)
print(Cities)
cities.add("Ayodhya")
print(cities)
cities.pop()
print(cities)
cities.update(subcities)
print(cities)
cities.remove("Gujarat")
print(cities)
cities.discard("Gujarat")
print(cities)
cities.clear()
print(cities)
if "Rajkot" in cities:
    print("Chennai is prezent the set")
else:
    print("Not in the list")
