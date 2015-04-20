----
-- phpLiteAdmin database dump (http://phpliteadmin.googlecode.com)
-- phpLiteAdmin version: 1.9.5
-- Exported: 12:07am on December 19, 2014 (IST)
-- database file: /home/jaishankar/PycharmProjects/weight_lifting/wl.db
----
BEGIN TRANSACTION;

----
-- Table structure for LIFT_TYPE
----
CREATE TABLE "LIFT_TYPE" (
	id INTEGER NOT NULL, 
	"liftType" VARCHAR(40), 
	"liftName" VARCHAR(40), 
	PRIMARY KEY (id)
);

----
-- Data dump for LIFT_TYPE, a total of 5 rows
----
INSERT INTO "LIFT_TYPE" ("id","liftType","liftName") VALUES ('1','Olympic Lift','Snatch');
INSERT INTO "LIFT_TYPE" ("id","liftType","liftName") VALUES ('2','Olympic Lift','Clean and Jerk');
INSERT INTO "LIFT_TYPE" ("id","liftType","liftName") VALUES ('3','Power Lift','Squat');
INSERT INTO "LIFT_TYPE" ("id","liftType","liftName") VALUES ('4','Power Lift','Bench Press');
INSERT INTO "LIFT_TYPE" ("id","liftType","liftName") VALUES ('5','Power Lift','Dead Lift');

----
-- Table structure for COEFFICIENT
----
CREATE TABLE "COEFFICIENT" (
	id INTEGER NOT NULL, 
	gender VARCHAR(10), 
	"liftType" VARCHAR(40), 
	year INTEGER, 
	a FLOAT, 
	b FLOAT, 
	c FLOAT, 
	d FLOAT, 
	e FLOAT, 
	f FLOAT, 
	PRIMARY KEY (id)
);

----
-- Data dump for COEFFICIENT, a total of 3 rows
----
INSERT INTO "COEFFICIENT" ("id","gender","liftType","year","a","b","c","d","e","f") VALUES ('1','Male','Power Lift','0','-216.0475144','16.2606339','-0.002388645','-0.00113732','7.01863e-06','-1.291e-08');
INSERT INTO "COEFFICIENT" ("id","gender","liftType","year","a","b","c","d","e","f") VALUES ('2','Male','Olympic Lift','2014','0.784780654','173.961','0.0','0.0','0.0','0.0');
INSERT INTO "COEFFICIENT" ("id","gender","liftType","year","a","b","c","d","e","f") VALUES ('3','Female','Olympic Lift','2014','1.056683941','125.441','0.0','0.0','0.0','0.0');

----
-- Table structure for MEMBER
----
CREATE TABLE "MEMBER" (
	id INTEGER NOT NULL, 
	fname VARCHAR(40), 
	lname VARCHAR(40), 
	grp VARCHAR(2), 
	gender VARCHAR(10), 
	dob VARCHAR(10), 
	PRIMARY KEY (id)
);

----
-- Data dump for MEMBER, a total of 7 rows
----
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('1','Jaishankar','Hebballi','D','Male','16-01-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('2','Nishtha','Shoney','C','Female','10-09-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('3','Akash','Hebballi','D','Male','12-03-2000');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('4','Prithiv','Sassisegarane','D','Male','10-11-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('5','Rohan','Kandoi','D','Male','07-07-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('6','Dheeraj','Somani','D','Male','25-07-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('7','Apurva','Shavadia','D','Male','23-05-1990');

----
-- Table structure for COMPETITION
----
CREATE TABLE "COMPETITION" (
	id INTEGER NOT NULL, 
	name VARCHAR(40), 
	year INTEGER, 
	PRIMARY KEY (id)
);

----
-- Data dump for COMPETITION, a total of 1 rows
----
INSERT INTO "COMPETITION" ("id","name","year") VALUES ('1','competition 2009','2009');

----
-- Table structure for COMP_MEMBERS
----
CREATE TABLE "COMP_MEMBERS" (
	mem_id INTEGER, 
	comp_id INTEGER, 
	UNIQUE (mem_id, comp_id), 
	FOREIGN KEY(mem_id) REFERENCES "MEMBER" (id), 
	FOREIGN KEY(comp_id) REFERENCES "COMPETITION" (id)
);

----
-- Data dump for COMP_MEMBERS, a total of 3 rows
----
INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('1','1');
INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('3','1');
INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('6','1');

----
-- Table structure for LIFT
----
CREATE TABLE "LIFT" (
	id INTEGER NOT NULL, 
	body_weight FLOAT, 
	date VARCHAR(10), 
	lift_weight FLOAT, 
	mem_id INTEGER, 
	"liftType_id" INTEGER, 
	competition_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (mem_id, "liftType_id", competition_id), 
	FOREIGN KEY(mem_id) REFERENCES "MEMBER" (id), 
	FOREIGN KEY("liftType_id") REFERENCES "LIFT_TYPE" (id), 
	FOREIGN KEY(competition_id) REFERENCES "COMPETITION" (id)
);

----
-- Data dump for LIFT, a total of 8 rows
----
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('1','86.8','16-12-2009','48.0','1','1','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('2','86.5','18-12-2009','45.2','1','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('3','75.5','18-12-2009','50.2','6','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('4','45.5','18-12-2009','50.0','3','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('5','45.5','18-12-2009','30.0','3','1','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('6','86.8','20-12-2009','167.0','1','5','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('7','45.8','20-12-2009','132.0','3','5','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('8','77.8','20-12-2009','178.0','6','5','1');

----
-- structure for index sqlite_autoindex_COMP_MEMBERS_1 on table COMP_MEMBERS
----
;

----
-- structure for index sqlite_autoindex_LIFT_1 on table LIFT
----
;
COMMIT;
