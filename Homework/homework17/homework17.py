names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
print(names)
count = 0
for i in range(len(names)):
    count += 1
    for j in range(len(names[i]) - 1):
        if isinstance(names[i], list):
            count += 1
            for k in range(len(names[i][j]) - 1):
                if isinstance(names[i][j], list):
                    count += 1
print(count)
