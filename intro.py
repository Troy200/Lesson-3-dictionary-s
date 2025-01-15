capitals={}
capitals["Netherlands"]="Amsterdam"
capitals["Sweden"]="Stockholm"
capitals["India"]="New Delhi"


print(capitals)

print(list(capitals.keys()))
print(list(capitals.values()))

del(capitals["India"])

print(capitals)

print(capitals.get("India"))

print(len(capitals))