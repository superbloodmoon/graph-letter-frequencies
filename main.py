import matplotlib.pyplot as plt
from collections import Counter
import keyboard


#----------------------------------------------#
      
input = ([*open('setinput.txt').read().lower().strip()])

input = list(map(ord, input))
input = ([i for i in input if i > 96 and i < 123])


most_common = input.count(max(set(input), key=input.count))
least_common = input.count(min(set(input), key=input.count))

print(most_common, least_common)

allnums = [chr(i) for i in range(97,123)]

y = [] #COUNTS of ALL nums - 1 per
colors = []


for i in allnums:
  y.append(input.count(ord(i)))

for i in y:
      
  if i == most_common:
    colors.append("red")
  elif i == least_common:
    colors.append("blue")
  else: 
    colors.append("gray")

  
for i in y:
  y[y.index(i)] = y[y.index(i)] / len(input) * 100


plt.bar(allnums, y, color=colors)
plt.xlabel("Letters")
plt.ylabel("Frequency (as a Percentage from Total)")
plt.title("Frequencies of English Alphabet Characters in a Given Text")

plt.show()
