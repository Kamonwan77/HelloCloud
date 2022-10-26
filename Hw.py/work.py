from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, CHAR, VARCHAR, Integer, String, Text, DateTime, Float, Boolean, PickleType

Base = declarative_base()
db_uri = 'sqlite:///work.sqlite3'
engine = create_engine(db_uri, echo=False)

class Students(Base):
    __tablename__ = 'Students' 
    student_id = Column(String(13),primary_key = True,nullable = True) 
    f_name = Column(String(30),nullable = False) 
    l_name = Column(String(30),nullable=False) 
    e_mail = Column(String(50), nullable=False) 

    def __repr__(self):
        return '<User(student_id = {}, f_name = {}, l_name = {}, e_mail ={})>'.format(self.student_id, self.f_name, self.l_name, self.e_mail)
        

class Registration(Base):
    __tablename__ = 'Registration' 
    id = Column(Integer(), primary_key = True)
    student_id = Column(String(13)) 
    subject_id = Column(String(15),nullable = False) 
    year = Column(String(4),nullable=False) 
    semester = Column(String(1),nullable=False)  
    grade = Column(String(2))

    def __repr__(self):
        return '<User(student_id = {}, subject_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, \
            self.subject_id, self.year , self.semester, self.grade)

class Subjects(Base):
    __tablename__ = 'Subjects' 
    subject_id = Column(String(15),primary_key = True) 
    subject_name = Column(String(50),nullable = False) 
    credit = Column(Integer(),nullable=False) 
    teacher_id = Column(String(3),nullable=False) 
    def __repr__(self):
        return '<User(subject_id = {}, subject_name = {}, credit = {}, teacher_id ={})>'.format(self.subject_id, \
            self.subject_name, self.credit , self.teacher_id)

class Teacher(Base):
    __tablename__ = 'Teachers' 
    teacher_id = Column(String(3),primary_key=True, nullable=True)
    f_name = Column(String(50), nullable=True)
    l_name = Column(String(30), nullable=True)
    e_mail = Column(String(50), nullable=True)

    def __repr__(self):
            return '<User(teacher_id = {} , f_name= {} , l_name = {} , e_mail = {})>'.format(self.teacher_id,\
                    self.f_name, self.l_name , self.e_mail)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()



user1 = Students(
    student_id ='6406022630016',
    f_name='Kamonwan',
    l_name='Janmanee',
    e_mail ='s6406022630016@email.kmutnb.ac.th'
)

user2 = Students(
    student_id ='6406022620061',
    f_name='Mathawee',
    l_name='Robkob',
    e_mail ='s6406022620061@email.kmutnb.ac.th'
)

user3 = Students(
    student_id ='6406022610058',
    f_name='Piyawan',
    l_name='Nimpraprut',
    e_mail ='s6406022610058@email.kmutnb.ac.th'
)



regis1 = Registration(
    student_id ='6406022630016',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis2 = Registration(
    student_id ='6406022630016',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'C+'
)

regis3 = Registration(
    student_id ='6406022620061',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis4 = Registration(
    student_id ='6406022620061',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'B+'
)

regis5 = Registration(
    student_id ='6406022610058',
    subject_id='060233205',
    year='2565',
    semester ='1',
    grade = 'B'
)

regis6 = Registration(
    student_id ='6406022610058',
    subject_id='060233113',
    year='2565',
    semester ='1',
    grade = 'C'
)


sub1 = Subjects(subject_id ='060233205',subject_name='Advance network and protocol',credit='3',teacher_id ='KNM')
sub2 = Subjects(subject_id ='060233113',subject_name='Advance Computer Programming',credit='1',teacher_id ='AMK')

Tea1 = Teacher(teacher_id='KNM',f_name='Khanista',l_name='Namee', e_mail='Khanista@gmail.com')
Tea2 = Teacher(teacher_id='AMK',f_name='Anirach',l_name='Mingkhwan',e_mail='Anirach@gmail.com')

session.add_all([user1,user2,user3,regis1, regis2, regis3, regis4, regis5, regis6, sub1 ,sub2, Tea1,Tea2])
session.commit()