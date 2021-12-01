scores = [3, 4 ,21 ,36 ,10, 28 ,35 ,5 ,24, 42]
# scores = [0 ,9 ,3 ,10, 2, 20]
# print("aa")
max = 0
i = 0
count = 0
while i < len(scores):
    if scores[i] > max:
        max = scores[i]
        count = count + 1
    i = i + 1
print(count-1)

min=scores[0]
j=0
count_1=0
while j<len(scores):
    if scores[j]<min:
        min=scores[j]
        count_1=count_1+1
    j=j+1
print(count_1)

    
    



