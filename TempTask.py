class NonPositiveException(Exception):
    def __init__(self, text):
        self.text = text


class PositiveList(list):
    def append(self, value):
        if value < 0:
            raise NonPositiveException("this is not positive")
        else:
            super().append(value)

temp=PositiveList()
a=-5
try:
    temp.append(a)
    print(temp)
except Exception as e:
    print(e)