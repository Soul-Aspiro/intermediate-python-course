import random
def main():
  dice_rolls=int(input("Enter the no of rolls: "))
  dice_sum=0
  for i in range(0,dicerolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum+=roll
  print(f'You have rolled total {dice_sum}')

if __name__== "__main__":
  main()
