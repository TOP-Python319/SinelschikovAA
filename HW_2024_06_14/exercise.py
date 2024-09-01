# ДЗ.

# Задание 1.

SELECT 
name, year, appearances
FROM 
MarvelCharacters 
WHERE 
hair = "Bald" AND 
ALIGN = "Bad Characters" AND 
year between 1990 and 1999 
ORDER by YEAR;

# Задание 2.

SELECT name, year, EYE
From MarvelCharacters
Where eye IS NOT NULL AND identify = "Secret Identity" AND 
eye != "Blue Eyes" AND eye != "Brown Eyes" and eye != "Green Eyes";

# Задание 3.

SELECT name, hair
FROM MarvelCharacters 
WHERE hair = "Variable Hair";

# Задание 4.

SELECT name, eye
From MarvelCharacters
WHERE sex = 'Female Characters' AND eye IN ("Gold Eyes", "Amber Eyes");

# Задание 5.

SELECT name, FIRST_APPEARANCE
from MarvelCharacters 
WHERE identify = "No Dual Identity"
ORDER BY 
year DESC ;

# Задание 6.

SELECT name, align, hair
FROM MarvelCharacters 
WHERE Hair NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair') AND align IN ('Good Characters', 'Bad Characters');

# Задание 7.

SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE year between 1960 and 1969;

# Задание 8.

SELECT name, eye, hair
from MarvelCharacters 
where eye = "Yellow Eyes" AND hair = "Red Hair";

# Задание 9.

SELECT name, APPEARANCES 
FROM MarvelCharacters
WHERE APPEARANCES < 10;

# Задание 10.

SELECT name, APPEARANCES
FROM MarvelCharacters 
ORDER BY APPEARANCES DESC
LIMIT 5;

# Задание 11.

SELECT name, YEAR 
From MarvelCharacters 
WHERE year between 2000 AND 2009;

# Задание 12.

SELECT name, eye
FROM MarvelCharacters mc 
WHere eye IN ("Magenta Eyes", "Pink Eyes", "Violet Eyes");

# Задание 13.

SELECT name, identify, year
FROM MarvelCharacters mc 
WHERE identify = "Public Identity"
ORDER BY year ASC;

# Задание 14.

SELECT name, hair, eye
FROM MarvelCharacters mc 
WHERE hair = "Black Hair" and eye = "Green Eyes"
ORDER BY name 

# Задание 15.

SELECT name, sex
FROM MarvelCharacters mc 
WHERE sex NOT IN ('Male Characters' , 'Female Characters') AND Align = "Bad Characters";

# Задание 16.

SELECT name, sex, max(appearances)
FROM MarvelCharacters mc 
WHERE sex IN ('Male Characters' , 'Female Characters')
GROUP BY sex;

# Задание 17.

SELECT hair, eye, sum(appearances) as сумма
from MarvelCharacters 
WHERE  hair != '' AND eye != ''
GROUP BY 
hair, eye
HAVING сумма != 0
ORDER BY 
сумма DESC

# Задание 18.

WITH overall_decades AS
(SELECT name, appearances, (year / 10) * 10 as decade
FROM MarvelCharacters
WHERE Year IS NOT NULL AND year >= 1940)
SELECT name, max(appearances), decade
from overall_decades
GROUP BY 
decade
ORDER BY 
decade

# Задание 19.

SELECT name, year, align, count(*) as char_count
FROM MarvelCharacters mc 
WHERE align IN ('Good Characters', 'Bad Characters') AND 
year between 1980 and 1989
GROUP BY align, year
ORDER BY align, year

# Задание 20.

SELECT hair, sum(appearances) as сумма
FROM MarvelCharacters mc 
GROUP BY hair
ORDER BY сумма Desc
LIMIT 3