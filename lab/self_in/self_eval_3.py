scores = {'Ann': 79.5, 'Beth': 64.3, 'Charlie': 81.0}
average = sum(scores.values()) / len(scores)
print(f'Average score = {average:.2f}\n'
      f'Students who receive scores more than average are')
for key in scores.keys():
    if scores.get(key) > average:
        print(key)
