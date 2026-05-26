from fastapi.testclient import TestClient

from backend.app.main import create_app

client = TestClient(create_app())


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_match_placeholder_returns_empty_matches() -> None:
    response = client.post(
        "/api/v1/recommendations/match",
        json={
            "sop": {
                "title": "Robotics research plan",
                "text": (
                    "I want to research human-robot interaction and adaptive control "
                    "for assistive robots."
                ),
                "language": "en",
                "target_fields": ["robotics", "human-robot interaction"],
            },
            "top_k": 5,
            "min_score": 0.2,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["matches"] == []
    assert payload["retrieval_strategy"] == "placeholder"
    assert payload["query_id"]
