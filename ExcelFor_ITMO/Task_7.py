t = int(input())
skip = input()
for i in range(t):
    d = {}
    k = int(input())
    played = {}
    for j in range(k):
        str = input()
        p_name = str[0:-2]
        n_songs = int(str.split()[-1])
        song_list = []
        main_time = 0
        for z in range(n_songs):
            str_song = input()
            s_name = str_song.split(' by ')[0][1:]
            autor = str_song.split(' by ')[1].split(' for ')[0]
            time_str = str_song.split()[-1]
            time = int(time_str.split(':')[0]) * 60 + int(time_str.split(':')[1])
            song_list.append([s_name, autor, time])
        d[p_name] = [song_list, main_time]
    q = int(input())
    print(d)
    for j in range(q):
        str = input()
        act = str.split()[0]
        p_name = str[6:-6]
        time_str = str.split()[-1]
        time = int(time_str.split(':')[0]) * 60 + int(time_str.split(':')[1])
        if act == "Start":
            time_pl = 0
            z = 0
            while time > time_pl:
                time_pl += d[p_name][0][z][2]
                if (d[p_name][0][z][0] + " by " + d[p_name][0][z][1]) in d:
                    played[(d[p_name][0][z][0] + " by " + d[p_name][0][z][1])] += 1
                else:
                    played[(d[p_name][0][z][0] + " by " + d[p_name][0][z][1])] = 1
                z += 1
            d[p_name][1] += time
        if act == "Continue":
            time_pl = 0
            z = 0
            while d[p_name][1] >= time_pl:
                time_pl += d[p_name][0][z][2]
                z += 1
            while time + d[p_name][1] >= time_pl:
                time_pl += d[p_name][0][z][2]
                if (d[p_name][0][z][0] + " by " + d[p_name][0][z][1]) in d:
                    played[(d[p_name][0][z][0] + " by " + d[p_name][0][z][1])] += 1
                else:
                    played[((d[p_name][0][z][0] + " by " + d[p_name][0][z][1]))] = 1
                z += 1
            d[p_name][1] += time
    skip = input()
    print(d)