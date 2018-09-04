import gc


class Node:
    def __init__(self, id):
        self.id = id
        self.next = None

    def __repr__(self):
        return "Node {0}".format(self.id)


n1, n2, n3 = Node(1), Node(2), Node(3)
n1.next, n2.next, n3.next = n2, n3, n1

for ref in gc.get_referents(n2):
    print('Referent:', ref)

for ref in gc.get_referrers(n2):
    print('Referrer:', ref)
