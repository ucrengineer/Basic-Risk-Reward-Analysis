import numpy as np
import matplotlib.pyplot as plt
from random import randint

def random():

    value = randint(1,10)

    return (value % 2)


InitialCapital = 6500
NumberOfTrades = 10
MaxLoss = .03
MaxGain = .1

gains = []

FinalCapital = [InitialCapital]
win = 0
loss = 0
i = 0
# 1/4 of trades become a gain at 10%
while i < round(NumberOfTrades):

    verdict = random()
    if verdict == True:
        #percentage = (randint(1,MaxGain*100)/100)
        percentage = MaxGain
        gain = FinalCapital[i]*percentage
        FinalCapital.append(gain + FinalCapital[i])
        print('Right!: {0}'.format(FinalCapital[-1]))
        gains.append(percentage)
        i+=1
        win +=1
        continue
    else:
        gain = FinalCapital[i]*MaxLoss
        FinalCapital.append(FinalCapital[i]-gain)
        print('Wrong!: {0}'.format(FinalCapital[-1]))
        i+=1
        loss +=1
        continue

BattingAverage = win/NumberOfTrades
if BattingAverage != 1:
    # reward/risk rato
    Expectancy = (BattingAverage*(sum(gains)/len(gains)))/((1-BattingAverage)*MaxLoss)
else:
    pass
print('*****RESULTS*****')
print('Gain/Loss: {0}%'.format(round(100*(FinalCapital[-1]/FinalCapital[0] - 1),2)))
print('Batting Stats: Wins = {0}   Loss = {1}'.format(win,loss))
print('Expectancy : {}'.format(Expectancy))
plt.figure('Gains and Losses per Trade')
plt.title('Inital Captial: {0} Max Loss: {1} Avg Gain: {2} Batting Average: {3}%'.format(InitialCapital,MaxLoss,round(sum(gains)/len(gains),2),100*win/NumberOfTrades))
plt.ylabel('Captial $')
plt.xlabel('Number of Trades')
plt.xticks(np.arange(0, 21, step=1))
plt.plot(range(NumberOfTrades+1),FinalCapital)
plt.show()
