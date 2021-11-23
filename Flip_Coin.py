import random
"""Flip Coin and print percentage of Heads and Tails"""
def flipCoin():
    heads = 0 
    tails = 0 
    for i in range(200): 
      coin=random.randint(1,2) 
      if coin==1: 
          heads+=1 
      else: 
          tails+=1 
    headspercent = (heads / 200)*100 
    tailspercent = (tails / 200)*100 
    print("Heads percent: " ,(headspercent)) 
    print("Tails percent: " , (tailspercent)) 
    
if __name__=='__main__':    
    flipCoin() 
