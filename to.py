file = open(input())
item = ""
ps = ""
l = 0
for line in file:
   if line == "rizz:\n":
      item = "rizz"
   elif line == ":rizz\n":
      item = ""
   elif item == "rizz":
      try:
         l = len(line) - 1
         exec(str("print(") + str(line[0:l]) + str(")"))
      except:
         print(line)
   elif line == "gyatt:\n":
      item = "gyatt"
   elif line == ":gyatt\n":
      exec(ps)
      item = ""
   elif item == "gyatt":
      ps = str(ps) + str(line)
   else:
      pass
