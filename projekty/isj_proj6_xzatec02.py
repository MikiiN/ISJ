#!/usr/bin/env python3

class Polynomial():
    def __init__(self, *args, **kwargs):
        self.pol = []
        if args:
            # argument is list
            if isinstance(args[0], list):
                self.pol = args[0]
            # normal arguments
            else:
                for x_val in args:
                    self.pol.append(x_val)
        # keyword arguments
        elif kwargs:
            max_idx = -1
            # find max index
            for x_key, value in kwargs.items():
                if not value == 0:
                    max_idx = max(max_idx, int(x_key.replace("x", "")))
            # create list
            for i in range(max_idx+1):
                key = "x" + str(i)
                if key in kwargs:
                    self.pol.append(int(kwargs[key]))
                else:
                    self.pol.append(0)
            if self.pol == []:
                self.pol.append(0)
    
    
    def __str__(self):
        result = ""
        first_flag = True
        # iterate over reversed polynomial
        for i, val in reversed(list(enumerate(self.pol))):
            if not val == 0:
                if first_flag: # first non zero element
                    if val < 0:
                        result = "- "
                    first_flag = False
                else:
                    if val < 0:
                        result = result + " - "
                    else:
                        result = result + " + "
                if i == 0: # x^0 handling 
                    result = result + str(abs(val))
                elif i == 1: # x^1 handling
                    if abs(val) == 1:
                        result = result + "x"
                    else:
                        result = result + str(abs(val)) + "x"
                else:
                    if abs(val) == 1:
                        result = result + "x^" + str(i)
                    else:
                        result = result + str(abs(val)) + "x^" + str(i)
        if first_flag: # only zeros in polynomial
            result = "0"
        return result
    
    
    def __eq__(self, other):
        return self.pol == other.pol
            
    
    def __add__(self, other):
        if len(self.pol) > len(other.pol):
            result = self.pol.copy()
            second = other.pol
        else:
            result = other.pol.copy()
            second = self.pol
        # iterate over smaller list
        for i, val in enumerate(second):
            result[i] = result[i] + val
        return Polynomial(result)
    

    def __pow__(self, other):
        if other < 0:
            return self
        if other == 0: # ^0 handling
            return Polynomial(1)
        if other == 1: # ^1 handling
            return Polynomial(self.pol)
        result = self.pol.copy()
        for _ in range(1, other):
            tmp = []
            # polynomial multiply
            for i, a_val in enumerate(self.pol):
                for j, b_val in enumerate(result):
                    numb = a_val * b_val
                    idx = i+j
                    # checking if polynomial index is not out of range
                    if idx >= len(tmp):
                        for _ in range(len(tmp), idx):
                            tmp.append(0)
                        tmp.append(numb)
                    else:
                        tmp[idx] = tmp[idx] + numb
            result = tmp.copy()
        return Polynomial(result)
    
    
    def derivative(self):
        new = []
        for i in range(1, len(self.pol)):
            new.append(self.pol[i]*i)
        if not new:
            new.append(0)
        return Polynomial(new)
    
    
    def at_value(self, *values):
        result = [0, 0]
        for i in range(len(values)):
            for j, val in enumerate(self.pol):
                result[i] += val * (values[i]**j)
        if len(values) == 2:
            return result[1]-result[0]
        return result[0]


def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
