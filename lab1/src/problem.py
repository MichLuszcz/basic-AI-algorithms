

class Problem:
    def __init__(self, function: function, gradient: list):
        self.function = function
        self.gradient = gradient

    def value(self, x0: tuple):
        return self.function(x0)


