select name, age, sex
from members
where sex = 'm'
and age > 20
order by name asc;

select name, age, sex, likes
from members
where likes = 'dancing'
order by name asc;

select name, age, sex, likes
from members
where sex = 'm'
and likes = 'politics'
order by name asc;

select name, age, sex, likes, dislikes
from members
where likes = dislikes;

select name, age, sex
from members
where sex = 'f'
and age > 20 
and age < 40
order by age desc;

select name, age, sex
from members
where sex = 'f'
and age between 20 and 40
order by age desc;

select name
from members
where name like 'a%';

select name
from members
where name like '_a%';

select *
from members
where likes like '%ing';

select name
from members
where likes = 'football'
or likes = 'golf';

select name, likes, earns
from members
where likes in ('football', 'golf')
order by earns desc;