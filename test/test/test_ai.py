from ai_engine.evaluator import evaluate_farming_activity

def test_score():
    data = {
        "crop_type": "maize",
        "area_hectares": 1.2,
        "activity": "planting",
        "timestamp": "2025-07-08"
    }
    result = evaluate_farming_activity(data)
    assert result["user_score"] > 0
