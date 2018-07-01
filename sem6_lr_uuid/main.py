from random import randint

def get_new_uuid():

  Alphabet="0123456789abcdef"
  uuid=""

  length = 36

  for i in range(length):

    if(i==8 or i==13 or i==18 or i==23):
      uuid += "-"
    else:
      uuid += Alphabet[randint(0,len(Alphabet)-1)]
  return uuid

def gen():
  lst = []
  while (True):
    uuid = get_new_uuid()
    while (lst.count(uuid) != 0):
      uuid = get_new_uuid()
    lst.append(uuid)
    yield uuid

g = gen()

g.send(None)
for i in range(1000):
  print(g.send(None))
