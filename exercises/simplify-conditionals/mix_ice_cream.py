# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def drinks(drink):
    return ('coffee' in drink or 'strawberry milkshake' in drink)

def make_drink(drink, addons):
    mix = []
    if drinks(drink):
        mix = add(mix, 'coffee')
    if drinks(drink):
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')
    mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
