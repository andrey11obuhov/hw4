import random
import statistics
sp=[random.randint(0, 100)for _ in range(10)]
print(sp)
if sp.index(min(sp))< sp.index(max(sp)):
       print( statistics.mean([i for i in sp if sp.index(min(sp))<=sp.index(i)<= sp.index(max(sp))]))

else:

    p=statistics.median([i for i in sp if sp.index(max(sp)) < sp.index(i) < sp.index(min(sp))] )
    for i in sp:
        if sp.index(max(sp)) <sp.index(i) < sp.index(min(sp)):
            sp[sp.index(i)]=p
    print(sp)
