-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.name FROM tv_shows AS tv
JOIN tv_show_genres AS tsg ON tv.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tv.title = 'Dexter'
ORDER BY tg.name ASC;