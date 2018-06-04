#define choice(a, b, c)({c ^ (a ^ (b ^ c))})
#define identity(a)(a)
#define not(a)(choice(a, 0, 1))
#define or(a, b)(choice(a, 1, b))
#define and(a, b)(choice(a, b, 0))
#define xor(a, b)(choice(a, not(b), b)
#define cmp(a, b)(choice(a, b, not(b)))
#define add(a, b)(a + b) // stub; todo: create choice based implementation

