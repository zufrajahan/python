from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro , to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f" train no {self.trainNo} is running on time")

    def getFare(self, fro , to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12345)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")