data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
max_name_length = 11
max_score_length = 3
for name, score in data:
    print(f"{name:<{max_name_length}} = {score:>{max_score_length}}")


data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

max_name_length = max(len(name) for name, score in data)
max_score_length = max(len(str(score)) for name, score in data)

for name, score in data:
    print(f"{name:<{max_name_length}} = {score:>{max_score_length}}")


    