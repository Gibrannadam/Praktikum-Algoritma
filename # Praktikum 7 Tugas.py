# Praktikum 7 Tugas

def ordinal_indicator(number):
  """Mengembalikan ordinal indicator untuk sebuah angka.

  Args:
    number: Angka bulat positif.

  Returns:
    String yang berisi ordinal indicator.
  """

  if 10 <= number % 100 <= 20:
    return str(number) + "th"
  else:
    last_digit = number % 10
    if last_digit == 1:
      return str(number) + "st"
    elif last_digit == 2:
      return str(number) + "nd"
    elif last_digit == 3:
      return str(number) + "rd"
    else:
      return str(number) + "th"

while True:
  try:
    number = int(input(">>"))
    print(ordinal_indicator(number))
  except ValueError:
    print("Masukkan angka yang valid.")