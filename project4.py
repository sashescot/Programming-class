import random

trialnum = 0

while(trialnum < 1000):
    counter = 0 
    roll_die = 0 

    while(roll_die != 6):
        counter = counter + 1 
        roll_die = random.randint(1,6)
        print(counter)
        trialnum += 1
    
average = counter + roll_die // trialnum
print("On average it took", average, "tries to roll a 6")