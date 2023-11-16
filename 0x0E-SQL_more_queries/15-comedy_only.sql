--  lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv.title FROM tv_shows AS tv
JOIN tv_show_genres AS tsg ON tv.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY tv.title ASC;