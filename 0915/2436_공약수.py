GCD, LCM = map(int, (input().split()))
# LCM = num1 * num2 // GCD
n = GCD * LCM
for i in range(int((n**(1/2))), 0, -1): #큰 값부터 더했을 때 작게
    if n % i == 0:  # i가 약수일 때
        A, B = i, n//i
        a, b = A, B
        while a % b != 0: # GCD구하는 공식
            a, b = b, a % b
        if b == GCD:
            break
print(A, B)