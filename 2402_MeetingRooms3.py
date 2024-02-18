n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

n = 2
meetings = [[43,44],[34,36],[11,47],[1,8],[30,33],[45,48],[23,41],[29,30]]
# [[1, 8], [11, 47], [23, 41], [29, 30], [30, 33], [34, 36], [43, 44], [45, 48]] 
def mostBooked(n: int, meetings: list[list[int]]) -> int:
    meetings = sorted(meetings, key=lambda x: x[0])
    temps = 0
    meeting_actuel = 0
    room_utilisation = {}
    room_temps = {}
    for i in range(n):
        room_utilisation[i] = 0
        room_temps[i] = 0

    while meeting_actuel < len(meetings):
        nouvelle_room = True
        while nouvelle_room and meeting_actuel < len(meetings) and meetings[meeting_actuel][0] <= temps:
            for i in range(n):
                if room_temps[i] <= temps:
                    room_temps[i] = temps + (meetings[meeting_actuel][1]-meetings[meeting_actuel][0])
                    room_utilisation[i] += 1
                    meeting_actuel += 1
                    break
            else:
                nouvelle_room = False
        print(f"Temps actuel : {temps}")
        print(f"Temps : {room_temps}")
        print(f"Utilisation : {room_utilisation}\n")
        temps += 1
    return max(room_utilisation, key=room_utilisation.get)


print(mostBooked(n,meetings))
