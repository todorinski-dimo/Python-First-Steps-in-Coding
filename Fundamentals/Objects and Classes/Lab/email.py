class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


created_mails = []
while True:
    data = input().split()
    if data[0] == "Stop":
        break
    se, re, co = data
    email_created = Email(se, re, co)
    created_mails.append(email_created)


idxes = [int(item) for item in input().split(", ")]

for idx in idxes:
    created_mails[idx].send()

for item in created_mails:
    print(item.get_info())


