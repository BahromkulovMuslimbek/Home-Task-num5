# # Task num 2
# class Iterable_Class:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration


# objects = Iterable_Class([2, 9, 5, 3, 7])

# for i in objects:
#     print(i)



# # Task num 3
# class Iterable_Class:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration

# def filter_odd_nums(num):
#     return num % 2 != 0


# objects = Iterable_Class([1, 2, 3, 4, 5, 6, 7, 8])
# filtered_objs = filter(filter_odd_nums, objects)

# for i in filtered_objs:
#     print(i)



# Task num 4
class Iterable_id:
    objects = []

    def __init__(self, data):
        self.data = data
        self.index = 0
        Iterable_id.objects.append(self)

    @classmethod
    def get_id(cls):
        ids = []
        for i in cls.objects:
            ids.append(id(i))
        return ids

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(Iterable_id.objects):
            result = id(Iterable_id.objects[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration


obj_1 = Iterable_id([1, 2, 3])
obj_2 = Iterable_id([4, 5, 6])
obj_3 = Iterable_id([7, 8, 9])

for obj_id in Iterable_id.get_id():
    print(obj_id)