def negative_vs_positive(int_list):
    sum_negative = 0
    sum_positive = 0
    for item in int_list:
        if item < 0:
            sum_negative += item
        else:
            sum_positive += item
    def stronger():
        if abs(sum_negative) > sum_positive:
            return "The negatives are stronger than the positives"
        else:
            return "The positives are stronger than the negatives"
    return f"{sum_negative}\n{sum_positive}\n{stronger()}"

numbers = [int(num) for num in input().split()]

print(negative_vs_positive(numbers))