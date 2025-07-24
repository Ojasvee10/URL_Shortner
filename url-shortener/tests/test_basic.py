import pytest
from app.main import app, storage

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_shorten_valid_url(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    assert res.status_code == 201
    data = res.get_json()
    assert "short_code" in data and "short_url" in data

def test_shorten_invalid_url(client):
    res = client.post("/api/shorten", json={"url": "invalid-url"})
    assert res.status_code == 400

def test_redirect_existing(client):
    res = client.post("/api/shorten", json={"url": "https://www.linkedin.com/jobs/view/4267669976/?trackingId=&refId=&midToken=AQEKCfHIZwEGtA&midSig=1kfbIpaw-CVrQ1&trk=eml-email_jobs_job_application_viewed_01-applied_jobs-0-applied_job&trkEmail=eml-email_jobs_job_application_viewed_01-applied_jobs-0-applied_job-null-hgybl0~mdh0kbv0~lt-null-null&eid=hgybl0-mdh0kbv0-lt&otpToken=MTMwNTFiZTYxNjJlYzljNWIyMmEwZmViNDExYmU0Yjc4Y2M2ZDY0NDlkYWU4NzY5N2JjZjA0Njc0YTVlNWRmMmYzZDBkNmU5NGJjOWUwZTA2M2FiZjdjN2ZhMzg0MjI4M2YyNmNjMWE2Njk2NjlmNzU1Y2NjYzc2LDEsMQ%3D%3D"})
    code = res.get_json()["short_code"]
    res = client.get(f"/{code}", follow_redirects=False)
    assert res.status_code == 302
    assert res.headers["Location"] == "https://www.linkedin.com/jobs/view/4267669976/?trackingId=&refId=&midToken=AQEKCfHIZwEGtA&midSig=1kfbIpaw-CVrQ1&trk=eml-email_jobs_job_application_viewed_01-applied_jobs-0-applied_job&trkEmail=eml-email_jobs_job_application_viewed_01-applied_jobs-0-applied_job-null-hgybl0~mdh0kbv0~lt-null-null&eid=hgybl0-mdh0kbv0-lt&otpToken=MTMwNTFiZTYxNjJlYzljNWIyMmEwZmViNDExYmU0Yjc4Y2M2ZDY0NDlkYWU4NzY5N2JjZjA0Njc0YTVlNWRmMmYzZDBkNmU5NGJjOWUwZTA2M2FiZjdjN2ZhMzg0MjI4M2YyNmNjMWE2Njk2NjlmNzU1Y2NjYzc2LDEsMQ%3D%3D"

def test_redirect_not_found(client):
    res = client.get("/abcdef")
    assert res.status_code == 404

def test_stats(client):
    res = client.post("/api/shorten", json={"url": "https://pytest.org"})
    code = res.get_json()["short_code"]

    # Click twice
    client.get(f"/{code}")
    client.get(f"/{code}")

    res = client.get(f"/api/stats/{code}")
    data = res.get_json()
    assert res.status_code == 200
    assert data["clicks"] == 2
    assert data["url"] == "https://pytest.org"
    assert "created_at" in data
