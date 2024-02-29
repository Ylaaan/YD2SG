import datetime
from jinja2 import Environment, PackageLoader, select_autoescape

# Variables
yes_aliases = ["yes","Yes","YES","y","Y"]
no_aliases = ["no","No","NO","n","N"]
exit_aliases = ["exit","Exit","EXIT","quit","Quit","QUIT"]

version="0.0.1"
current_time=datetime.datetime.now()

# Functions

# Make sure input is an integer
def get_int_input(input_message):
    input_int = ""
    while input_int == "":
        try :
            input_int = int(input(input_message))
            return input_int
        except:
            print("ERROR: Input must be an integer.")
    
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

# Prints banners
def print_banner(message):
    print()
    print("=============================================================")
    print(message)
    print("=============================================================")
    print()

def YD2SG():
    # Logic
    print_banner("Welcome to Ylaan's Discord Schedule Generator v"+version)
    week = get_int_input("What week schedule do you want to generate? (0=This week; 1=Next week; etc...)\n")
    message_of_the_week = input("What is the message of the week? (This message will appear on top of the schedule.)\n")

    timestamps = []
    timestamps_relative = []
    games = []
    for day_number in range (0,7):
        print("---------------------------------------------------------------------------------------")
        print("On",get_week_date(week,day_number).strftime("%A"),)
        
        # Logic block to manage no stream days.
        is_streaming = ""
        while is_streaming not in yes_aliases and is_streaming not in no_aliases:
            is_streaming = input("Will you stream? (Yes/No)\n")
            if is_streaming in no_aliases:
                games.append("- No stream")
                timestamps.append("<t:"+str(generate_timestamp(week,day_number,0,0))+":F>")
                timestamps_relative.append("")
            elif is_streaming in yes_aliases:
                hour = get_int_input("What hour will you stream on?\n")
                minute = get_int_input("What minute will you stream on?\n")
                games.append(input("What game will you play?\n"))
                timestamps.append("<t:"+str(generate_timestamp(week,day_number,hour,minute))+":F>")
                timestamps_relative.append("(<t:"+str(generate_timestamp(week,day_number,hour,minute))+":R>)")


    print_banner("Here is your template :D copy paste it directly into discord")

    # generates the schedule from the template
    env = Environment(
        loader=PackageLoader("YD2SG"),
        autoescape=select_autoescape()
    )
    template = env.get_template("schedule_template.j2")

    print(template.render(
        message_of_the_week=message_of_the_week,
        timestamp_monday=timestamps[0],
        timestamp_monday_relative=timestamps_relative[0],
        game_monday=games[0],
        timestamp_tuesday=timestamps[1],
        timestamp_tuesday_relative=timestamps_relative[1],
        game_tuesday=games[1],
        timestamp_wenesday=timestamps[2],
        timestamp_wenesday_relative=timestamps_relative[2],
        game_wenesday=games[2],
        timestamp_thursday=timestamps[3],
        timestamp_thursday_relative=timestamps_relative[3],
        game_thursday=games[3],
        timestamp_friday=timestamps[4],
        timestamp_friday_relative=timestamps_relative[4],
        game_friday=games[4],
        timestamp_saturday=timestamps[5],
        timestamp_saturday_relative=timestamps_relative[5],
        game_saturday=games[5],
        timestamp_sunday=timestamps[6],
        timestamp_sunday_relative=timestamps_relative[6],
        game_sunday=games[6]
    ))

    print_banner("Thank you for using YDSG.")

    exit_input = ""
    while exit_input not in exit_aliases:
        exit_input = input("Type exit or quit to close the program.\n")
    exit(0)