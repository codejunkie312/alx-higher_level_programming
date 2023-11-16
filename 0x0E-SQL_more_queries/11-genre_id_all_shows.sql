--  lists all shows contained in the database `hbtn_0d_tvshows`.
SELECT show.`title`, show_genre.`genre_id` FROM `tv_shows` AS show
LEFT JOIN `tv_show_genres` AS show_genre ON show.`id` = show_genre.`show_id`
ORDER BY show.`title`, show_genre.`genre_id`;