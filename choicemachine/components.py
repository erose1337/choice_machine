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
         
def _cmp(a, b):
    return choice(a, b, _not(b))
          
def _or(a, b):
    #if a == 1:
    #    output 1
    #else:
    #   output b
    return choice(a, 1, b)

def half_adder(a, b):
    #   a
    #   b +
    #-----
    #c  s    
    _sum = xor(a, b)
    carry = _and(a, b)
    return _sum, carry
    
def full_adder(a, b, carry_input):
    sum0, carry0 = half_adder(carry_input, a)
    sum1, carry1 = half_adder(sum0, b)
    return sum1, _or(carry0, carry1)
    
def add(a, b, width):
    mask = 1
    carry = 0
    output = 0
    for bit in range(width):
        a_bit = _and(a, mask)
        b_bit = _and(b, mask)
        _sum, carry = full_adder(a_bit, b_bit, carry)        
        print "Output before: ", output, output | _sum, _or(output, _sum)
        output = _or(output, _sum)
        print "After: ", a_bit, b_bit, _sum, carry, output
        mask <<= 1
    return output
    
    
def test_or():
    for a in range(4):
        for b in range(4):
            output1 = a | b
            output2 = _or(a, b)
            assert output1 == output2, (output1, output2)
    print("_or unit test passed")
    
def test_not():
    a = 0
    assert _not(a) == 1
    a = 1
    assert _not(a) == 0
    print("_not unit test passed")
            
def test_and():    
    for a in range(4):
        for b in range(4):
            a_out = _and(a, b)
            assert a_out == a & b, (a_out, a & b)                   
    print "_and unit test passed"
        
def test_xor():
    for a in range(4):
        for b in range(4):
            output = xor(a, b)
            assert output == a ^ b, (a, b, output, a ^ b)
    print("xor unit test passed")                
            
def test_cmp():
    for a in range(4):
        for b in range(4):
            output = _cmp(a, b)
            assert output == (a == b)
    print("_cmp unit test passed")
    
def test_add():
    for a in range(16):
        for b in range(16):
            print "Adding: ", a, b
            output = add(a, b, 4)
            assert output == a + b, (output, a + b)
    print("add unit test passed")
    
if __name__ == "__main__":    
    test_not()
    test_and()
    test_xor()
    test_cmp()
    test_or()
    test_add()
    