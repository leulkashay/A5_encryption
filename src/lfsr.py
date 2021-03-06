from BitVector import BitVector

class LFSR(object):
    def __init__(self,length,clock_bits,taps,majority_bits=None,negated_bit=None,bitstring=None,int_value=None):
        
        if bitstring:
            self.register=BitVector(bitstring=bitstring)
        elif int_value:
            self.register=BitVector(size=length,intVal=int_value)
        else:
            self.register=BitVector(size=length)
        
        self.length=length
        self.clock_bits=[]
        self.taps=taps
        self.majority_bits=majority_bits
        self.negated_bit=negated_bit

        for clock_bit in clock_bits:
            self.clock_bits.append(length - clock_bit -1)

        

    def clock(self,key_bit=False):
        result=key_bit
        for tap in self.taps:
            result= result ^ self.register[(self.length - tap -1)]
        self.register << 1
        self.register[-1] = result
        
    def get_clock_bit(self):
        clock_bit_value=[]
        for clock_bit in self.clock_bits:
            clock_bit_value.append(self.register[clock_bit])
        return clock_bit_value

    def set_bit(self,index,value):
        self.register[self.length - index - 1]=value

    def get_bit(self,index):
        return self.register[self.length - index - 1]

    def get_majority(self):
        values=[self.register[self.length - self.negated_bit - 1] ^ 1]
        for bit in self.majority_bits:
            values.append(self.register[self.length - bit -1 ])
        a=values[0]
        b=values[1]
        c=values[2]
        return (a*b) ^ (a*c) ^ (b*c)