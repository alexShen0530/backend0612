CREATE DATABASE IF NOT EXISTS fastapi_test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE fastapi_test;
INSERT INTO `book` (`title`, `author`, `price`, `create_time`, `update_time`) VALUES
('The FastAPI Handbook', 'Alice Zhang', 39.9, '2026-06-17 10:00:00', '2026-06-17 10:00:00'),
('Python for Data Science', 'Bob Li', 49.5, '2026-06-17 10:05:00', '2026-06-17 10:05:00'),
('Deep Learning Basics', 'Charlie Wang', 59.0, '2026-06-17 10:10:00', '2026-06-17 10:10:00'),
('Mastering SQLAlchemy', 'David Chen', 45.0, '2026-06-17 10:15:00', '2026-06-17 10:15:00'),
('Async Python in Practice', 'Eva Liu', 52.5, '2026-06-17 10:20:00', '2026-06-17 10:20:00');
