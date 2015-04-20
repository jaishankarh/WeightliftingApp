from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import *
from sqlalchemy import UniqueConstraint

from sqlalchemy import create_engine

engine = create_engine('sqlite:///wl.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = scoped_session(Session)

# dbQuery('CREATE TABLE IF NOT EXISTS MEMBER(id INTEGER PRIMARY KEY AUTOINCREMENT, fname VARCHAR(30), lname VARCHAR(30), grp VARCHAR(2), gender VARCHAR(10), dob VARCHAR(10)')
# dbQuery("CREATE TABLE IF NOT EXISTS LIFT_TYPES(id INTEGER PRIMARY KEY AUTOINCREMENT, liftType VARCHAR(30), liftName VARCHAR(30))")
# dbQuery("CREATE TABLE IF NOT EXISTS COEFFICIENTS(id INTEGER PRIMARY KEY AUTOINCREMENT, liftid INTEGER, value REAL, FOREIGN KEY(liftid) REFERENCES LIFTS(id) ON DELETE CASCADE)")
# dbQuery("CREATE TABLE IF NOT EXISTS LIFTS(id INTEGER PRIMARY KEY AUTOINCREMENT, body_weight REAL, mem_id INTEGER, lift_id INTEGER, year INTEGER, date VARCHAR(10), lift_weight REAL, FOREIGN KEY(lift_id) REFERENCES LIFTS(id) ON DELETE CASCADE, FOREIGN KEY(mem_id) REFERENCES MEMBER(id) ON DELETE CASCADE)")
# dbQuery("CREATE TABLE IF NOT EXISTS COMPETITION(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30), mem_id INTEGER, lift_id INTEGER, year INTEGER, date VARCHAR(10), lift_weight REAL, FOREIGN KEY(lift_id) REFERENCES LIFTS(id) ON DELETE CASCADE, FOREIGN KEY(mem_id) REFERENCES MEMBER(id) ON DELETE CASCADE)")

Comp_lifts = Table('COMP_MEMBERS', Base.metadata,
    Column('mem_id', Integer, ForeignKey('MEMBER.id')),
    Column('comp_id', Integer, ForeignKey('COMPETITION.id')),
    UniqueConstraint('mem_id', 'comp_id')
)

class Member(Base):
    __tablename__ = 'MEMBER'

    id = Column(Integer, primary_key=True)
    fname = Column(String(40))
    lname = Column(String(40))
    grp = Column(String(2))
    gender = Column(String(10))
    dob = Column(String(10))
    lifts = relationship("Lift",  cascade="all, delete-orphan", backref=backref("member"))
    competitions = relationship("Competition", secondary=Comp_lifts, backref=backref("members"))

    def __repr__(self):
        return "<Member(fname='%s', lname='%s', dob='%s')>" % (self.fname, self.lname, self.dob)


class Lift_Type(Base):
    __tablename__ = 'LIFT_TYPE'

    id = Column(Integer, primary_key=True)
    liftType = Column(String(40))
    liftName = Column(String(40))
    UniqueConstraint('liftType', 'liftName', name='lift_constraint')

    def __repr__(self):
        return "<Lift_Type(Type='%s', Name='%s')>" % (self.liftType, self.liftName)

class Coefficient(Base):
    __tablename__ = 'COEFFICIENT'

    id = Column(Integer, primary_key=True)
    gender = Column(String(10))
    liftType = Column(String(40))
    year = Column(Integer)
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    d = Column(Float)
    e = Column(Float)
    f = Column(Float)
    comp_id = Column(Integer, ForeignKey('COMPETITION.id'))

    def __repr__(self):
        return "<Coefficient(Type='%s', Year='%s, a='%s, b='%s, c='%s, d='%s, e='%s, f='%s,')>" % (self.liftType, self.year, self.a, self.b, self.c, self.d, self.e, self.f)

class Lift(Base):
    __tablename__ = 'LIFT'

    id = Column(Integer, primary_key=True)
    body_weight = Column(Float)
    date = Column(String(10))
    lift_weight = Column(Float)
    mem_id = Column(Integer, ForeignKey('MEMBER.id'))
    #member_obj = relationship("Member", backref="lifts")
    liftType_id = Column(Integer, ForeignKey('LIFT_TYPE.id'))
    lift_type = relationship("Lift_Type", backref=backref("lifts", cascade="all, delete-orphan"))
    competition_id = Column(Integer, ForeignKey('COMPETITION.id'))
    competition = relationship("Competition", backref=backref("lifts", cascade="all, delete-orphan"))

    __table_args__ = (UniqueConstraint('mem_id', 'liftType_id', "competition_id"),)

    def __repr__(self):
        return "<Lift(Member='%s', Lift Name='%s', Lift Weight='%s', Competition year='%s')>"  %(self.member.fname + " " + self.member.lname, self.lift_type.liftName, self.lift_weight, self.competition.year)


class Competition(Base):
    __tablename__ = 'COMPETITION'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    year = Column(Integer)
    coefficients = relationship("Coefficient", cascade="all, delete-orphan", backref=backref("competition"))


    def __repr__(self):
        return "<Competition(Name='%s', Year='%s')>" % (self.name, self.year)

# class RecordClasses(Base):
#     __tablename__ = 'RECORD_CLASS'
#
#     id = Column(Integer, primary_key=True)
#     gender = Column(String(10))
#     className = Column(String(20))
#     classWeight = Column(Float)
#
# class Record(Base):
#




Base.metadata.create_all(engine)
lifts = session.query(Lift_Type).all()
if len(lifts) == 0:
    snatch = Lift_Type(id=1, liftType="Olympic Lift", liftName="Snatch")
    cleanJerk = Lift_Type(id=2, liftType="Olympic Lift", liftName="Clean and Jerk")

    squat = Lift_Type(id=3, liftType="Power Lift", liftName="Squat")
    benchPress = Lift_Type(id=4, liftType="Power Lift", liftName="Bench Press")
    deadLift = Lift_Type(id=5, liftType="Power Lift", liftName="Dead Lift")

    try:
        session.add(snatch)
        session.add(cleanJerk)
        session.add(squat)
        session.add(benchPress)
        session.add(deadLift)
        session.commit()
    except:
        session.rollback()
        raise

comp = session.query(Competition).first()
if comp is None:
    global comp
    comp = Competition(name="Competition 2015", year=2015)
    try:
        session.add(comp)
        session.commit()
    except:
        self.session.rollback()
coeffs = session.query(Coefficient).all()
if len(coeffs) == 0:
    global comp
    powerLiftsCoeff = Coefficient(gender="Male", liftType="Power Lift", year=2015, a=-216.0475144, b=16.2606339, c=-0.002388645, d=-0.00113732, e=7.01863E-06, f=-1.291E-08,competition=comp)
    olympicliftCoeff = Coefficient(gender="Male", liftType="Olympic Lift", year=2015, a=0.784780654, b=173.961, c=0, d=0, e=0, f=0,competition=comp)
    olympicliftCoeff2 = Coefficient(gender="Female", liftType="Olympic Lift", year=2015, a=1.056683941, b=125.441, c=0, d=0, e=0, f=0,competition=comp)

    try:
        session.add(powerLiftsCoeff)
        session.add(olympicliftCoeff)
        session.add(olympicliftCoeff2)
        session.commit()
    except:
        session.rollback()
        raise
