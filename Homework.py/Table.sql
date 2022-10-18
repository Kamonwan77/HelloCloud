SELECT Students.student_id , Students.f_name ,Students.l_name 
, Subjects.subject_id , Subjects.subject_name
,Registration.grade , Teacher.f_name , Teacher.l_name from Students

JOIN Registration
    on Students.student_id = Registration.student_id
JOIN Subjects
    on Registration.subject_id = Subjects.subject_id
JOIN Teacher
    on Subjects.teacher_id = Teacher.teacher_id
;