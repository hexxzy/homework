def calc(a, b, oper):
  match oper:
    case "/":
      return a / b if b != 0 else "Деление на 0!"
    case "*":
      return a * b
    case "-":
      return a - b
    case "+":
      return a + b
    case "**":
      return a ** b


print("Ответ: ", calc(float(input("Введите первое число: ")), float(input("Введите второе число: ")),
  input("Введите операцию: ")))