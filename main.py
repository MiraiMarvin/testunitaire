# calcul.py

def addition(a, b):
    return a + b

def seconde_to_minute(seconde):
    result = seconde / 60
    result = int(result)  
    return str("ça fait " + str(result) + " minute(s)")

def list_converter(list_of_strings):
    return [ seconde_to_minute(s) for s in list_of_strings ]