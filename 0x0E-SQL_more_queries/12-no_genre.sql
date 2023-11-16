-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv.title, tsg.genre_id FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tsg ON tv.id = tsg.show_id WHERE tsg.genre_id IS NULL
ORDER BY tv.title ASC, tsg.genre_id ASC;
