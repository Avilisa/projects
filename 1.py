from datetime import datetime
import random
random_list = [random.randint(1, 1000) for i in range(10000)]
before = datetime.now()

sorted_list = sorted(random_list)
print(sorted_list)
after_sorted = datetime.now()

for i in range(10-1):
    for j in range(10-i-1):
        if random_list[j] > random_list[j+1]:
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]

print(random_list)
after_bubble = datetime.now()

print('после сортировки sorted: ', after_sorted - before)
print('после сортировки bubble: ', after_bubble - after_sorted)
