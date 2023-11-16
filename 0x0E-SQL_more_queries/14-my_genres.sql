-- uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
SELECT show_genre.`name` FROM `tv_genres` AS show_genre
INNER JOIN `tv_show_genres` AS tv ON show_genre.`id` = tv.`genre_id`
INNER JOIN `tv_shows` AS show ON tv.`show_id` = show.`id` WHERE show.`title` = "Dexter"
ORDER BY show_genre.`name`;