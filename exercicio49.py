def fibonacci(n):
  """
  Função para gerar a sequência de Fibonacci até o n-ésimo termo.

  Args:
    n: O número de termos a serem gerados.

  Returns:
    Uma lista contendo os n primeiros termos da sequência de Fibonacci.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [1]
  else:
    fib_list = [1, 1]
    while len(fib_list) < n:
      next_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(next_fib)
    return fib_list