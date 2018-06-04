def bits(number, size):
    return format(number, 'b').zfill(size)
    
def strange_multiplier(a, b, bit_size=8):    
#                        10011010    
#                        01010101
#                       ---------- and
#                        10011010
#                       00000000|
#                      10011010||
#                     00000000|||
#                    10011010||||
#                   00000000|||||
#                  10011010||||||
#                 00000000|||||||
#                 ----------------- xor
#                 010110111010010
    output = 0
    for shift_amount, bitb in enumerate(reversed(bits(b, bit_size))):
        if bitb == '1':            
            output ^= a << shift_amount        
    return output

    

        
    
def test_strange_multiplier():
  #  b = 85
  #  a = 154
    a = 85
    b = 154
    out = strange_multiplier(a, b)
    assert out == 11730, out
    
    #for a in range(256):
    #    for b in range(256):
    #        assert strange_multiplier(a, b) == strange_multiplier(b, a)
    
    a = 85
    b = 100    
    c = 50 
    ab = strange_multiplier(a, b)
    bc = strange_multiplier(b, c)
    abc = strange_multiplier(a, b & c)
    print a, b, c, ab, bc, ab & bc, abc
    
    
if __name__ == "__main__":
    test_strange_multiplier()
    
