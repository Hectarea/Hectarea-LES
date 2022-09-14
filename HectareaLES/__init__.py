class LES:

    def __init__(self):
        self.ProcessingBlocks = [self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7,]

        self.DeProcessingBlocks = [self.__0, self.__1, self.__2, self.__3, self.__4, self.__5, self.__6, self.__7,]

    def encrypt(self, xArray, password, iv, nonce):

        nonce = int.from_bytes(nonce,'big')

        tempArray = b''

        for index in range(len(xArray)):
            tempArray += bytes([self.ProcessingBlocks[((index)*(nonce))%2**3](xArray[index], password, iv, (index+(nonce%len(password)))%(len(password)))])

        return tempArray
    
    def decrypt(self, xArray, password, iv, nonce):

        nonce = int.from_bytes(nonce,'big')

        tempArray = b''

        for index in range(len(xArray)):
            tempArray += bytes([self.DeProcessingBlocks[((index)*(nonce))%2**3](xArray[index], password, iv, (index+(nonce%len(password)))%(len(password)))])

        return tempArray


    def _0(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+iv*password**2)%2**16):
            x -= iv*password%256
        return (iv*password+x)%256

    def __0(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+iv*password**2)%2**16):
            x += iv*password%256
        return (x-password*iv)%256

    def _1(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(password%(2**16)):

            x += nonce+iv*password%(2**16)

        return x%256

    def __1(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(password%(2**16)):

            x -= nonce+iv*password%(2**16)
            
        return x%256

    def _2(self, x, password, iv, nonce):

        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))
        password = iv*int.from_bytes(password, 'big')

        for nm in range((nonce+password**2)%2**16):
            x -= iv*password
        return (iv*password+x)%256

    def __2(self, x, password, iv, nonce):

        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))
        password = iv*int.from_bytes(password, 'big')

        for nm in range((nonce+password**2)%2**16):
            x += iv*password
        return (x-password*iv)%256

    def _3(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(password%(2**16)):

            x += nonce+iv*password%(2**16)*nm

        return x%256

    def __3(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(password%(2**16)):

            x -= nonce+iv*password%(2**16)*nm
            
        return x%256

    def _4(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+password**2)%2**16):
            x -= iv*password**3
        return ((iv*password)+x)%256

    def __4(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+password**2)%2**16):
            x += iv*password**3
        return (x-(iv*password))%256

    def _5(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(nonce+iv*password%(2**16)):

            x -= password%(2**16)
            x -= iv*password%(1+(nm*password))

        return x%256

    def __5(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range(nonce+iv*password%(2**16)):

            x += password%(2**16)
            x += iv*password%(1+(nm*password))
            
        return x%256

    def _6(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+password**2)%2**16):
            x -= nonce+iv*password%password%(nm+1)
        return (iv*password+x)%256

    def __6(self, x, password, iv, nonce):

        password = int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))

        for nm in range((nonce+password**2)%2**16):
            x += nonce+iv*password%password%(nm+1)
        return (x-iv*password)%256

    def _7(self, x, password, iv, nonce):

        password = nonce+int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))
        for nm in range(iv%(2**16)):

            x += password%(nm+nonce+1)

        return x%256

    def __7(self, x, password, iv, nonce):

        password = nonce+int.from_bytes(password, 'big')
        iv= (1 + nonce) * (1+int.from_bytes(iv, 'big'))
        for nm in range(iv%(2**16)):

            x -= password%(nm+nonce+1)
            
        return x%256