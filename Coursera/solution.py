import sys

base = {}
for line in sys.stdin:
    command, family_summa = line.strip().split(' ', 1)
    if command in ['DEPOSIT', 'WITHDRAW', 'TRANSFER']:
        family, summa = family_summa.split(' ', 1)
        base.setdefault(family, 0)
        if command == 'DEPOSIT':
            base[family] += int(summa)
        elif command == 'WITHDRAW':
            base[family] -= int(summa)
        elif command == 'TRANSFER':
            family_2, summa_transfer = summa.split()
            base.setdefault(family_2, 0)
            base[family] -= int(summa_transfer)
            base[family_2] += int(summa_transfer)
    elif command == 'BALANCE':
        print(base.get(family_summa, 'ERROR'))
    elif command == 'INCOME':
        for key, value in base.items():
            if value > 0:
                value += int(value * (int(family_summa) / 100))
