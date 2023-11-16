-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv.title, tsg.genre_id FROM tv_shows AS tv
INNER JOIN tv_show_genres AS tsg ON tv.id = tsg.show_id
ORDER BY tv.title ASC, tsg.genre_id ASC;