import random

ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
  sentence = "I will not steal the chalk from the classroom."
  err_frequency = 100 // 8
  for i in range(1, 101):
    if i % err_frequency == 0:
      s = sentence
      err_i = random.randint(0, len(s) - 1)
      err_ch = sentence[err_i]
      new_ch = None
      if err_ch.isupper():
        while True:
          new_ch = ALPHA_UPPER[random.randint(0, 25)]
          if new_ch != err_ch: break
      else:
        while True:
          new_ch = ALPHA_LOWER[random.randint(0, 25)]
          if new_ch != err_ch: break
      s_list = list(s)
      s_list[err_i] = new_ch
      s = "".join(s_list)
      print(f"{i}: {s}")
    else:
      print(f"{i}: {sentence}")

if __name__ == "__main__": main()