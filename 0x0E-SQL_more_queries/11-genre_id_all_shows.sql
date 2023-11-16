--  lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv.title, tsg.genre_id FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tsg ON tv.id = tsg.show_id
ORDER BY tv.title ASC, tsg.genre_id ASC;