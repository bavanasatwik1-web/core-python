
count = 0

for i in range(1,10):

    if i % 3 == 0:
        continue

    count += i

    if count > 10:
        break

print(count)