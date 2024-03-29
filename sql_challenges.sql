
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


-- AGGREGATIONS - SUM
-- https://www.hackerrank.com/challenges/revising-aggregations-sum

-- Query total population with constraint - no call for group by here :
select sum(population)
from city
where district = 'California';


-- AGGREGATIONS - AVERAGE, AND CASTING AS INTEGER 
-- https://www.hackerrank.com/challenges/average-population

-- Mysql speciality - signed (for negatives) and unsigned integers :

select cast(avg(population) as unsigned)
from city;

-- AGGREGATIONS - SUM, BETWEEN, ROUND 
-- https://www.hackerrank.com/challenges/weather-observation-station-13

select round(sum(lat_n), 4)
from station
where lat_n between 38.7880 and 137.2345;


-- SELECT FIELD BASED ON ANOTHER FIELD
-- https://www.hackerrank.com/challenges/weather-observation-station-15

-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is 
-- less than 137.2345. Round your answer to 4 decimal places.
select round(long_w,4)
from station
where lat_n < 137.2345
order by lat_n desc
limit 1;

-- or alternatively :
select round(long_w,4)
from station
where lat_n = (select max(lat_n) from station
where lat_n < 137.2345);


-- AVERAGE POPULATION OF EACH CONTINENT, CAST AND FLOOR
-- https://www.hackerrank.com/challenges/average-population-of-each-continent

-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and 
-- their respective average city populations (CITY.Population) rounded down to the nearest integer.
select country.continent, cast(avg(city.population) as signed)
from city
inner join country
on city.countrycode=country.code
group by country.continent;

-- Gives wrong answer :
-- Your Output (stdout)
--    Asia 693038
--    Oceania 109190
--    Europe 175138
--    South America 147435
--    Africa 274439

-- whereas ...

select country.continent, floor(avg(city.population))
from city
inner join country
on city.countrycode=country.code
group by country.continent;

-- .. Gives right answer - ie "...rounded DOWN..."
-- Your Output (stdout)
--    Asia 693038
--    Oceania 109189
--    Europe 175138
--    South America 147435
--    Africa 274439

