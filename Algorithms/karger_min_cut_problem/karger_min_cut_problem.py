# In this program, we use Karger's randomized algorithm for finding the cut in a given graph with the minimum
# number of edges.

import numpy as np
import re

# we use a graph in a dictionary form, where keys are the vertices and the values are list of vertices which
# form edges with the keys.

def potential_min_cut_finder(g):
    
    from random import randint, choice
    
    vertices = list(g.keys())    
    n_vertices = len(g.keys())
    
    if n_vertices == 2:

        return len(g[list(g.keys())[0]])
    
    random_vertice = choice(vertices)
    random_edge_other_vertice = choice(g[random_vertice])
    
    for vertice in g[random_edge_other_vertice]:
        
        if vertice != random_vertice:
            
            g[random_vertice].append(vertice)
            
        g[vertice].remove(random_edge_other_vertice)
                
        if vertice != random_vertice:
            
            g[vertice].append(random_vertice)
    
    del g[random_edge_other_vertice]
    
    return potential_min_cut_finder(g)

# Since this algorithm is randomized, it doesn't necessarily return the correct answer at the first time; hence,
# we simply repeat the process a number of times to find out the minimum cut value.

min_cut = None

for i in range(50):
    
    data = open('data.txt')
    
    g = {}

    for line in data:

        line_data = re.findall('\d+', line)
        g[int(line_data[0])] = []

        for v in line_data[1:]:

            g[int(line_data[0])].append(int(v))
    
    last_count = potential_min_cut_finder(g)
    
    if not min_cut or last_count < min_cut:
        
        min_cut = last_count
    
print(min_cut)

print('\nThanks for reviewing')

# Thanks for reviewing
