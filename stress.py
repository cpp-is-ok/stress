import os
import json

try:
    with open("./_stress/stress.json") as f:
        param: dict = json.load(f)
except FileNotFoundError:
    print("Configuration file _stress/stress.json hasn't been found")
    quit(1)

SOLUTION = param.get("SOLUTION")
CORRECT = param.get("CORRECT")
GENERATOR = param.get("GENERATOR")
CHECKER = param.get("CHECKER")
TESTS_AMOUNT = param.get("TESTS_AMOUNT", 1000)
NO_STOP = param.get("NO_STOP", False)

if None in (SOLUTION, CORRECT, GENERATOR):
    print("Not enough files specified")
    quit(1)

for i in range(TESTS_AMOUNT):
    os.system(GENERATOR)
    os.system(f"{SOLUTION} < in > out")
    os.system(f"{CORRECT} < in > out1")
    flg = False
    f = open("out")
    ans = f.read()
    f.close()
    f1 = open("out1")
    cor = f1.read()
    f1.close()
    ans1 = ans.replace('\n', ' ').strip()
    cor1 = cor.replace('\n', ' ').strip()
    ans = ans.replace(' ', '').replace('\n', '')
    cor = cor.replace(' ', '').replace('\n', '')
    if CHECKER is None:
        flg = (ans == cor)
    else:
        os.system(f"{GENERATOR} out out1")
        f = open("out")
        res = f.read().replace(' ', '').replace('\n', '')
        if res not in ('YES', 'NO'):
            print(f"Generator answered {res}, expected YES/NO")
            quit(1)
        flg = (res == 'YES')
    if flg:
        print(f"[ ] TEST #{i} OK")
    else:
        f = open("in")
        test = f.read().replace('\n', '\n    ')
        f.close()
        print(f"[!] TEST #{i} WA: {ans1 = }, {cor1 = }\n[!] Test:\n[!] {test}")
        if not NO_STOP:
            quit()
