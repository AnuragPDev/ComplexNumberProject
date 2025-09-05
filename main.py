class ComplexNumer:
    pass

    def __init__(self, real=0.0 , imag=0.0): #default agrugument we can overshadowing it 
        self.real=real
        self.imag=imag
        #to print object in readble manner 
    def __str__(self):
        if self.real==0:
            return f"{self.imag}j"
        if self.imag<0:
            return f"{self.real}{self.imag}j"
        else:
            return f"{self.real}+{self.imag}j"

    # conjugate function for complex number
    def conjugate(self):
        
        imag=-1*self.imag
        if self.real==0:
            print(f"{imag}j")
        elif imag<0:
            print (f"{self.real}{imag}j")
        else:
            print (f"{self.real}+{imag}j")
        
    def __add__(self,other):
        realpart=self.real+other.real
        imagpart= self.imag+other.imag
        return ComplexNumer(realpart, imagpart)
    
    def __sub__(self,other):
        realpart=self.real-other.real
        imagpart= self.imag-other.imag
        return ComplexNumer(realpart, imagpart)
    def __mul__(self,other):
        answerReal=0
        answerImag=0
        answerReal=self.real*other.real - self.imag*other.imag
        answerImag=self.real*other.imag + self.imag*other.real
        
        return ComplexNumer(answerReal, answerImag)
   
    def __truediv__(self,other):
        denominator = other.real**2 + other.imag**2
        ans = self * ComplexNumer(other.real/denominator,(other.imag*-1)/denominator)
        return ans
        
        
        

cn1=ComplexNumer(3,4)
cn2 =ComplexNumer(4,5)

# print(cn1,cn2)
# print(cn1+cn2 , type(cn1+cn2))
print(cn1/cn2)

# print(f"{cn1.real},{cn1.imag}")  # this will print real and imaginary part of the complex number 
# print(f"{cn2.real},{cn2.imag}") 




