#Jeu de la vie

import time
import os
import copy

def initialise():
    print("Input generation 0 with # for living cells and spaces for dead cells, for example:\n # \n## \n#  \n\nInput empty line to validate, your input:")
    gen0 = []
    i=0
    while True:
        line = input()
        if line:
            gen0.append(list(line))
        else:
            break
    for row in gen0:
        for cell in row:
            if cell not in (' ','#'):
                os.system('cls')
                print("Invalid cell input\n")
                return initialise()
    if not (gen0):
        os.system('cls')
        print("Empty input\n")
        return initialise()
    os.system('cls')
    return reformat(gen0)

def reformat(gen):
    max_length = 0
    for row in gen:
        if (len(row) > max_length):
            max_length = len(row)
    for row in gen:
        diff = max_length - len(row)
        if(diff>0):
            for i in range(diff):
                row.append(' ')
    return gen
  
def pad(gen):
    for row in gen:
        row.insert(0,' ')
        row.append(' ')
    gen.append([' ']*len(gen[0]))
    gen.insert(0,[' ']*len(gen[0]))
    return gen

def unpad(gen):
    min_i=len(gen)
    max_i=-1
    min_j=len(gen[0])
    max_j=-1
    for i in range(len(gen)):
        for j in range(len(gen[0])):
            if(gen[i][j]=='#'):
                if(i<min_i):
                    min_i=i
                if(i>max_i):
                    max_i=i
                if(j<min_j):
                    min_j=j
                if(j>max_j):
                    max_j=j
    gen = gen[min_i:max_i+1]
    for i in range(len(gen)):
        gen[i] = gen[i][min_j:max_j+1]
    return gen                
  
def generate_new(gen):
    gen = pad(gen)
    new_gen = copy.deepcopy(gen)
    for i in range(len(gen)):
        for j in range(len(gen[0])):
            neighbours = get_neighbours(gen,i,j)
            if(neighbours == 3):
                new_gen[i][j] = '#'
            elif(neighbours != 2):
                new_gen[i][j] = ' '
    return unpad(new_gen)

def get_neighbours(gen, i, j):
    neighbours = 0
    for x_offset in (-1,0,1):
        for y_offset in (-1,0,1):
            if (not(x_offset==0 and y_offset==0) 
                and j+y_offset>=0 and j+y_offset<len(gen[0])
                and i+x_offset>=0 and i+x_offset<len(gen) 
                and gen[i+x_offset][j+y_offset]=='#'):
                neighbours+=1
    return neighbours

gen = initialise()
for i in range(1000):
    gen = generate_new(gen)
    print("Iteration "+str(i+1)+":\n")
    for row in gen:
        print(''.join(row))
    print()
    time.sleep(.1)
    
    