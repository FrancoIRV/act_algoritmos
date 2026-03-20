def breach_attempts(hackers, security_level, increase):
    securityFails = 0
    for i in hackers:
        if i > security_level:
            securityFails = securityFails +1
        else:
            security_level = security_level + increase
    return securityFails

print(breach_attempts([1,2,3], 1, 0))