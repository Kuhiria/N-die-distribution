import os
import random
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool
import threading
import itertools
import sys
 
done = False

def clear():
    os.system("cls")
clear()

def TirarDado():
    return random.randint(1,6)

def DisplayChart():

    xAxis = [n for n, _ in enumerate(combinaciones_posibles)]
    plt.bar(xAxis, histograma, color='teal')
    plt.title('Score combination Vs Number of occurences', fontsize=14)
    plt.xlabel('Score combination', fontsize=14)
    plt.ylabel('Number of occurences', fontsize=14)
    plt.xticks([n for n, _ in enumerate(combinaciones_posibles)], combinaciones_posibles)
    plt.show()

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rComputing ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# Ask for number of dice
while True:
    try:
        n = int(input("Enter a number of dice: "))
        while n < 0:
            clear()
            print("You cannot have a negative number of dice! Try again.\n")
            n = int(
                input("Enter a number of dice: "))
        break
    except:
        clear()
        print("Invalid input, try again.\n")

clear()
# Ask for number of iterations
while True:

    try:
        iterations = int(input("Enter an amount of dice throw iterations: "))
        while iterations < 0:
            clear()
            print("You cannot have a negative amount of iterations! Try again.\n")
            iterations = int(
                input("Enter an amount of dice throw iterations: "))
        break
    except:
        clear()
        print("Invalid input, try again.\n")

clear()

# これはへたです！
# Creation of histogram
histograma = [0] * (6*n + 1)
combinaciones_posibles = list(range((6 * n) + 1))
clear()

# Stopwatch for computing time
t = threading.Thread(target=animate)
t.start()
start = time.time()


# Dice throw and list storing
for i in range(iterations): 
    suma = 0
    for j in range(n):
        suma = suma + TirarDado()
    histograma[suma] += 1

# End stopwatch
end = time.time()
done = True
clear()

# Display result
print(f"Done!\n{end-start:.5f}s")
DisplayChart()


