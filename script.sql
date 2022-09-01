DROP TABLE IF EXISTS "data";

CREATE TABLE "data" (
	id SERIAL PRIMARY KEY, 
	create_at timestamp default now(),
	salary integer NULL,
	group_names char(1) default NULL,
	email varchar(255) default NULL,
	phone varchar(100) default NULL,
	names varchar(255) default NULL
);

INSERT INTO data (salary, group_names, email, phone, names)
VALUES
	(475840, 'A', 'Georgette@gmail.com', '0626251615', 'Joseph Selkirk'),
	(483058, 'C', 'Sean@gmail.com', '0620636754', 'Karen Peterson'),
	(752584, 'B', 'Susan@gmail.com', '0626215707', 'Kenton Mcgovern'),
	(151997, 'C', 'Billie@gmail.com', '0162644777', 'Michael Hayes'),
	(143154, 'B', 'Elease@gmail.com', '0506716503', 'Miguel Anderman'),
	(283330, 'A', 'Lloyd@gmail.com', '0714003661', 'Tamara Jackson'),
	(862156, 'A', 'Zachary@gmail.com', '0176646244', 'Dorothy Hanks'),
	(875268, 'C', 'Crystal@gmail.com', '0564117704', 'Richard Greenlief'),
	(178972, 'C', 'Sharon@gmail.com', '0330024121', 'Donna Myers'),
	(899593, 'A', 'Timothy@gmail.com', '0365430714', 'Kenneth Gaston');