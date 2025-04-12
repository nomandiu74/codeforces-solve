t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Length of the string
    s = input()  # Input string
    x = list(set(s))  # Unique characters in the string

    # Replace characters alternately with '0' and '1'
    for i in range(len(x)):
        if i % 2 == 0:
            s = s.replace(x[i], '0')  # Replace character with '0'
        else:
            s = s.replace(x[i], '1')  # Replace character with '1'

    # Check if the resulting string is alternating
    alternating = True
    for j in range(1, len(s)):
        if s[j] == s[j - 1]:  # If two consecutive characters are equal
            alternating = False
            break

    if alternating:
        print("YES")
    else:
        print("NO")