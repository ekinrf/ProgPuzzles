def eval_div(equations, values, queries):
    results = []

    for (dividend, divisor) in queries:
        if divisor is '0':
            results.append(-1.0)
        else:
            try:
                dividend = float(dividend)
                divsior = float(divisor)
                divsior

            except ValueError:
                results.append(-1.0)