-- Optimize search and score
-- Task 9

CREATE INDEX idx_name_first_score ON names (name(1), score);
