rock='''
 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''
paper='''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
          '''
scissor='''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
  '''

# condition===>>> 0 for rock ,1 for paper, 2 for scissors

import random
random_num=random.randint(0,2)
if random_num==0:
    print(rock)
elif random_num==1:
    print(paper)
else:
    print(scissor)