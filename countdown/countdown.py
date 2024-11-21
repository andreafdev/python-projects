import time

t = input('Digite o tempo(em segundos): ')

if t.isdigit():
    t = int(t)
else:
    print('Entrada inválida!')
    quit()


while t:  # 0 --> false | 1, 2 --> True
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")  # r = rewrite(sobrescrever)
    time.sleep(1)
    t = t - 1


print('ACABOU O TEMPO!')
