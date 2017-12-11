%Year1 semester1 Course
course(academicEnglish1,y1).
course(basicElectricityandElectronics,y1).
course(cProgramming,y1).
course(cprogrammingLaboratory,y1).
course(calculus1,y1).
course(introductiontoComputersandProgrammings,y1).
course(introductiontoLogic,y1).

%Year2 semester1 Course
course(advanceObjectOrientedProgramming,y2).
course(computerOrganizationandAssemblyLanguage,y2).
course(computerOrganizationandAssemblyLanguageLaboratory,y2).
course(dataStructuresandAlgorithm,y2).
course(dataStructuresandAlgorithmLaboratory,y2).
course(linearAlgebra,y2).
course(tecnicalWriting,y2).

%Year3 semester1 Course
course(artificialIntelligent,y3).
course(databaseSystems,y3).
course(objectOrientedAnalysisandDesign,y3).
course(objectOrientedAnalysisandDesignLaboratory,y3).
course(operatingSystems,y3).
course(theoryofComputation,y3).
course(webProgramming,y3).

%Year4 semester1 Course
course(humanComputerInteraction,y4).
course(softwareProject1,y4).
course(softwareVerificationandValidation,y4).

lecturer(montri_phothisonothai).
lecturer(ukrit_watchareeruetai).
lecturer(ronnachai_tiyarattanachai).
lecturer(natthapong_jungteerapanich).
lecturer(chaiwat_nuthong).
lecturer(churirat_boonkhun).
lecturer(kulwadee_somboonviwat).
lecturer(pipat_sookavatana).
lecturer(chivalai_temiyasathit).
lecturer(veera_boonjing).
lecturer(jochen_amrehn).
lecturer(xavier_boegly).
lecturer(isara_anantavrasilp).
lecturer(visit_hirankitti).
lecturer(pratoom_angurarohita).
lecturer(prakash_chanchana).
lecturer(surin_kittitornkun).
lecturer(suphamit_chittayasothorn).
lecturer(lily_ingsrisawang).
lecturer(vorapranee_khusmith).
lecturer(tatre_jantarakolica).
lecturer(boontee_kruatrachue).
lecturer(todsanai_chumwatana).
lecturer(yunyong_tengamnuay).
lecturer(rutchanee_gullayanon).
lecturer(kasin_vichienchom).
lecturer(teerawet_titseesang).

%y1
teach(montri_phothisonothai,basicElectricityandElectronics).
teach(ukrit_watchareeruetai,cProgramming).
teach(ukrit_watchareeruetai,cprogrammingLaboratory).
teach(ronnachai_tiyarattanachai,calculus1).
teach(veera_boonjing,introductiontoComputersandProgrammings).
teach(pratoom_angurarohita,introductiontoLogic).

%y2
teach(veera_boonjing,advanceObjectOrientedProgramming).
teach(surin_kittitornkun,computerOrganizationandAssemblyLanguage).
teach(surin_kittitornkun,computerOrganizationandAssemblyLanguageLaboratory).
teach(kulwadee_somboonviwat,dataStructuresandAlgorithm).
teach(kulwadee_somboonviwat,dataStructuresandAlgorithmLaboratory).
teach(linearAlgebra,prakash_chanchana).

%y3
teach(visit_hirankitti,artificialIntelligent).
teach(kulwadee_somboonviwat,databaseSystems).
teach(isara_anantavrasilp,objectOrientedAnalysisandDesign).
teach(isara_anantavrasilp,objectOrientedAnalysisandDesignLaboratory).
teach(boontee_kruatrachue,operatingSystems).
teach(natthapong_jungteerapanich,theoryofComputation).
teach(todsanai_chumwatana,webProgramming).

%y4
teach(montri_phothisonothai,humanComputerInteraction).
teach(natthapong_jungteerapanich,softwareVerificationandValidation).

%Lecturer timeslot
lectureTimeslot(montri_phothisonothai, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(ukrit_watchareeruetai, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(ronnachai_tiyarattanachai, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(chaiwat_nuthong, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(churirat_boonkhun, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(kulwadee_somboonviwat, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(pipat_sookavatana, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(jochen_amrehn, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(xavier_boegly, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(isara_anantavrasilp, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(visit_hirankitti, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(pratoom_angurarohita, [0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(prakash_chanchana, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(surin_kittitornkun, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(suphamit_chittayasothorn, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(lily_ingsrisawang, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(vorapranee_khusmith, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(tatre_jantarakolica, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(boontee_kruatrachue, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(todsanai_chumwatana, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(yunyong_tengamnuay, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(rutchanee_gullayanon, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(kasin_vichienchom, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
lectureTimeslot(teerawet_titseesang, [0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0]).
