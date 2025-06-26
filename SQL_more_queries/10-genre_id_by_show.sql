--  lists all shows contained in hbtn_0d_tvshows


SELECT tv_show.title, tv_show_genre.genre_id
FROM tv_shows
JOIN tv_show_genre ON tv_shows.id = tv_show_genre.tv_show_id
ORDER BY tv_show.title, tv_show_genre.genre_id;