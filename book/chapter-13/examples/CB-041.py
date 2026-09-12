def approval_rate(approved:int, reviewed:int):
    if reviewed == 0: return None
    return approved / reviewed

assert approval_rate(8,10) == 0.8
