num_cities = int(input())

data = dict()

for cur_city_num in range(num_cities):
    city, num_rooms = input().split()
    cur_city_data = {i: [] for i in range(24)}
    for cur_room_num in range(int(num_rooms)):
        timeline, name = input().split()
        for hour in range(24):
            if timeline[hour] == '.':
                cur_city_data[hour].append(name)
    data[city] = cur_city_data

num_requests = int(input())
for i in range(num_requests):
    request = input().split()
    potential_hours = set(i for i in range(24))
    for city in request[1:]:
        free_hours = set()
        for hour, rooms in data[city].items():
            if len(rooms) > 0:
                free_hours.add(hour)
        potential_hours &= free_hours
    if len(potential_hours) == 0:
        print('No', end='')
    else:
        print("Yes", end=' ')
        hour = ''
        for jija in potential_hours:
            hour = jija
            break
        for city in request[1:]:
            print(data[city][hour][0], end=' ')
    print()
