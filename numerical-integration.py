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

    while True:
        try:
            choice = input("\nEnter your choice (1-3, 0 to exit): ").strip()
            if choice == '0':
                break
            
            if choice not in {'1', '2', '3'}:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
                
            a = float(input("Enter lower bound (a): "))
            b = float(input("Enter upper bound (b): "))
            if b <= a:
                print("Error: b must be greater than a")
                continue
                
            n = int(input("Enter number of subintervals (n): "))
            if n <= 0:
                print("Error: n must be positive")
                continue
            if choice == '3' and n % 2 != 0:
                print("Warning: n should be even for Simpson's rule. Adding 1 to make it even.")
                n += 1
                
            expression = input("Enter function (e.g., 'x**2', 'sin(x)', 'exp(-x)'): ").strip()
            
            try:
                if choice == '1':
                    result = calc_composite_midpoint(a, b, n, expression)
                    method = "Composite Midpoint"
                elif choice == '2':
                    result = composite_trapezoidal(a, b, n, expression)
                    method = "Composite Trapezoidal"
                else:
                    result = composite_simpson(a, b, n, expression)
                    method = "Composite Simpson's"
                
                print(f"\n{method} Result: {result:.8f}")
                print(f"Parameters: a={a}, b={b}, n={n}, f(x)={expression}")
                
            except ValueError as e:
                print(f"Error: {e}")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()