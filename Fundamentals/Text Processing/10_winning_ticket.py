tickets = input().split(", ")

for index in range(len(tickets)):
    tickets[index] = tickets[index].strip()


wining_chars = ['@','#','$','^']
for item in tickets:
    if len(item) != 20:
        print("invalid ticket")
        continue
    for ch in wining_chars:
            for multy in range(10, 5, -1):
                find_chars = ch * multy
                left_ticket = item[0:10]
                right_ticket = item[10:20]
                if left_ticket.find(find_chars) > -1 and right_ticket.find(find_chars) > -1 and len(find_chars) == 10:
                    message = True
                    print(f'ticket "{item}" - {len(find_chars)}{ch} Jackpot!')
                elif left_ticket.find(find_chars) > -1 and right_ticket.find(find_chars) > -1 and 6 <= len(find_chars) <= 9:
                    message = True
                    print(f'ticket "{item}" - {len(find_chars)}{ch}')
                else:
                    message = True
                    print(f'ticket "{item}" - no match')