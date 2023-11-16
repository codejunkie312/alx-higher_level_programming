-- lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.
SELECT DISTINCT `title` FROM `tv_shows` AS show
LEFT JOIN `tv_show_genres` AS tv ON show.`id` = tv.`show_id`
LEFT JOIN `tv_genres` AS show_genre ON tv.`genre_id` = show_genre.`id`
WHERE show.`title` NOT IN (
    SELECT show.`title` FROM `tv_shows` AS show
    INNER JOIN `tv_show_genres` AS tv ON show.`id` = tv.`show_id`
    INNER JOIN `tv_genres` AS show_genre ON tv.`genre_id` = show_genre.`id` WHERE show_genre.`name` = "Comedy"
)
ORDER BY show.`title`;