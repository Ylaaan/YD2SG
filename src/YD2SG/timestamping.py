import datetime

current_time=datetime.datetime.now()
    
# Returns a list element with the datetime of a day of the selected week
def get_week_date(week_number_offset, target_day_number):
    startdate = datetime.datetime.fromisocalendar(current_time.year, current_time.isocalendar().week + week_number_offset, 1)
    dates = []
    for i in range(7):
        day = startdate + datetime.timedelta(days=i)
        dates.append(day)
    return dates[target_day_number]

# Generates an epoch timespamp (in seconds), takes in a date + hours + minutes
def generate_timestamp(week,day,hour,minute):
    stream_start_time = datetime.timedelta(hours=hour,minutes=minute)
    stream_start_full_time = get_week_date(week, day) + stream_start_time
    stream_start_full_time_timestamp_in_seconds = int(stream_start_full_time.timestamp())
    return stream_start_full_time_timestamp_in_seconds