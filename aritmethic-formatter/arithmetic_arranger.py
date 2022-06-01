def arithmetic_arranger(problems, display=False):
    import re
    def print_format(res, display):
        l1 = l2 = l3 = hasil = ''
        for i in res:
            x = i[:]
            i = i.split()
            pad = len(max(i, key=len))
            l1 += i[0].rjust(pad+2, ' ') + '    '
            l2 += i[1]+ i[2].rjust(pad+1, ' ') + '    '
            l3 += ('-'*(pad+2)) + '    '
            hasil += str(eval(x)).rjust(pad+2, ' ') + '    '
        if display:
          return l1[:-4] + '\n' + l2[:-4] + '\n' + l3[:-4] + '\n' + hasil[:-4]
        return l1[:-4] + '\n' + l2[:-4] + '\n' + l3[:-4]
    
    cek4digit = lambda token: re.fullmatch(r'^\d{1,4}\s*[+-]\s*\d{1,4}$', token)
    validasi_op = lambda token: (not bool(re.search(r'[/x]', token)) and bool(re.search(r'[+-]', token)))
    is_digit_only = lambda token: bool(re.fullmatch(r'\d+\s*[+-]\s*\d+$', token))
    if len(problems) > 5:
        return "Error: Too many problems."
    res = []
    for token in problems:
        if not validasi_op(token):
            return "Error: Operator must be '+' or '-'."
        if not is_digit_only(token):
            return "Error: Numbers must only contain digits."
        if not bool(cek4digit(token)):
            return "Error: Numbers cannot be more than four digits."
        # formats = token.split()
        res.append(token)
    return print_format(res, display)
    
