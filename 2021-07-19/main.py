#Classes

class Log:

    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last

    def record_id(self, order_id):
        if self.first is None:
            self.first = order_id
            self. last = order_id
        else:
            self.last.next = order_id
            order_id.previous = self.last
            self.last = order_id

    def size(self):
        item = self.first
        size = 0
        while item.next is not None:
            item = item.next
            size += 1
        return size + (self.first is not None)

    def get_last(self, i):
        if i > self.size():
            return "Index is greater than log length!"
        ith = self.last
        while i > 1:
            ith = ith.previous
            i -= 1
        return ith.id

class Order:

    def __init__(self, id):
        self.id = id
        self.previous = None
        self.next = None


#Calls
log = Log()

for i in range(0, 20):
    new_order = Order("n" + str(i+1))
    log.record_id(new_order)

#Last
print(log.last.id)

#Ith last
print(log.get_last(2))
