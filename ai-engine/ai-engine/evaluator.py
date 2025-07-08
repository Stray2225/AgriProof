# evaluator.py
# Dummy scoring logic for farm activities

def evaluate_farming_activity(data):
    """
    Example input:
    data = {
        'crop_type': 'maize',
        'area_hectares': 1.5,
        'activity': 'planting',
        'timestamp': '2025-07-08'
    }
    """
    score = 0

    if data.get('activity') == 'planting':
        score += 10
    if data.get('area_hectares', 0) >= 1:
        score += 5

    return {
        "user_score": score,
        "recommendation": "Approved for reward"
  }
