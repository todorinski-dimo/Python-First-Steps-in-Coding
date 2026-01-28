happiness_score = list(map(int, input().split()))
happiness_factor = int(input())
factored_score = list(map(lambda item: item * happiness_factor, happiness_score))
happy_employees = list(filter(lambda item: item >= (sum(factored_score)/len(factored_score)), factored_score))
if len(happy_employees) >= len(factored_score) / 2:
    print(f"Score: {len(happy_employees)}/{len(factored_score)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(factored_score)}. Employees are not happy!")

