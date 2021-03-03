
def TreeConstructor(strArr):
  parents = {}
  children = {}
  for s in strArr:
    a, b = map(int, s.replace('(', '').replace(')', '').split(','))
    if a in parents:
      return "false"
      
    else:
      parents[a] = True
      
    if b in children:
      children[b] += 1
      if children[b] > 2:
        return "false"
        
    else:
      children[b] = 1
  return "true"


# keep this function call here 
print(TreeConstructor(input(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"])))


