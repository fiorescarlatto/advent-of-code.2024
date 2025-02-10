with open("input.txt") as file:
  input = file.read().split('\n\n')

def is_lock(text):
  return text.startswith('#####')

def to_code(text, key=False):
  text = text.split('\n')
  code = ''
  stop = '#' if key else '.'
  for col in range(5):
    length = 0
    for row in range(1,7):
      length = row-1
      if text[row][col] == stop:
        break
    code += str(length)
  return code

locks = []
keys  = []

for grid in input:
  if is_lock(grid):
    locks.append(to_code(grid))
  else:
    keys.append(to_code(grid,True))

def opens(lock, key):
  lock = [int(x) for x in lock]
  key = [int(x) for x in key]
  for k,l in zip(key,lock):
    if k < l:
      return False
  return True

# print(locks, keys)

total = 0
for lock in locks:
  for key in keys:
    if opens(lock, key):
      total += 1

print(total)