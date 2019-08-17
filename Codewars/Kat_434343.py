def tribonacci(signature, n):
    return [signature[x] + signature[x-1] + signature[x-2] for x in range(2, n+3)]
