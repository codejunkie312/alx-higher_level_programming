-- lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.
SELECT tv.title FROM tv_shows AS tv WHERE NOT EXISTS (
    SELECT 1 
    FROM tv_show_genres AS tsg 
    INNER JOIN tv_genres AS tg ON tsg.genre_id = tg.id 
    WHERE tg.name = 'Comedy' AND tsg.show_id = tv.id
)
ORDER BY tv.title ASC;
