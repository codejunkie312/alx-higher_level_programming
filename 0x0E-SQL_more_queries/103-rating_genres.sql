-- lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.
SELECT show_genre.`name`, SUM(`rate`) AS `rating` FROM `tv_genres` AS show_genre
INNER JOIN `tv_show_genres` AS tv ON show_genre.`id` = tv.`genre_id`
INNER JOIN `tv_show_ratings` AS tv_rate ON tv.`show_id` = tv_rate.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;