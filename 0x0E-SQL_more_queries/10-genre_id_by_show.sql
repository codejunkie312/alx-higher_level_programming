-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT show.`title`, show_genre.`genre_id` FROM `tv_shows` AS show
INNER JOIN `tv_show_genres` AS show_genre ON show_genre.`show_id` = show.`id`
ORDER BY show.`title`, show_genre.`genre_id`;