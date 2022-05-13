
-- Selected SQL problems from the Hackerrank challenges.
-- Flavour is MySql.

-- REGEXP

-- https://www.hackerrank.com/challenges/weather-observation-station-6
select distinct city
from station
where city regexp '^[aeiou]';

-- https://www.hackerrank.com/challenges/weather-observation-station-7
select distinct city from station
where city regexp '[aeiou]$';

-- https://www.hackerrank.com/challenges/weather-observation-station-9
select distinct city from station
where not city regexp '^[aeiou]';


-- TYPE OF TRIANGLE

-- https://www.hackerrank.com/challenges/what-type-of-triangle

select case
when A+B>C and A+C>B and B+C>A then
    case
    when A=B and A=C then 'Equilateral'
    when A=B or A=C or B=C then 'Isosceles'
    else 'Scalene'
    end
    else 'Not A Triangle'
end
from triangles;


-- MEDIAN VALUE

-- https://www.hackerrank.com/challenges/weather-observation-station-20

-- Prime row_index to start at 0
set @row_index := -1;

-- Sort, then get just the values either side of 
-- the middle value, or the middle value itself if odd number of rows
-- then take the average of this/these, then round to 4dp
select round(avg(lat_n),4) from
(select @row_index:=@row_index + 1 as row_index, lat_n
from station
order by lat_n) as subq
where subq.row_index in
(floor(@row_index/2), ceil(@row_index/2));
