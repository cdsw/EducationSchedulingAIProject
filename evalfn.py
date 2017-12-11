def evaluator_function(schedule):
    tse = list(map(list, zip(*schedule)))
    penalty = 0
    for slot in range(len(tse)):
        time = tse[slot]
        for i in range (len(time)):
            if len(time[i]) == 0:
                continue
            if len(time[i]) > 1:
                penalty += 15
                continue
            for j in range (len(tse[slot])):
                if len(time[j]) != 1:
                    continue
                if i == j:
                    continue
                else:
                    if time[i][0].studentGroup == time[j][0].studentGroup:
                        penalty += 5
                    if time[i][0].lecturer == time[j][0].lecturer:
                        penalty += 5
            penalty += time[i].lecturer.time_preference[slot] * 2
            if slot % 3 == 2:
                penalty += 2
            if slot > 15:
                penalty += 3
    return penalty
