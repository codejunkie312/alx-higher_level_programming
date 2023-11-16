-- lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
SELECT show_genre.`name` AS `genre`, COUNT(*) AS `number_of_shows` FROM `tv_genres` AS show_genre
INNER JOIN tv_show_genres AS tv ON show_genre.`id` = tv.`genre_id`
GROUP BY show_genre.`name`
ORDER BY `number_of_shows` DESC;