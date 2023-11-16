-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT show.`title`, show_genre.`genre_id` FROM `tv_shows` AS show
LEFT JOIN `tv_show_genres` AS show_genre ON show.`id` = show_genre.`show_id` WHERE show_genre.`genre_id` IS NULL
ORDER BY show.`title`, show_genre.`genre_id`;