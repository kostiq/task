SELECT u.id, count(u.id) FROM Users u
LEFT JOIN Messages m ON u.id = m.user_id 
GROUP BY u.id
ORDER BY count(u.id) DESC
LIMIT 10; 