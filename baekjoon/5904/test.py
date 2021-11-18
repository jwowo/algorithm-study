import sys 
# def generate_minimum_moo_sequence(n, result, k=0):
#     if n <= len(result):
#         return result

#     curr_result = result + 'moo' + 'o' * k + result
#     return generate_minimum_moo_sequence(n, curr_result, k+1)

def minimum_moo_sequence(n, result, k=0):
    if n <= result:
        return k-1, result
    curr_result = 2 * result + k + 3 
    k, min_len = minimum_moo_sequence(n, curr_result, k+1)
    return k, min_len

def find_location(n):
    k, min_len = minimum_moo_sequence(n, 0)
    prev_len = (min_len - k - 3)//2

    if prev_len + 1 == n:
                return 'm'
    elif prev_len + 1 < n <= min_len - prev_len:
        return 'o'
    else:
        return find_location(n - min_len + prev_len)    


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(find_location(n))