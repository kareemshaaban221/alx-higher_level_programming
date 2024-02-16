-- This is my comment
SELECT a.title, b.genre_id
FROM tv_shows AS a
JOIN tv_show_genres AS b
ON b.show_id = a.id
ORDER BY a.title ASC, b.genre_id ASC;
