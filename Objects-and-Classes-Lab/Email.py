class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []
while command != "Stop":
    current = command.split(" ")
    sender = current[0]
    receiver = current[1]
    content = current[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()
is_sent_nums = input().split(", ")
for num in is_sent_nums:
    emails[int(num)].send()
for mail in emails:
    print(mail.get_info())