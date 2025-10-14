def digital_root(n):
    return n if n < 10 else n % 9 or 9

def is_lucky_ticket(ticket_number):
    digits = [int(d) for d in ticket_number]
    n = len(digits)    
    prefix_sums = [0] * n
    prefix_sums[0] = digits[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + digits[i]  
    total_sum = prefix_sums[-1]
    for i in range(n-1):
        left_sum = prefix_sums[i]
        right_sum = total_sum - left_sum     
        if digital_root(left_sum) == digital_root(right_sum):
            return True  
    return False

print("YES" if is_lucky_ticket(input()) else "NO")
