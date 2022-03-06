import statistics
c=[1, 5, 6.3, 6, None, 2.0, -4, None]
p=statistics.mean([i for i in c if i!= None])
print(list(map(lambda x:p if x==None else x, c) ) )
