import numpy as np
import pandas as pd
from random import randint
import math

data = pd.read_csv('week10e.txt', names=range(19))
cum_rank = np.zeros((data.shape[0], data.shape[1]))
rank = np.zeros(30)


#Message Class
class Message:
    def __init__(self, source, destination, TTL):
        self.source = source
        self.destination = destination
        self.TTL = TTL

#Random Message GEnerate
MessageList = []        
count = 0
while count < 50:
    source = randint(1, 12)
    destination = randint(1, 12)
    if(source != destination):
        MessageList.append(Message(source, destination, 7))
        count += 1
        
#Printing Message        
for x in range(50):
    print(MessageList[x].source, MessageList[x].destination, MessageList[x].TTL)
print("Message Done")
# Rank Calculation
for row in range(data.shape[0]):
    for column in range(data.shape[1]):
        if(math.isnan(data.iloc[row][column])):
            continue
        else:
            number = int(data.iloc[row][column])
            if(number > 30):
                continue
            rank[number-1] += 1
            cum_rank[row][column] = rank[number-1]
    
print("Rank Calculation Done")
#pseudocode
deliver = 0   
for x in range(50):
    for row in range(data.shape[0]):
            if (MessageList[x].destination == data.iloc[row][1] or MessageList[x].destination == data.iloc[row][2]):             
                deliver += 1
            else:
                for new_row in range(data.shape[0]):
                    if(cum_rank[new_row][0] > 1 and cum_rank[new_row][1] > 1):
                        MessageList[x].source = data.iloc[new_row][0]
    


print(deliver)