#intro
print("welcome to kg/m counter for black zinc coated pipes please only use calculation in mm")
print("only two diameter ranges allowed")
x = 0.02466
#input
print("kg/m= 1")
operator = input("please enter the what you want to find=")
wallthickness = float(input("wall thickness:"))
if operator == "1":
  rangedia = input("does your diameter have maximum and minmum? :")
  if rangedia == "yes":
    maxdia = float(input("max diameter:"))
    mindia = float(input("min diameter:"))
    avgdia = (maxdia + mindia)/2
    diff = float(avgdia - wallthickness)
    print("avg diameter=", avgdia)
    resultsavg = x * wallthickness * diff
    print("kg/m=", resultsavg)
  elif rangedia == "no":
    diameter = float(input("diameter:"))
    diff = float(diameter - wallthickness)
    results420 = x * wallthickness * diff
  print("kg/m=", results420)
else:
  print("there was a invalid input please try again")
    


  

  



