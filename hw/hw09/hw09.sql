create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where dogs.height > sizes.min and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select a.name from dogs as a, dogs as b, parents where child = a.name and b.name = parent order by b.height desc;

-- Sentences about siblings that are the same size
create table sentences as
with siblings(sib1, sib2) as (select s1.child, s2.child from parents as s1, parents as s2 where s1.parent = s2.parent and s1.child != s2.child and s1.child < s2.child)
select sib1 || " and " ||  sib2 || " are " || a.size || " siblings" from siblings, size_of_dogs as a, size_of_dogs as b where a.name = sib1 and b.name = sib2 and a.size = b.size;  

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with helper(d1, d2, d3, d4, h) as (
    select a.name, b.name, b.height, 0, a.height+b.height  from dogs as a, dogs as b where a.height < b.height union
    select d1, d2, c.name, d.name, h+c.height+d.height from helper, dogs as c, dogs as d where d3 < c.height and c.height < d.height)
  select d1 || ", " || d2 || ", " || d3 || ", " || d4, h from helper where d4 != 0 and h>170 order by h;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  with combos(a, b) as (
    select c.*, d.* from ints as c, ints as d)
  , helper(col) as (
    select a from combos where a % b = 0)
  select col as col1, count(col) as col2 from helper group by col;

create table primes as
  select col1 from divisors where col2 = 2;
