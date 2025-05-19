import math

def calc_composite_midpoint(a, b, n, expression):
    h = (b - a) / n
    f = lambda x: evaluate_expression(expression, x)
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))

def composite_trapezoidal(a, b, n, expression):
    h = (b - a) / n
    f = lambda x: evaluate_expression(expression, x)
    sum_terms = sum(f(a + i * h) for i in range(1, n))
    return h * (0.5 * f(a) + sum_terms + 0.5 * f(b))

def composite_simpson(a, b, n, expression):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")
    h = (b - a) / n
    f = lambda x: evaluate_expression(expression, x)
    
    sum_odd = sum(4 * f(a + i * h) for i in range(1, n, 2))
    sum_even = sum(2 * f(a + i * h) for i in range(2, n-1, 2))
    
    return (h / 3) * (f(a) + sum_odd + sum_even + f(b))

def evaluate_expression(expression, x):
    try:
        expr = expression.replace('^', '**')
        expr = ''.join(c if c.isdigit() or c in 'x.' else f'*{c}' 
                      if i > 0 and expr[i-1].isdigit() and c == 'x' else c 
                      for i, c in enumerate(expr))
        return eval(expr, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                          'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
                          'pi': math.pi, 'e': math.e})
    except:
        raise ValueError(f"Invalid expression: {expression}")

def main():
    print("Numerical Integration Calculator")
    print("Choose a method:")
    print("1- Composite Midpoint Rule")
    print("2- Composite Trapezoidal Rule")
    print("3- Composite Simpson's Rule")
    print("4- All Methods")

    while True:
        try:
            choice = input("\nEnter your choice (1-4, 0 to exit): ").strip()
            if choice == '0':
                break
            
            if choice not in {'1', '2', '3', '4'}:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue
                
            a = float(input("Enter lower bound (a): "))
            b = float(input("Enter upper bound (b): "))
            if b <= a:
                print("Error: b must be greater than a")
                continue
                
            h = float(input("Enter step size (h): "))
            if h <= 0 or h > (b - a):
                print("Error: h must be positive and less than (b - a)")
                continue

            n = int((b - a) / h)
            h = (b - a) / n  # Adjust h to match exact division

            expression = input("Enter function (e.g., 'x**2', 'sin(x)', 'exp(-x)'): ").strip()
            
            try:
                if choice == '1':
                    result = calc_composite_midpoint(a, b, n, expression)
                    print(f"\nComposite Midpoint Result: {result:.8f}")
                
                elif choice == '2':
                    result = composite_trapezoidal(a, b, n, expression)
                    print(f"\nComposite Trapezoidal Result: {result:.8f}")

                elif choice == '3':
                    if n % 2 != 0:
                        print("Warning: Simpson's rule requires even n. Increasing n by 1.")
                        n += 1
                        h = (b - a) / n
                    result = composite_simpson(a, b, n, expression)
                    print(f"\nComposite Simpson's Result: {result:.8f}")

                elif choice == '4':
                    print("\n== Results Using All Methods ==")
                    midpoint_result = calc_composite_midpoint(a, b, n, expression)
                    trapezoidal_result = composite_trapezoidal(a, b, n, expression)
                    simpson_n = n + 1 if n % 2 != 0 else n
                    simpson_h = (b - a) / simpson_n
                    simpson_result = composite_simpson(a, b, simpson_n, expression)

                    print(f"Composite Midpoint Result   : {midpoint_result:.8f}")
                    print(f"Composite Trapezoidal Result: {trapezoidal_result:.8f}")
                    print(f"Composite Simpson's Result  : {simpson_result:.8f}")
                    print(f"Parameters: a={a}, b={b}, h={h:.8f}, n={n}, f(x)={expression}")

            except ValueError as e:
                print(f"Error: {e}")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()