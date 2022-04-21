-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Requirements;

-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (yu can assume user_id is linked to an existing users)
-- project_name, a new or already existing project - If no projecgs.name found in the table, you should create it
-- score, the value for the correction

DELIMITER || ;
CREATE PROCEDURE AddBonus(
    IN user_id INTEGER,
    IN project_name VARCHAR(255),
    IN score INTEGER
)
BEGIN
    IF NOT EXISTS(SELECT name FROM projects WHERE name=project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO correctiond (user_id, project_id, score)
    VALUES (user_id, (SELECT id from projects WHERE name=project_name), score);
END; ||
DELIMITER ;
