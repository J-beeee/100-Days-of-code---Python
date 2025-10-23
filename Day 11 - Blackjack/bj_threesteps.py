import random as r
c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def p():
    if input("Play? 'y': ") == 'y':
        u, comp = [r.choice(c) for _ in range(2)], [r.choice(c)]
        while sum(u) < 21 and input(f"Your: {u} ({sum(u)}). Another? 'y': ") == 'y':
            u.append(r.choice(c))
            if sum(u) > 21 and 11 in u: u[u.index(11)] = 1
        while sum(comp) < 17: comp.append(r.choice(c))
        us, cs = sum(u), sum(comp)
        print(f"Your: {u} ({us}) | Computer: {comp} ({cs})")
        print("You win!" if (us <= 21 and (us > cs or cs > 21)) else "You lose!" if us != cs else "Draw!")
        p()
p()