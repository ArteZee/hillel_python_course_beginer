# get amount of the day and hour
earth_day_hour = input().split(", ")

day_earth: float = (int(earth_day_hour[0]) + int(earth_day_hour[1]) / 24)

one_straws_in_earth = 1.02595675

mars_straws = round(day_earth * one_straws_in_earth, 2)

print(mars_straws)

