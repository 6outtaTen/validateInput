def validate_int(prompt_text = "Please enter an integer: ", err_text = "Please make sure that you entered an INTEGER"):
    """
    Prompts, returns and validates that the input is an integer, if not, it warns 
    Takes in 2 arguments: prompt_text and error_text - the text that user wants to be the prompt
    and the text that displays when the input is not valid. The defaults are: 
    prompt_text = "Please enter an integer: " error_text = "Please make sure that you entered an INTEGER"
    """

    while True:
        try:
            user_input = int(input(f"{prompt_text}"))
        except ValueError:
            print(f"{err_text}")
        else:
            return user_input
        

def validate_str(prompt_text = "Please enter a string: ", err_text = "Please make sure that you entered a STRING", stricly_restrict = True):
    """
    Prompts, returns and validates that the input is a string, if not, it warns 
    Takes in 2 arguments: prompt_text and error_text - the text that user wants to be the prompt
    and the text that displays when the input is not valid. The defaults are: 
    prompt_text = "Please enter a string: " error_text = "Please make sure that you entered a STRING"
    """

    if stricly_restrict:
        while True:
            user_input = input(f"{prompt_text}")

            if any(x.isdigit() for x in user_input):
                print(f"{err_text}")
                continue
            else:
                return user_input
    else:
        user_input = input(f"{prompt_text}")

        try:
            int(user_input)
        except ValueError: # As in, if you don't want the whole string to be a number.
            return user_input
        else:
            print("f{err_text}")