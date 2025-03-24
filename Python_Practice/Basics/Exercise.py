class Number:
    def __init__(self,number):
        """initialize the number

        Args:
            number (init): number
        """
        self._number = number

    def is_even(self):
        """number is prime or not
        """
        if self._number % 2 == 0:
            print('even')
        else: print('not even')

    def is_prime(self):
        """the given number is prime or not
        """
        for index in range(2, self._number):
            if self._number % index == 0:
                print('is a not prime')
                return True
            print("is prime")
            return False

    def is_pallindrome(self):
        """the given number is pallindrome or not
        """    
        return n1 == self._number[::-1]
    
    if is_pallindrome(n1):        

      print("pallendrome")
    else:
      print("not a pallendrome")



n1 = Number(131)   
#n1.is_even()
#n1.is_prime()
n1.is_pallindrome()