def needs_review(confidence: float, threshold: float=0.80):
    return confidence < threshold

assert needs_review(0.55) is True
assert needs_review(0.95) is False
