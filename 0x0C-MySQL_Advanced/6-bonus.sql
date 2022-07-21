-- Add bonus
-- Task 6

DELIMETER $$
CREATE PROCEDURE AddBonus(
IN user_id INT, project_name varchar(255), score INT
)
BEGIN
UPDATE corrections SET NEW.user_id = user_id, NEW.score = score
END;
$$
