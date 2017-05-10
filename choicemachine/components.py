from os import urandom

random_bit = lambda: ord(urandom(1)) & 1
    
def choice(a, b, c):
    # in hardware, choice is like a switch or a transistor
    # this software representation utilizes two instructions (AND/XOR) to implement choice       
    return c ^ (a & (b ^ c))
    
def identity(a):
    return choice(a, 1, 0)
    
def _not(a):
    # 0 -> 1
    # 1 -> 0
    # choice(0, 0, 1)
    # choice(1, 0, 1)
    return choice(a, 0, 1)
    
def _and(a, b):
    # 0 ^ (a & (b ^ 0)) == a & b
    return choice(a, b, 0)        
         
def xor(a, b):
    # if a == 1:
    #   output not b
    # else:
    #   output b
    return choice(a, _not(b), b)
                
def test_not():
    a = 0
    assert _not(a) == 1
    a = 1
    assert _not(a) == 0
    print "_not unit test passed"
            
def test_and():    
    for a in range(2):
        for b in range(2):
            a_out = _and(a, b)
            assert a_out == a & b                      
    print "_and unit test passed"
        
def test_xor():
    for a in range(2):
        for b in range(2):
            output = xor(a, b)
            assert output == a ^ b
    print "xor unit test passed"                  
            
if __name__ == "__main__":
    test_not()
    test_and()
    test_xor()
    