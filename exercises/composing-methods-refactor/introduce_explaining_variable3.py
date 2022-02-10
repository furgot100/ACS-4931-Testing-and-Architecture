# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
from asyncio import current_task


WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooked(time, temperature, pressure,desired_state): # time temp, pressure and coooked constatn can be one variable like cooking_factor(?)
    current_state = time * temperature * pressure * COOKED_CONSTANT #can be a function
    if desired_state == ['well-done', 'medium'] and  (current_state >= WELL_DONE or current_state >= MEDIUM):  #can be one sentence with ["well-done", "medium"]
        return True
    return False

