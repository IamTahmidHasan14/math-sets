set1 = {1, 4, 9, 8, 6, 7, 1, 4}
print("Set1:", set1)
set2 = {1, True, 4, "Hasan", 9, 8, "Tahmid", "Tahmid"}
print("set2:", set2)

print("union:", set1.union(set2))
print("intersection:", set1.intersection(set2))
print("difference:", set1.difference(set2))
print("isdisjoint:", set1.isdisjoint(set2))
print("issuperset:", set1.issuperset(set2))
print("issubset:", set1.issubset(set2))