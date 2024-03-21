% Define symptoms and their associated diseases
symptom(fever, flu).
symptom(cough, flu).
symptom(fatigue, flu).
symptom(sore_throat, flu).
symptom(runny_nose, flu).
symptom(vomiting, flu).
symptom(diarrhea, flu).

symptom(fever, cold).
symptom(cough, cold).
symptom(runny_nose, cold).
symptom(sneezing, cold).
symptom(sore_throat, cold).

% Rules for diagnosing diseases based on symptoms
diagnose(Disease, Symptoms) :-
    findall(D, (symptom(S, D), member(S, Symptoms)), Diseases),
    list_to_set(Diseases, UniqueDiseases),
    member(Disease, UniqueDiseases).

OUTPUT:
% ?- diagnose(Disease, [fever, cough, sore_throat]).
% Disease = flu.
