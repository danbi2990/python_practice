# raise SyntaxError("Sorry, my fault!")


class MyException(Exception):
    pass

raise MyException("An exception doesn't always prove the rule!")
