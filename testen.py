def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner

@smart_div
def div(a, b):
    print(a / b)


div(2,4)



# funktion darf nicht verändert werden
def div(a, b):
    print(a, b)

#def smart_div
    # soll vor ausgabe noch "hallo" printen und dann erst das a durch b
    




# def div(a, b):
#     print(a / b)


# def smart_div(func):

#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)

#     return inner


# div = smart_div(div)

# div(2,4)







# def div(a, b):
#     print(a / b)


# def smart_div(a, b):
#     if a < b:
#         a, b = b, a
#     return div(a,b)


# smart_div(2,4)
