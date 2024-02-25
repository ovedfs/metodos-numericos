a = int(input('Ingresa el valor de a: '))
b = int(input('Ingresa el valor de b: '))
e = 1 # dato arbitrario
i = 1

def polinomio(l):
  return l * (l * (l - 6) + 4) + 5

while e >= 0.01:
  if i > 1:
    if(f_a * f_x > 0):
      a = x
      x0 = x
    else:
      b = x
      x0 = x

  x = (a + b) / 2 # Bisección
  f_a = polinomio(a)
  f_b = polinomio(b)
  # x = (a * f_b - b * f_a) / (f_b - f_a) # falsa posición
  f_x = polinomio(x)

  if i > 1:
    e = abs(x - x0)
    data = {'a': a, 'b': b, 'x': x, 'f_a': f_a, 'f_b': f_b, 'f_x': f_x, 'e': e, 'i': i}
  else:
    data = {'a': a, 'b': b, 'x': x, 'f_a': f_a, 'f_b': f_b, 'f_x': f_x}

  print(data)
  i = i + 1
