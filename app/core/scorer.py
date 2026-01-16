def calculate_score(signals: dict):
    if not signals:
        return 0

    total = 0
    for signal in signals.values():
        total += signal.risk

    avg_risk = total / len(signals)
    score = round((1 - avg_risk) * 100, 2)

    return score
