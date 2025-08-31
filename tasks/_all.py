from prefect import serve

from customers import process_customers
from fibonacci import fibonacci

if __name__ == "__main__":
    customers_deployment = process_customers.to_deployment(name="deployment_process_customers")
    fibonacci_deployment = fibonacci.to_deployment(name="deployment_fibonacci")

    serve(customers_deployment, fibonacci_deployment)
