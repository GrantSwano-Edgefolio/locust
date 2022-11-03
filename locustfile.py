from locust import HttpUser, task, between
import credentials
import testdata


class JPMCEdgeUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.request(
            method="GET",
            url="/auth/login",
            auth=credentials.DEV_AUTH)

    @task(3)
    def search_funds(self):
        self.client.get("/app/funds/")

    @task(1)
    def view_fund_groups(self):
        self.client.get("/app/fund-groups/")

    @task(6)
    def view_fund(self):
        self.client.get(f"/app/funds/{testdata.get_random_fund()}/")

    @task(1)
    def view_peers(self):
        self.client.get(f"/app/funds/{testdata.get_random_fund()}/peers/")

    @task(1)
    def view_analysis(self):
        self.client.get(f"/app/funds/{testdata.get_random_fund()}/analysis/")
