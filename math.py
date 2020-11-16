# Python 3.2+
# імпортуємо потрібні утиліти та бібліотеку для математичних обчислень
import os
import concurrent.futures
import numpy as np

# задаємо функцію для паузи терміналу
def pause():
    programPause = input("\nExit the script with ENTER")

# задаємо функції с обчилсеннями
def f1():
    mo=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    me=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])
        
    a = np.array([
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1]])

    b = np.array([
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1]])

    firstMove = mo.dot(me)
    secondMove = firstMove.dot(b)
    thirdMove = np.add(a, secondMove)

    return thirdMove

def f2():
    mk=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    ml=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    mg=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    firstMove = mk.dot(ml)
    secondMove = firstMove.dot(mg)
    thirdMove = np.subtract(secondMove, mk)

    return thirdMove

def f3():
    mp=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    mr=np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

    t = np.array([
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1]])

    firstMove = mp.dot(mr)
    secondMove = np.transpose(firstMove)
    thirdMove = secondMove.dot(t)

    return thirdMove

# використовуємо executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # запускаємо три треди
    resultF1 = executor.submit(f1)
    resultF2 = executor.submit(f2)
    resultF3 = executor.submit(f3)

    # очікуємо заверешння тредів
    executor.shutdown(wait=True)

    # прінтуємо результати у термінал
    print("F1 (C):")
    for i in resultF1.result():
        print(i)

    
    print("F2 (MF):")
    for i in resultF2.result():
        print(i)

    
    print("F3 (O):")
    for i in resultF3.result():
        print(i)

# ставимо термінал на паузу
pause()
