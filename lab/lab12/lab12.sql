.read fa16data.sql
.read sp17data.sql

CREATE TABLE obedience AS
  select seven, hilfinger from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 16 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select s.date, s.color, s.pet, s.number, f.number from students as s, fa16students as f where s.date = f.date and s.color = f.color and s.pet = f.pet;

CREATE TABLE sevens AS
  select s.seven from students as s, checkboxes as c where s.time = c.time and s.number = 7  and c.'7' = "True";

CREATE TABLE matchmaker AS
  select f.pet, f.song, f.color, s.color from students as f, students as s where f.pet = s.pet and f.song = s.song and f.time < s.time;
