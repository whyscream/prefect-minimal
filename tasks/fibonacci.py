from prefect import task, flow

@task
def fib_recursive(n: int) -> int:
    """
    Compute the nth Fibonacci number.

    This is a naive recursive implementation and is not efficient for large n.
    But you can use it to demonstrate task execution in Prefect.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

@task(log_prints=True)
def fib_naive(n):
    """
    Compute the nth Fibonacci number.

    This is an iterative implementation and is efficient for large n.
    The function logs intermediate results every 1000 iterations.
    But this is a single task, nothing to parallelize here.
    """
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
        if x % 1000 == 0:
            print(f"Intermediate result Fibonacci number for n={x}: {a}")
    return a

@flow(log_prints=True)
def fibonacci_flow(n: int) -> int:
    """Flow to compute the nth Fibonacci number."""
    result =  fib_naive(n)
    print(f"The {n}th Fibonacci number is: {result}")
    return result

if __name__ == "__main__":
    fibonacci_flow.serve(name="fibonacci-flow")
