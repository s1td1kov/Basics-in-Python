def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(height, fp, tp):
    print(height, fp, tp)


n = int(input())
moveTower(n, 1, 3, 2)
