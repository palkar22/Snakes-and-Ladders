#snake and ladder
import random
ladder={"2":9,"7":13,"11":17,"18":20}
snake={"24":13,"8":5,"21":16,"10":1}
p1=1
p2=1
def game1():
  global p1
  dice=random.randint(1,7)
  p1=p1+dice
  if str(p1) in ladder:
    new1=ladder.get(str(p1))
    p1=new1
  if str(p1) in snake:
    new1=snake.get(str(p1))
    p1=new1
  print("player 1 new location is",p1)
  if p1<25:
    game2()
  else:
    print("player 1 wins")

def game2():
  global p2
  dice=random.randint(1,7)
  p2=p2+dice
  if str(p2) in ladder:
    new2=ladder.get(str(p2))
    p2=new2
  if str(p2) in snake:
    new2=snake.get(str(p2))
    p2=new2
  print("player 2 new location is",p2)
  if p2<25:
    game1()
  else:
    print("player 2 wins")


game1()