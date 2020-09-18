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

  if not groups:
    return pairs
  else:
    max(groups)
    

sample = 'abcdeffgghh'

print(max_diff_pairs(sample))