import random
from GeneticAlgorithm import Room
from GeneticAlgorithm import Course
from GeneticAlgorithm import Lecturer
from GeneticAlgorithm import Student_group
import copy

def get_key(item):
    return item[0]

def crossover(mating_pool):

    result_lst = []  # list of result
    for mate in mating_pool:  # 1
        rnum = random.randrange(21)
        mate_result = []  # list of sumed mate
        for ielement in range(len(mate[0])):  # 3
            element_lst = []  # list of sumed element
            for ilst in range(len(mate[0][ielement])):  # 4
                result = sumup(mate[0][ielement][ilst], mate[1][ielement][ilst], rnum,ielement)  # sumed element
                element_lst.append(result)
            mate_result.append(element_lst)
        result_lst.append(mate_result)
    return result_lst

def sumup(lstA, lstB, rnum,t):
    result=[]
    if(t == 1):
        result=lstA.course_timeslot[:rnum]
        result.extend(lstB.course_timeslot[rnum:21])
    elif(t==0):
        result = lstA.room_timeslot[:rnum]
        result.extend(lstB.room_timeslot[rnum:21])
    elif(t==2):
        result = lstA.student_group_timeslot[:rnum]
        result.extend(lstB.student_group_timeslot[rnum:21])
    return result

def create_mating_pool(evaluate_dict):
    mating_pool = []
    sample = []
    sorted_evaluate_dict = sorted(evaluate_dict, key = get_key)
    '''
    for i in range(len(sorted_evaluate_dict)):
        if(sorted_evaluate_dict[i][0] < 1000000):
            sample.append(sorted_evaluate_dict[i])
    '''
    for i in sorted_evaluate_dict:
        sample.append(i)

    print('sample: ', len(sample))
    for j in range(len(sample)):
        for l in range(len(sample) - j):
            mating_pool.append(sample[j])

    return mating_pool

def create_evaluate_list(schedule):
    penalties = []
    for rnd in range(len(schedule)):
        room_list = schedule[rnd][0]
        lect_list = schedule[rnd][1]
        stud_list = schedule[rnd][2]
        penalty = 0
        for room_sched in room_list:
            for slot in range(len(room_sched.room_timeslot)):
                if len(room_sched.room_timeslot[slot]) > 1:
                    penalty += 1000000
                elif len(room_sched.room_timeslot[slot]) == 1:
                    if slot > 14:
                        penalty += 50  # weekend
                    if slot % 3 == 2:
                        penalty += 25  # evening

        for lect_sched in lect_list:
            for slot in range(len(lect_sched.course_timeslot)):
                if len(lect_sched.course_timeslot[slot]) > 1:
                    penalty += 1000000
                elif len(lect_sched.course_timeslot[slot]) == 1:
                    penalty += 75 * lect_sched.preference_timeslot[slot]

        for stud_sched in stud_list:
            for slot in range(len(stud_sched.student_group_timeslot)):
                if len(stud_sched.student_group_timeslot[slot]) > 1:
                    penalty += 1000000

        penalties.append(penalty)
    return penalties

def evaluate2(schedule,courses):
    penalties = []
    for rnd in range(len(schedule)):
        count = 0
        room_list = schedule[rnd][0]
        penalty = 0
        for room_sched in room_list:
            for slot in range(len(room_sched)):
                if(len(room_sched[slot])) == 1:
                    chk_list = copy.deepcopy(room_sched)
                    chker = chk_list.pop(slot)
                    if(chker in chk_list):
                        penalty +=1000000
                    chk_list=room_list
                    count+=1
                    if slot > 14:
                        penalty += 50
                    if slot % 3 == 2:
                        penalty += 25
            if(count != len(courses)):
                penalty +=1000000
            count = 0
        penalties.append(penalty)
    print(penalties)
    return penalties

def create_random_list(limit_random, room_list, course_list, lecturer_list, student_group_list):
    random_list = []
    for i in range(limit_random):
        a = copy.deepcopy(room_list)
        b = copy.deepcopy(lecturer_list)
        c = copy.deepcopy(student_group_list)
        random_list.append([a, b, c])
        del a, b, c

    for i in range(limit_random):
        for course in course_list:
            a = random.randint(0, len(random_list[i][0]) - 1)  ## random room
            room_a = random_list[i][0][a]
            position = random.randint(0, len(room_a.room_timeslot) - 1) ## random room slot
            room_a.place_course(position, course.course_name)

            for lecturer in random_list[i][1]:      ## find the lecturer and fill slot
                if(course.lecturer == lecturer.lecturer_name):
                    lecturer.place_course(position, course.course_name)

            for student_group in random_list[i][2]:     ## find the student group and fill slot
                if (course.student_group == student_group.student_group):
                    student_group.place_course(position, course.course_name)

    return random_list

def print_all_time_slot(random_list):
    print('result')
    print('roomslot:')
    for j in random_list[0]:
        print(j.room_name)
        j.print_timeslot()

    print()
    print('lecturerslot:')
    for k in random_list[1]:
        print(k.lecturer_name)
        k.print_timeslot()

    print()
    print('Studentgroupslot:')
    for l in random_list[2]:
        print(l.student_group)
        l.print_timeslot()

    print()

def create_evaluate_dict(random_list, evaluate_list):
    evaluate_dict = []
    for i in range(len(random_list)):
        evaluate_dict.append([evaluate_list[i],random_list[i]])
    return evaluate_dict

def create_random_mating_pool(limit_random, mating_pool):
    random_mating_pool = []
    for i in range (limit_random):
        a = random.randint(0, len(mating_pool)) - 1
        b = random.randint(0, len(mating_pool)) - 1

        random_mating_pool.append([mating_pool[a][1], mating_pool[b][1]])
    return random_mating_pool

def genetic_function(limit_random, number_of_generation, room_list, course_list, lecturer_list, student_group_list):
    random_list = create_random_list(limit_random, room_list, course_list, lecturer_list, student_group_list)
    evaluate_list = create_evaluate_list(random_list)
    evaluate_dict = create_evaluate_dict(random_list, evaluate_list) # list of [[evaluate cost, [[room obj], [lecturer obj], [std obj]]]]
    '''
    mating_pool = create_mating_pool(evaluate_dict)
    random_mating_pool = create_random_mating_pool(limit_random, mating_pool)
    next_generation = crossover(random_mating_pool)
    '''
    '''
    for i in range(number_of_generation - 2):
        evaluate_list = evaluate2(next_generation, course_list)
        evaluate_dict = create_evaluate_dict(next_generation, evaluate_list)
        #mating_pool = create_mating_pool(evaluate_dict)
        
        while(len(mating_pool) == 0):
            next_generation = crossover(random_mating_pool)
            evaluate_list = evaluate2(next_generation, course_list)
            evaluate_dict = create_evaluate_dict(next_generation, evaluate_list)
            mating_pool = create_mating_pool(evaluate_dict)
        
        random_mating_pool = create_random_mating_pool(limit_random, mating_pool)
        next_generation = crossover(random_mating_pool)

    evaluate_list = evaluate2(next_generation, course_list)
    evaluate_dict = create_evaluate_dict(random_list, evaluate_list)
    
    return evaluate_dict[0]
    '''

def genetic_function2(limit_random, room_list, course_list, lecturer_list, student_group_list):
    evaluate2(limit_random, course_list)

def main():
    y1= Student_group.StudentGroup('y1')
    y2= Student_group.StudentGroup('y2')
    y3= Student_group.StudentGroup('y3')
    y4= Student_group.StudentGroup('y4')
    print(type(y1))
    ic01 = Room.Room('ic01')
    ic02 = Room.Room('ic02')
    ic03 = Room.Room('ic03')
    ic04 = Room.Room('ic04')

    basicElectricityandElectronics = Course.Course('basicElectricityandElectronics', 'montri_phothisonothai', 'y1')
    cProgramming = Course.Course('cProgramming', 'ukrit_watchareeruetai', 'y1')
    cprogrammingLaboratory = Course.Course('cprogrammingLaboratory', 'ukrit_watchareeruetai', 'y1')
    calculus1 = Course.Course('calculus1', 'ronnachai_tiyarattanachai', 'y1')
    introductiontoComputersandProgrammings = Course.Course('introductiontoComputersandProgrammings', 'veera_boonjing', 'y1')
    introductiontoLogic = Course.Course('introductiontoLogic', 'pratoom_angurarohita', 'y1')

    advanceObjectOrientedProgramming = Course.Course('advanceObjectOrientedProgramming', 'veera_boonjing', 'y2')
    computerOrganizationandAssemblyLanguage = Course.Course('computerOrganizationandAssemblyLanguage', 'surin_kittitornkun', 'y2')
    computerOrganizationandAssemblyLanguageLaboratory = Course.Course('computerOrganizationandAssemblyLanguageLaboratory', 'surin_kittitornkun', 'y2')
    dataStructuresandAlgorithm = Course.Course('dataStructuresandAlgorithm', 'kulwadee_somboonviwat', 'y2')
    dataStructuresandAlgorithmLaboratory = Course.Course('dataStructuresandAlgorithmLaboratory', 'kulwadee_somboonviwat', 'y2')
    linearAlgebra = Course.Course('linearAlgebra', 'prakash_chanchana', 'y2')

    artificialIntelligent = Course.Course('artificialIntelligent', 'visit_hirankitti', 'y3')
    databaseSystems = Course.Course('databaseSystems', 'kulwadee_somboonviwat', 'y3')
    objectOrientedAnalysisandDesign = Course.Course('objectOrientedAnalysisandDesign', 'isara_anantavrasilp', 'y3')
    objectOrientedAnalysisandDesignLaboratory = Course.Course('objectOrientedAnalysisandDesignLaboratory', 'isara_anantavrasilp', 'y3')
    operatingSystems = Course.Course('operatingSystems', 'boontee_kruatrachue', 'y3')
    theoryofComputation = Course.Course('theoryofComputation', 'natthapong_jungteerapanich', 'y3')
    webProgramming = Course.Course('webProgramming', 'todsanai_chumwatana', 'y3')

    humanComputerInteraction = Course.Course('humanComputerInteraction', 'montri_phothisonothai', 'y4')
    softwareVerificationandValidation = Course.Course('softwareVerificationandValidation', 'natthapong_jungteerapanich', 'y4')

    montri_phothisonothai = Lecturer.Lecturer('montri_phothisonothai', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    ukrit_watchareeruetai = Lecturer.Lecturer('ukrit_watchareeruetai', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    ronnachai_tiyarattanachai = Lecturer.Lecturer('ronnachai_tiyarattanachai', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    veera_boonjing = Lecturer.Lecturer('veera_boonjing', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    pratoom_angurarohita = Lecturer.Lecturer('pratoom_angurarohita', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    surin_kittitornkun = Lecturer.Lecturer('surin_kittitornkun', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    kulwadee_somboonviwat = Lecturer.Lecturer('kulwadee_somboonviwat', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    prakash_chanchana = Lecturer.Lecturer('prakash_chanchana', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    visit_hirankitti = Lecturer.Lecturer('visit_hirankitti', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    isara_anantavrasilp = Lecturer.Lecturer('isara_anantavrasilp', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    boontee_kruatrachue = Lecturer.Lecturer('boontee_kruatrachue', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    natthapong_jungteerapanich = Lecturer.Lecturer('natthapong_jungteerapanich',[0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])
    todsanai_chumwatana = Lecturer.Lecturer('todsanai_chumwatana', [0,0,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1, 5,5,5, 5,5,5])

    room_list = [ic01, ic02, ic03, ic04]
    course_list = [basicElectricityandElectronics, cProgramming, cprogrammingLaboratory,
                   calculus1, introductiontoComputersandProgrammings, introductiontoLogic,
                   advanceObjectOrientedProgramming, computerOrganizationandAssemblyLanguage, computerOrganizationandAssemblyLanguageLaboratory,
                   dataStructuresandAlgorithm, dataStructuresandAlgorithmLaboratory, linearAlgebra,
                   artificialIntelligent, databaseSystems, objectOrientedAnalysisandDesign,
                   objectOrientedAnalysisandDesignLaboratory, operatingSystems, theoryofComputation,
                   webProgramming, humanComputerInteraction, softwareVerificationandValidation]

    lecturer_list = [montri_phothisonothai, ukrit_watchareeruetai, ronnachai_tiyarattanachai,
                     veera_boonjing, pratoom_angurarohita, surin_kittitornkun,
                     kulwadee_somboonviwat, prakash_chanchana, visit_hirankitti,
                     isara_anantavrasilp, boontee_kruatrachue, natthapong_jungteerapanich,
                     todsanai_chumwatana]

    student_group_list = [y1, y2, y3, y4]
    limit_random = eval(input('limit random: '))
    number_of_generation = eval(input('number of generation: '))
    best_output = genetic_function(limit_random, number_of_generation, room_list, course_list, lecturer_list, student_group_list)
    print(best_output[0])
main()
