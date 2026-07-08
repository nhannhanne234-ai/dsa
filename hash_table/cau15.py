class ConsistentHash:
    def __init__(self):
        self.ring = []
        self.servers = {}

    def hash_func(self, key):
        h = 0
        for c in str(key):
            h += ord(c)
        return h % 100

    def add_server(self, server):
        for i in range(3):
            vnode = server + str(i)
            pos = self.hash_func(vnode)
            self.ring.append(pos)
            self.servers[pos] = server
        self.ring.sort()

    def remove_server(self, server):
        remove_list = []
        for pos in self.ring:
            if self.servers[pos] == server:
                remove_list.append(pos)
        for pos in remove_list:
            self.ring.remove(pos)
            del self.servers[pos]

    def get_server(self, key):
        if len(self.ring) == 0:
            return None
        key_pos = self.hash_func(key)
        for pos in self.ring:
            if pos >= key_pos:
                return self.servers[pos]
        return self.servers[self.ring[0]]

ch = ConsistentHash()
ch.add_server("S1")
ch.add_server("S2")
ch.add_server("S3")
print(ch.get_server("user100"))
print(ch.get_server("user200"))
ch.add_server("S4")
print(ch.get_server("user100"))