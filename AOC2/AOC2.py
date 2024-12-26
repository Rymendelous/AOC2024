with open(r"C:\Users\user\Desktop\AOC2024\AOC2\input2.txt", 'r') as file:
    lines = file.readlines()
    arrays = [list(map(int, line.split())) for line in lines]

def identique():
    global arrays
    arrays = [array for array in arrays if len(array) == len(set(array))]

def difference():
    global arrays
    arrays = [array for array in arrays if all(abs(array[i] - array[i+1]) <= 3 for i in range(len(array) - 1))]

def increasing():
    global arrays
    arrays = [array for array in arrays if all(array[i] <= array[i+1] for i in range(len(array) - 1))]

def decreasing():
    global arrays
    arrays = [array for array in arrays if all(array[i] >= array[i+1] for i in range(len(array) - 1))]

identique()
difference()
increasing()
arrays_inc = arrays[:]

#obligé je recharge pour faire le filtre sur decreasing sans increasing
with open(r"C:\Users\user\Desktop\AOC2024\AOC2\input2.txt", 'r') as file:
    lines = file.readlines()
    arrays = [list(map(int, line.split())) for line in lines]

identique()
difference()
decreasing()
arrays_dec = arrays[:]  #une copie comme ça je garde mes resultat intermediaire

#On combine les resultat apres avoir filtré
val = list(set(map(tuple, arrays_inc + arrays_dec)))

print("The number of safe reports is :", len(val))

    


           







