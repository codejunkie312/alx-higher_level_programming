-- lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
SELECT show.`title`, show_genre.`name` FROM `tv_shows` AS show
LEFT JOIN `tv_show_genres` AS tv ON show.`id` = tv.`show_id`
LEFT JOIN `tv_genres` AS show_genre ON tv.`genre_id` = show_genre.`id`
ORDER BY show.`title`, show_genre.`name`;