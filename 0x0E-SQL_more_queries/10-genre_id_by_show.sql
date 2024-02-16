-- This is my comment
SELECT b.title, a.genre_id
FROM tv_show_genres AS a
JOIN tv_shows AS b
ON a.show_id = b.id;
