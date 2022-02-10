# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

harmful_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

def toxin_alert():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()

def not_toxin():
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()


ingredients = ['ash']
if ingredients in harmful_ingredients:
    toxin_alert()
else:
    not_toxin()


