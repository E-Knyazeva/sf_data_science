from collections import deque
dq = deque() # создать пустой дек
print(dq)

clients = deque()
clients.append('Ivanov') # добавить человека в очередь
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
clients.append('Knyazev')
print(clients)
print(clients[3]) # есть индексация по элементам

del clients[1]
print(clients)

first_client = clients.popleft() #заберём двоих человек из начала очереди 
second_client = clients.popleft()
print('First client:', first_client)
print('Second client:', second_client)
print(clients)

clients.appendleft('Vip-client') #добавить  нужно в начало очереди 
print(clients)

tired_client = clients.pop() # Последний клиент в очереди устал ждать и отменил вызов
print(tired_client, 'left the queue')
print(clients)


shop = deque([1,2,3,4,5]) # очередь из клиентов магазинчика на заправке 
print(shop)
shop.extend([11,12,13,14,15,16,17]) # добавим в неё сразу всех туристов, приехавших на экскурсионном автобусе
print(shop)

shop = deque([1,2,3,4,5]) 
print(shop)
shop.extendleft([11,12,13,14,15,16,17]) # клиенты турфирмы обслуживаются вне очереди, добавим их в начало той же очереди
print(shop)



limited = deque(maxlen=3) # задание максимальной длины очереди
print(limited)

limited_from_list = deque([1,3,4,5,6,7],maxlen=3) # в очереди с ограниченной длиной сохраняются только последние элементы, а первые исчезают из памяти
print(limited_from_list)

limited.extend([1,2,3]) 
print(limited)

print(limited.append(8)) 
print(limited)


temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

days = deque(maxlen=7)

for temp in temps:
    days.append(temp)  # Добавляем температуру в очередь
    if len(days) == days.maxlen: # Если длина очереди оказалась равной максимальной длине очереди (7), печатаем среднюю температуру за последние 7 дней
        print(round(sum(days)/len(days), 2), end='; ')
print('')


dq = deque([1,2,3,4,5])
print(dq)
dq.reverse()
print(dq)

dq = deque([1,2,3,4,5])
print(dq)
dq.rotate(3)
print(dq)

dq = deque([1,2,3,4,5])
print(dq)
dq.rotate(-1)
print(dq)

dq = deque([1,2,4,3,2,1,5,9,7,4,4,2,3])
print(dq.index(5))
print(dq.count(4))
dq.clear()
print(dq)


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
temps_check = dict()
for temps_check, temp in temps:
    if temp not in temps:
        temps[temp] = list()
    temps[temp].append(temps_check)
print(temps_check)