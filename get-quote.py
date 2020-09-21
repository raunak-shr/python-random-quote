import random
def raunak():
   

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  quotes.replace("/n", " ")
  print(quotes[rnd])
  print(quotes[rnd-2])
  
if __name__== "__main__":
  raunak()
