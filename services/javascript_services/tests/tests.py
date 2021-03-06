import requests
import json


def test_pa11y():
    # local testing - run node server.js for this test
    header = {"Content-type": "application/json"}
    payload = json.dumps({"domain":"whitehouse.gov"})
    response = requests.get("http://localhost:8000",headers=header,data=payload)
    assert isinstance(response.text, str)
    assert response.status_code == 200

def test_pa11y_service():
    # local testing - run node server.js for this test
    header = {"Content-type": "application/json"}
    payload = json.dumps({"domain":"whitehouse.gov"})
    response = requests.get("https://domain-scan-javascript-services.app.cloud.gov",headers=header,data=payload)
    assert isinstance(response.text, str)
    assert response.status_code == 200
