from functools import reduce

def unique(seq: list) -> list:
  accumulator = []

  for item in seq:
    if not item in accumulator:
      accumulator.append(item)

  return accumulator

def unique_reduce(seq: list) -> list: 
  return reduce(lambda acc, el: acc + [el] if not el in acc else acc, seq, [])

sequence = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 1, 1, 1, 5, 5, 1, 1, 2]

print(unique(sequence))
print(unique_reduce(sequence))