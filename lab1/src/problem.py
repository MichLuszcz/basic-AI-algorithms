class Problem:
    def __init__(self, function, gradient):
        self.function = function
        self.gradient = gradient

    def function_value(self, x0: list):
        return self.function(x0)

    def gradient_value(self, x0: list) -> list:
        return self.gradient(x0)
