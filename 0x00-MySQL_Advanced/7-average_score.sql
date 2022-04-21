-- SQL script thst creates a stored procedure ComputerAverageScoreForUser that computes and store the average score for a student. Note: An averagescore can be a decimal

-- Requirements:

-- Procedure ComputerAverageScoreForUser is taking 1 input:
-- user_id, a user.id value (you can assume that user_id is linked to an existing user)

DROP PROCEDURE IF EXISTS ComputerAverageScoreForUser:

DELIMITER //
CREATE PROCEDURE ComputerAverageScoreForUser (IN user_id INT)
BEGIN DECLARE avg_score FLOAT;

SET avg_score =  (
SELECT AVG(score)
FROM corrections AS Corr
WHERE Corr.user_id=user_id); UPDATE users

SET average_Score = avg_score
WHERE id=user_id;
END //
DELIMITER;