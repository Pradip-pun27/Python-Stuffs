class Sliding_Window:
    def __init__(self,data,size):
        self.size = size
        self.List_Num = data
        self.idx =0

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.idx + self.size)> len(self.List_Num):
            raise StopIteration
        
        window = self.List_Num[self.idx:(self.idx+self.size)]
        self.idx+=1
        return window
    
Nums = (1,2,3,4,5,6,7,8,9,10)
windows = Sliding_Window(Nums,3)

for w in windows:
    print(w)

# iterator = iter(windows)
# while True:
#     try:
#         w = next(iterator)
#         print(w)
#     except StopIteration:
#         break

