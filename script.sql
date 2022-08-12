DROP TABLE IF EXISTS "data";

CREATE TABLE "data" (
	id SERIAL PRIMARY KEY, 
	names varchar(255) default NULL,
	phone varchar(100) default NULL,
	email varchar(255) default NULL,
	salary integer NULL
);

INSERT INTO data (names, phone, email, salary)
VALUES
	('Rebecca Hinson', '0415263155', 'Laura@gmail.com', 360518),
	('Dannette Gray', '0001471725', 'Debra@gmail.com', 388704),
	('Donna Williams', '0305124540', 'Louise@gmail.com', 343808),
	('Edwin Benford', '0157047204', 'Chris@gmail.com', 344153),
	('Jose Floyd', '0603050654', 'Calvin@gmail.com', 915815),
	('Dennis Davis', '0357370737', 'Gerald@gmail.com', 140687),
	('Stanley Bunch', '0643032504', 'Bessie@gmail.com', 159718),
	('Frederick Merchant', '0635165541', 'Joan@gmail.com', 442550),
	('Amber Phillip', '0243371513', 'Lea@gmail.com', 522363),
	('Susan Solanki', '0656037035', 'Dustin@gmail.com', 166441);