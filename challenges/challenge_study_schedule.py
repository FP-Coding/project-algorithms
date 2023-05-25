def study_schedule(permanence_period, target_time):
    if not target_time and target_time != 0:
        return None
    count = 0
    for start, end in permanence_period:
        if not start or not end or type(start) != int or type(end) != int:
            return None
        if start <= target_time <= end:
            count += 1
    return count
