import math
import datetime

distance = int(input('Enter Distance in Miles: '))
avg_speed = 55

drive_hours = (distance / avg_speed) + ((distance / avg_speed) * 0.08)

hours_to_drive_per_day = 11
total_trip_time = 0
rest_hours = 10

if drive_hours < hours_to_drive_per_day:
    total_trip_time = drive_hours
else:
    remainder = drive_hours // hours_to_drive_per_day
    total_break_time = remainder * rest_hours
    total_trip_time = drive_hours + total_break_time


print(math.ceil(total_trip_time))