import random
from random import randint


class Deque(object):

    def __init__(self, maxi):

        self.current_size = 0
        self.first = -1
        self.last = -1
        self.MaxArraySize = maxi
        self.queue = [None] * maxi

    def add_to_front(self, x):

        if self.isFull():
            return False
        if self.isEmpty():
            self.first = 0
            self.last = 0
            self.queue[self.first] = x
            self.current_size += 1
            return True

        self.first -= 1
        if self.first == -1:
            self.first = self.MaxArraySize - 1
        self.queue[self.first] = x
        self.current_size += 1

        return True

    def add_to_back(self, x):

        if self.isFull():
            return False
        if self.isEmpty():
            self.first = 0
            self.last = 0
            self.queue[self.last] = x
            self.current_size += 1
            return True

        self.last = (self.last + 1) % self.MaxArraySize
        self.queue[self.last] = x
        self.current_size += 1

        return True

    def remove_front(self):

        if self.isEmpty():
            return False

        self.first = (self.first + 1) % self.MaxArraySize
        self.current_size -= 1
        if self.isEmpty():
            self.first = -1
            self.last = -1

        return True

    def remove_back(self):

        if self.isEmpty():
            return False

        self.last -= 1
        self.current_size -= 1
        if self.isEmpty():
            self.first = -1
            self.last = -1
            return True

        if self.last == -1:
            self.last = self.MaxArraySize - 1

        return True

    def getFrontElement(self):
        if self.isEmpty():
            return -1

        return self.queue[self.first]

    def getBackElement(self):
        if self.isEmpty():
            return -1
        return self.queue[self.last]

    def isEmpty(self):

        return self.current_size == 0

    def isFull(self):
        return self.current_size == self.MaxArraySize


instance1 = Deque(20)

print("half full deque")
for _ in range(10):
    value = randint(0, 100)
    instance1.add_to_front(value)
    print(instance1.getFrontElement(), end=" ")

print("")
print("Current Size:", instance1.current_size)

instance2 = Deque(20)


def frontSim(prob):
    print("Front Simulation")

    value3 = (random.uniform(0, 100) * 3) % 100

    if prob <= 0.1:
        instance2.add_to_front(value3)
        print(value3, "was added to Front Index")
    elif prob <= 0.2 and not (instance2.isEmpty()):
        removed = instance2.getFrontElement()
        instance2.remove_front()
        print(removed, "was remove from Front Index")
    else:
        print("Nothing Happened")
    if not (instance2.isEmpty()):
        print("Front element ", instance2.getFrontElement())
    print("Current Size:", instance2.current_size)
    if instance2.isEmpty():
        print("Deque is empty")
    if instance2.isFull():
        print("Deque is full")


def backSim(prob):
    print("Back Simulation")

    value2 = (random.uniform(0, 100) * 2) % 100

    if prob <= 0.1:
        instance2.add_to_back(value2)
        print(value2, "was added to Back Index")
    elif prob <= 0.6 and not (instance2.isEmpty()):
        removed = instance2.getBackElement()
        instance2.remove_back()
        print(removed, "was remove from Back Index")
    else:
        print("Nothing Happened")
    if not (instance2.isEmpty()):
        print("Back element ", instance2.getBackElement())
    print("Current Size:", instance2.current_size)
    if instance2.isEmpty():
        print("Deque is empty")
    if instance2.isFull():
        print("Deque is full")


instance3 = Deque(20)


def frontSim2(prob):
    print("Front Simulation")

    value5 = (random.uniform(0, 100) * 5) % 100

    if prob <= 0.1:
        instance3.add_to_front(value5)
        print(value5, "was added to Front Index")
    elif prob <= 0.6 and not (instance3.isEmpty()):
        removed = instance3.getFrontElement()
        instance3.remove_front()
        print(removed, "was remove from Front Index")
    else:
        print("Nothing Happened")
    if not (instance3.isEmpty()):
        print("Front element ", instance3.getFrontElement())
    print("Current Size:", instance3.current_size)
    if instance3.isEmpty():
        print("Deque is empty")
    if instance3.isFull():
        print("Deque is full")


def backSim2(prob):
    print("Back Simulation")

    value4 = (random.uniform(0, 100) * 4) % 100

    if prob <= 0.1:
        instance3.add_to_back(value4)
        print(value4, "was added to Back Index")
    elif prob <= 0.2 and not (instance3.isEmpty()):
        removed = instance3.getBackElement()
        instance3.remove_back()
        print(removed, "was remove from Back Index")
    else:
        print("Nothing Happened")
    if not (instance3.isEmpty()):
        print("Back element ", instance3.getBackElement())
    print("Current Size:", instance3.current_size)
    if instance3.isEmpty():
        print("Deque is empty")
    if instance3.isFull():
        print("Deque is full")


for sim1 in range(50):
    vfProb = random.uniform(0, 1)
    vbProb = random.uniform(0, 1)
    print("-------------------------")
    print("1st Deque")
    print("-------------------------")
    frontSim(vfProb)
    print("-------------------------")
    backSim(vbProb)
    print("***************************************************************************")

for sim2 in range(50):
    vfProb2 = random.uniform(0, 1)
    vbProb2 = random.uniform(0, 1)

    print("-------------------------")
    print("2nd Deque")
    print("-------------------------")
    frontSim2(vfProb2)
    print("-------------------------")
    print("-------------------------")
    backSim2(vbProb2)
    print("*****************************************************************************")
