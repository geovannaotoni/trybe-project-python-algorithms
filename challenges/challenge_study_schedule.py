def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for start_hour, finish_hour in permanence_period:
            if start_hour <= target_time <= finish_hour:
                count += 1
        return count
    except TypeError:
        return None
