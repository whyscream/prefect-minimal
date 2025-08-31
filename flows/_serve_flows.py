from prefect import serve

from customers import process_customers
from fibonacci import fibonacci

if __name__ == "__main__":
    flows = [
        process_customers,
        fibonacci,
    ]

    deployments = []
    for flow in flows:
        deployment = flow.to_deployment(name=flow.__name__)
        deployments.append(deployment)

    serve(*deployments)
