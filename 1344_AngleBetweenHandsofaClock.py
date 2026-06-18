

def angleClock(hour: int, minutes: int) -> float:
    total = 360
    
    minutes_angle = 6*minutes
    
    heure_angle = (hour%12)*30 + 30*minutes/60
    # print(minutes_angle)
    # print(heure_angle)

    if minutes_angle <= heure_angle:
        distance2 = abs(360-heure_angle) + minutes_angle
    else:
        distance2 = abs(360-minutes_angle) + heure_angle

    return min(abs(heure_angle-minutes_angle), distance2)


hour = 1
minutes = 57
print(angleClock(hour, minutes))