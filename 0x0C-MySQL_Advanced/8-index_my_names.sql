-- Optimize simple search
-- Task 8

CREATE INDEX idx_name_first ON names (name(1));
