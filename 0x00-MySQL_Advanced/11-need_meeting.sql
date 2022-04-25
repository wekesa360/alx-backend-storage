-- SQL script that creates a view need_meeting that lists all students that have a score under 88 (strict) and no last_meeting or more than 1 month.

-- Requirements:
-- THe view need_meeting should return all students name when:
-- They score under (Strict) to 80
-- AND no last_meeting date OR more than a month

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), interval - 1 MONTH));