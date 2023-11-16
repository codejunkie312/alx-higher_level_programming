--  lists all Comedy shows in the database `hbtn_0d_tvshows`.
SELECT show.`title` FROM `tv_shows` AS show
INNER JOIN `tv_show_genres` AS tv ON show.`id` = tv.`show_id`
INNER JOIN `tv_genres` AS show_genre ON tv.`genre_id` = show_genre.`id` WHERE show_genre.`name` = "Comedy"
ORDER BY show.`title`;