def test(n: int) -> bool:
    return n>=100 and n <1000

def sum_digits(n: int) -> int:
    a = n/100
    b = (b / 10) % 10
    c = n % 10
    return a + b + c