INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('1','Jaishankar','Hebballi','D','Male','16-01-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('2','Nishtha','Shoney','C','Female','10-09-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('3','Akash','Hebballi','D','Male','12-03-2000');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('4','Prithiv','Sassisegarane','D','Male','10-11-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('5','Rohan','Kandoi','D','Male','07-07-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('6','Dheeraj','Somani','D','Male','25-07-1991');
INSERT INTO "MEMBER" ("id","fname","lname","grp","gender","dob") VALUES ('7','Apurva','Shavadia','D','Male','23-05-1990');


INSERT INTO "COMPETITION" ("id","name","year") VALUES ('1','Competition 2015','2015');


INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('1','1');
INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('3','1');
INSERT INTO "COMP_MEMBERS" ("mem_id","comp_id") VALUES ('6','1');


INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('1','86.8','16-12-2014','48.0','1','1','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('2','86.5','18-12-2014','45.2','1','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('3','75.5','18-12-2014','50.2','6','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('4','45.5','18-12-2014','50.0','3','2','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('5','45.5','18-12-2014','30.0','3','1','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('6','86.8','20-12-2014','167.0','1','5','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('7','45.8','20-12-2014','132.0','3','5','1');
INSERT INTO "LIFT" ("id","body_weight","date","lift_weight","mem_id","liftType_id","competition_id") VALUES ('8','77.8','20-12-2014','178.0','6','5','1');
