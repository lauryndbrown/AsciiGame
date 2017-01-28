"""
User Input Tools for the ASCII Game Class 
"""
YES = "Y"
NO = "N"
YES_OR_NO = {YES:True,NO:False}
def yes_or_no(message):
    """
    Helper Function that handles user input for yes or no questions
    """
    while True:
        response = input(message)
        if response==YES or response==NO:
            return YES_OR_NO[response]
def are_you_sure(message):
    """
    Helper Function that confirms user input for freeform fields
    """
    while True:
        response = input(message)
        certain = yes_or_no("Are you sure "+response+" is ok?")
        if certain==True:
            return response
def enter_next_action(message, choices, display, should_confirm=False):
    """
    Helper Function that handles user input for Controls
    """
    response = input(message)
    while True:
        if response.isdigit():
            response = int(response)
        if response in range(len(choices)):
            if should_confirm:
                response = are_you_sure(message)
            return choices[response]
        display.reset()
        response = input(message)
