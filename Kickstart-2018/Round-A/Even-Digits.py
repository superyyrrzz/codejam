# URL: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

def find_left_most_odd_index(n):
  res = -1
  index = 0
  remain = n
  while remain > 0:
    if remain % 2 == 1:
      res = index
    index += 1
    remain = remain // 10
  return res

# handle carry
def patch(upper, index):
  mask = 10 ** index
  if mask > upper:
    return upper
  digit = (upper // mask) % 10
  if digit == 0:
    return patch(upper, index + 1)
  elif digit == 9:
    return patch(upper + 10 ** index, index + 1)
  elif digit % 2 == 1:
    return upper + 10 ** index
  else:
    return upper

def even_digits(n):
  left_most_odd_index= find_left_most_odd_index(n)
  if left_most_odd_index == -1:
    return 0

  mask = 10 ** left_most_odd_index
  # upper: ++ odd digit, pend 0s
  upper = patch(n - n % mask + mask, left_most_odd_index)
  # lower: -- odd digit, pend 8s 
  lower = n - n % mask - mask + (mask - 1) // 9 * 8
  return min(upper - n, n - lower)

t = int(input())
for i in range(1, t + 1):
  x = int(input())
  res = even_digits(x)
  print("Case #{}: {}".format(i, res))