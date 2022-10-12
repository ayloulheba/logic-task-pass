# count how many character repeated in a string

s="machine learning"

print([(i,s.count(i)) for i in set(s)])