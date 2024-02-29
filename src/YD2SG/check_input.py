
# Make sure input is an integer
def get_int_input(input_message):
    input_int = ""
    while input_int == "":
        try :
            input_int = int(input(input_message))
            return input_int
        except:
            print("ERROR: Input must be an integer.")