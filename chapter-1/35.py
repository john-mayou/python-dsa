import random

def main():
  for n in range(5, 101, 5):
    same_bday = 0
    bday_days = set()
    for _ in range(n):
      bday = random.randint(0, 365)
      if bday in bday_days:
        same_bday += 1
      else:
        bday_days.add(bday)
    print(f"n = {n}: {same_bday}")

if __name__ == "__main__": main()