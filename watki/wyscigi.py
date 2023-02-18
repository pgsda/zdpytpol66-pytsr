from threading import Thread


def count(rl):
    for _ in range(1_000_000):
        rl[0] += 1


result = [0]

t1 = Thread(target=count, args=(result,))
t2 = Thread(target=count, args=(result,))

t1.start()
t2.start()

t1.join()
t2.join()

print(result[0])
