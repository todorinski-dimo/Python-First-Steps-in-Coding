work_list = input().split()
work_list = [item for item in work_list if item == item[::-1]]
search_word = input()
print(work_list)
print(f"Found palindrome {work_list.count(search_word)} times")