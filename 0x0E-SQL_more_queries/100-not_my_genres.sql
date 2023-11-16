-- uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`
SELECT tg.name FROM tv_genres AS tg WHERE tg.id NOT IN (
    SELECT tsg.genre_id 
    FROM tv_show_genres AS tsg
    INNER JOIN tv_shows AS tv ON tsg.show_id = tv.id
    WHERE tv.title = 'Dexter'
)
ORDER BY tg.name ASC;