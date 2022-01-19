import sys

languages_all = None
languages_one = None
languages_next = set()
n, m_i = None, 0
for line in sys.stdin:
    s = line.strip()
    if n is None:
        n = int(s)
    else:
        if s.isdigit():
            m_i = int(s)
        else:
            languages_next.add(s)
            if len(languages_next) == m_i:
                if languages_all is None:
                    languages_all = languages_next.copy()
                    languages_one = languages_next.copy()
                else:
                    languages_all &= languages_next
                    languages_one |= languages_next
                languages_next = set()

print(len(languages_all), *languages_all, sep='\n')
print(len(languages_one), *languages_one, sep='\n')
