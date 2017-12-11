import random
from GeneticAlgorithm import Room
from GeneticAlgorithm import Course
from GeneticAlgorithm import Lecturer
from GeneticAlgorithm import Student_group


def random_function(limit_random, room_list, course_list, lecturer_list, student_group_list):
    random_list = []
    for i in range(limit_random):
        random_list.append([room_list, lecturer_list, student_group_list])

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

    print('result')
    for i in range(len(random_list)):
        print(i, 'roomslot:')
        for j in random_list[i][0]:
            j.print_timeslot()

        print()
        print(i, 'lecturerslot:')
        for k in random_list[i][1]:
            k.print_timeslot()

        print()
        print(i, 'Studentgroupslot:')
        for l in random_list[i][2]:
            l.print_timeslot()

        print()
    return random_list



def genetic_function(limit_random, number_of_generation, room_list, course_list, lecturer_list, student_group_list):
    for i in range(number_of_generation):
        random_list = random_function(limit_random, room_list, course_list, lecturer_list, student_group_list)



def main():
    y1= Student_group.StudentGroup('y1')
    y2= Student_group.StudentGroup('y2')
    y3= Student_group.StudentGroup('y3')
    y4= Student_group.StudentGroup('y4')

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

    montri_phothisonothai = Lecturer.Lecturer('montri_phothisonothai', [])
    ukrit_watchareeruetai = Lecturer.Lecturer('ukrit_watchareeruetai', [])
    ronnachai_tiyarattanachai = Lecturer.Lecturer('ronnachai_tiyarattanachai', [])
    veera_boonjing = Lecturer.Lecturer('veera_boonjing', [])
    pratoom_angurarohita = Lecturer.Lecturer('pratoom_angurarohita', [])
    surin_kittitornkun = Lecturer.Lecturer('surin_kittitornkun', [])
    kulwadee_somboonviwat = Lecturer.Lecturer('kulwadee_somboonviwat', [])
    prakash_chanchana = Lecturer.Lecturer('prakash_chanchana', [])
    visit_hirankitti = Lecturer.Lecturer('visit_hirankitti', [])
    isara_anantavrasilp = Lecturer.Lecturer('isara_anantavrasilp', [])
    boontee_kruatrachue = Lecturer.Lecturer('boontee_kruatrachue', [])
    natthapong_jungteerapanich = Lecturer.Lecturer('natthapong_jungteerapanich',[])
    todsanai_chumwatana = Lecturer.Lecturer('todsanai_chumwatana', [])

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
    genetic_function(limit_random, number_of_generation, room_list, course_list, lecturer_list, student_group_list)

main()
