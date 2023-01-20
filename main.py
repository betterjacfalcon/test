file = open('./input.txt', 'r+')
f = open('./output.txt', 'r+')

IGUAL = ' = '
EXCEPTION = 'Error'

for i in file.name:
  fileLine = file.readline()
  size = len(fileLine)

  if (fileLine[1:2].isspace() or not (fileLine[1:2].isdigit())):
    fileLine_1 = fileLine[0]
  else:
    fileLine_1 = fileLine[0:2]

  fileLine_n = fileLine[size - 2:size - 1]

  if fileLine_1.isnumeric() & fileLine_n.isnumeric() or size == 1:
    if "+" in fileLine:
      resultado = int(fileLine_1) + int(fileLine_n)      
      f.write(fileLine_1 + ' + ' + fileLine_n + IGUAL + str(resultado)+'\n')
    elif "-" in fileLine:
      resultado = int(fileLine_1) - int(fileLine_n)
      f.write(fileLine_1 + ' - ' + fileLine_n + IGUAL + str(resultado)+'\n')
    elif "*" in fileLine:
      resultado = int(fileLine_1) * int(fileLine_n)
      f.write(fileLine_1 + ' * ' + fileLine_n + IGUAL + str(resultado)+'\n')
    elif "/" in fileLine:
      resultado = int(fileLine_1) / int(fileLine_n)
      f.write(fileLine_1 + ' / ' + fileLine_n + IGUAL + str(resultado)+'\n')
    elif ";" in fileLine:
      f.write(EXCEPTION+'\n')
    elif "=" in fileLine:
      break
  else:
    f.write(EXCEPTION+'\n')
