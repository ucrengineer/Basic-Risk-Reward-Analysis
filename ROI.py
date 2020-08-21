""" This displays the optimal gain/loss ratio based on consecutive gains
and losses """
import numpy as np
import matplotlib.pyplot as plt
import operator


def analyze(NumberOfTrades,RRratio,GainPerc,LossPerc,BattingAverage):
    # with n batting average
    for gain in GainPerc:
        TotalCash.append(np.power((1+gain),BattingAverage*NumberOfTrades))

    i =0
    while i < len(LossPerc):

        FinalCash = (TotalCash[i])*(np.power((1-LossPerc[i]),((1-BattingAverage)*NumberOfTrades)))
        TotalPerc.append(100* (FinalCash - 1))
        i +=1

    index,value = max(enumerate(TotalPerc),key = operator.itemgetter(1))
    print(value,GainPerc[index],LossPerc[index])

    plt.plot(range(0,len(GainPerc)),TotalPerc)
    plt.grid()
    plt.title('@ {0}% Batting Average, {1} Reward/Risk & {2} Number of Trades'.format(\
        round(BattingAverage,2),round(RRratio,2),round(NumberOfTrades,2)))
    plt.xlabel('Length of Gain Percentages Calculated')
    plt.ylabel('% ROI')
    plt.text(len(GainPerc)*.5,max(TotalPerc),'Max ROI %: {0}'.format(value))
    plt.text(len(GainPerc)*.5,max(TotalPerc)-5,'Optimal Gain %: {0}'.format(100*GainPerc[index]))
    plt.text(len(GainPerc)*.5,max(TotalPerc)-10,'Optimal Loss %: {0}'.format(100*LossPerc[index]))
    plt.show()



TotalCash = []
FinalCash= []
TotalPerc = []
NumberOfTrades = 10
LossPerc = []
BattingAverage= .4
AverageGain = .12
AverageLoss = .06
RRratio = (BattingAverage*AverageGain)/((1-BattingAverage)*AverageLoss)

GainPerc = [float(x)/100 for x in range(4,102,2)]
for each in GainPerc:
    LossPerc.append(each/RRratio)
print('GL Ratio: {0}'.format(AverageGain/AverageLoss))
analyze(NumberOfTrades,RRratio,GainPerc,LossPerc,.4)
"""Moral of the Story...CUT YOUR LOSSES AT 6% OR LESS"""
