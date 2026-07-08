class ArrayList:
    def __init__(self):
        self.data = []
        self.mod_count = 0

    def add(self, value):
        self.data.append(value)
        self.mod_count += 1

    def remove(self, index):
        del self.data[index]
        self.mod_count += 1

    def __iter__(self):
        return ArrayListIterator(self)


class ArrayListIterator:
    def __init__(self, arr_list):
        self.arr_list = arr_list
        self.index = 0
        self.expected_mod_count = arr_list.mod_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.expected_mod_count != self.arr_list.mod_count:
            print("boom, đang duyệt mà sửa, dừng lặp giờ")
            raise StopIteration 
        if self.index >= len(self.arr_list.data):
            raise StopIteration
        val = self.arr_list.data[self.index]
        self.index += 1
        return val

a = ArrayList()
a.add(10)
a.add(20)
a.add(30)
for x in a:
    print(x)