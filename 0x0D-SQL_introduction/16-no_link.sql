-- a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

SELECT ALL (score, name) from second_table WHERE NAME IS NOT NULL or name!='' ORDER BY score DESC;
