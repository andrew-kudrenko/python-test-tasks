def max_diff_pairs(string: str) -> int:
  groups = []
  pairs = 0
  prev = None

  for s in string:
    if s != prev:
      pairs += 1
    else:
      groups.append(pairs)
      pairs = 0
    
    prev = s

  groups.append(pairs)

  return max(groups)
    

# sample = 'abcdeffgghh'
sample = '12222987654321'

print(max_diff_pairs(sample))