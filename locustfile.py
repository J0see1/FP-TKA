from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests

    @task(1)
    def get_orders(self):
        self.client.get("/orders")

    @task(1)
    def create_order(self):
        data = {
            "product": "ProductX",
            "quantity": 5,
            "customer_name": "John Doe",
            "customer_address": "123 Main St"
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/orders", json=data, headers=headers)