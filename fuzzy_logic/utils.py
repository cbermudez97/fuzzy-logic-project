def isFloatIn(x, m=None, M=None):
    try:
        float(x)
    except:
        raise ValueError('Data must be a float.')
    if not m is None and not m <= float(x):
        raise ValueError(f'Data must be greater or equal than {m}.')
    if not M is None is None and not M >= float(x):
        raise ValueError(f'Data must be lesser or equal than {M}.')


def inputUntil(msg, cond):
    while True:
        data = input(msg)
        try:
            cond(data)
            return data
        except Exception as e:
            print(str(e))
        continue
