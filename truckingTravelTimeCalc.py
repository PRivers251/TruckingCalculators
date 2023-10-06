import math
import datetime
from datetime import timedelta

appt_input = input('Input Appointment (Month / Day) Time (24 Hour Clock): ')
month = int(appt_input.split(' ')[0].split('/')[0])
day = int(appt_input.split(' ')[0].split('/')[1])
hour = int(appt_input.split(' ')[1].split(':')[0])
minute = int(appt_input.split(' ')[1].split(':')[1])
appt = datetime.datetime(datetime.date.today().year,month,day,hour,minute,00,00)


distance = int(input('Enter Distance in Miles: '))
avg_speed = 55

drive_hours = (distance / avg_speed) + ((distance / avg_speed) * 0.10)

hours_to_drive_per_day = 11
total_trip_time = 0
rest_hours = 10

if drive_hours < hours_to_drive_per_day:
    total_trip_time = drive_hours
else:
    remainder = drive_hours // hours_to_drive_per_day
    total_break_time = remainder * rest_hours
    total_trip_time = drive_hours + total_break_time

depart_time = appt - timedelta(hours=total_trip_time)

depart_time_formatted = f'You should plan to leave no later than {depart_time.strftime("%A")} {depart_time.month}/{depart_time.day} @ {depart_time.strftime("%I:%M %p")}.'
print(depart_time_formatted)