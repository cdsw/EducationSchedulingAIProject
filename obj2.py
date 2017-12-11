class Course:
    def __init__(self,lect,year):
        self.lect = lect
        self.year = year

class Room:
    def __init__(self):
        self.timeslot=[[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

class Lecturer:
    def __init__(self):
        self.time_preference_timeslot=[[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

class StudentGroup:
    def __init__(self):
        self.timeslot=[[],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[], [],[],[]]

class Schedule:
    def __init__(self):
        rooms = []
    def addRoom(self,Room):
        rooms.append(Room)

y1= StudentGroup()
y2= StudentGroup()
y3= StudentGroup()
y4= StudentGroup()

ic01=Room()
ic06=Room()
ic16=Room()
ic04=Room()

montri_phothisonothai = Lecturer()
ukrit_watchareeruetai = Lecturer()
ronnachai_tiyarattanachai = Lecturer()
natthapong_jungteerapanich = Lecturer()
chaiwat_nuthong = Lecturer()
churirat_boonkhun = Lecturer()
kulwadee_somboonviwat = Lecturer()
pipat_sookavatana = Lecturer()
chivalai_temiyasathit = Lecturer()
veera_boonjing = Lecturer()
jochen_amrehn = Lecturer()
xavier_boegly = Lecturer()
isara_anantavrasilp = Lecturer()
visit_hirankitti = Lecturer()
pratoom_angurarohita = Lecturer()
prakash_chanchana = Lecturer()
surin_kittitornkun = Lecturer()
suphamit_chittayasothorn = Lecturer()
lily_ingsrisawang = Lecturer()
vorapranee_khusmith = Lecturer()
tatre_jantarakolica = Lecturer()
boontee_kruatrachue = Lecturer()
todsanai_chumwatana = Lecturer()
yunyong_tengamnuay = Lecturer()
rutchanee_gullayanon = Lecturer()
kasin_vichienchom = Lecturer()
teerawet_titseesang = Lecturer()

basicElectricityandElectronics = Course(montri_phothisonothai,"y1")
cProgramming = Course(ukrit_watchareeruetai,"y1")
cprogrammingLaboratory = Course(ukrit_watchareeruetai,"y1")
calculus1 = Course(ronnachai_tiyarattanachai.addCourse,"y1")
introductiontoComputersandProgrammings = Course(veera_boonjing,"y1")
introductiontoLogic = Course(pratoom_angurarohita,"y1")

advanceObjectOrientedProgramming = Course(veera_boonjing,"y2")
computerOrganizationandAssemblyLanguage = Course(surin_kittitornkun,"y2")
computerOrganizationandAssemblyLanguageLaboratory = Course(surin_kittitornkun,"y2")
dataStructuresandAlgorithm = Course(kulwadee_somboonviwat,"y2")
dataStructuresandAlgorithmLaboratory = Course(kulwadee_somboonviwat,"y2")
linearAlgebra = Course(prakash_chanchana,"y2")

artificialIntelligent = Course(visit_hirankitti,"y3")
databaseSystems = Course(kulwadee_somboonviwat,"y3")
objectOrientedAnalysisandDesign = Course(isara_anantavrasilp,"y3")
objectOrientedAnalysisandDesignLaboratory = Course(isara_anantavrasilp,"y3")
operatingSystems = Course(boontee_kruatrachue,"y3")
theoryofComputation = Course(natthapong_jungteerapanich,"y3")
webProgramming = Course(todsanai_chumwatana,"y3")

humanComputerInteraction = Course(montri_phothisonothai,"y4")
softwareVerificationandValidation = Course(natthapong_jungteerapanich,"y4")
