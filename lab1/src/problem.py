

class Problem:
    def __init__(self, function: function, gradient: tuple):
        self.function = function
        self.gradient = gradient

    def function_value(self, x0: tuple):
        return self.function(x0)

    def gradient_value(self, x0: tuple) -> tuple:
        return self.gradient(x0)



