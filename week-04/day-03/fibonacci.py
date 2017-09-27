class Fibonacci(object):
    def fibonacci(self, num):
        if num <= 1:
            return num
        else:
            return self.fibonacci(num -1) + self.fibonacci(num -2)
            