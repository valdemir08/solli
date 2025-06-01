def validate_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove tudo que não for número

    if len(cnpj) != 14:
        return False

    # Cálculo dos dígitos verificadores do CNPJ
    def calc_digit(digs, multipliers):
        s = sum(int(d)*m for d, m in zip(digs, multipliers))
        r = s % 11
        return '0' if r < 2 else str(11 - r)

    original_digits = cnpj[-2:]
    base = cnpj[:-2]

    first_digit = calc_digit(base, [5,4,3,2,9,8,7,6,5,4,3,2])
    second_digit = calc_digit(base + first_digit, [6,5,4,3,2,9,8,7,6,5,4,3,2])

    return original_digits == first_digit + second_digit
