items =[1,4,2,7]
# for item in items:
#     print(item)

#Under the hood of for loop
iterator = items.__iter__() #iter(items)
while True:
    try:
        item= iterator.__next__()#next(iterator)
        print(item)
    except StopIteration:
        break
