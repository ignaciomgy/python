#http://edupython.blogspot.com/2016/06/combinaciones-permutaciones-y-otras.html

c= [3,2,1]

import collections as co
import itertools as it

def unique(list_):
       return len(set(list_)) == len(list_)

def get_combos(branches):
       by_parent = co.defaultdict(list)

       for branch in branches:
           by_parent[branch.p].append(branch)

       combos = it.product(*by_parent.values())

       return it.ifilter(lambda x: unique([b.c for b in x]), combos)
    

get_combos(c)