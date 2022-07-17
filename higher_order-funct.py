def big(text):
    return text.upper()


def small(text):
    return text.lower()


def hello(func):
    text = func(" Python")  # here we are assigning function to variable
    print(text)


hello(big)
hello(small)