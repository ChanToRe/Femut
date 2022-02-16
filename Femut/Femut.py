def pearson(Length, Sex='Male' or 'Female'):
    if Sex == 'Male' and Length > 0:
        result = 81.306 + 1.880 * Length
    elif Sex == 'Female' and Length > 0:
        result = 72.844 + 1.945 * Length
    else :
        pass
    return result

def tng(Length):
    if Length > 0:
        result = 2.15 * Length + 72.57
    else :
        pass
    return result

def huzii(Length, Sex='Male' or 'Female'):
    if Sex == 'Male' and Length > 0:
        result = (2.47 * (Length*10) + 549.01)/10
    elif Sex == 'Female' and Length > 0:
        result = (2.24 * (Length*10) + 610.43)/10
    else :
        pass
    return result