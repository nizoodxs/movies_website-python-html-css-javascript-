import fresh_tomatoes
import movie

#put movies details as [movie_name] = movie.Movie([title],[story],[url of trailer],[link for poster from internet)
thor = movie.Movie("Thor:Ranarok","God of thunder","https://www.youtube.com/watch?v=ue80QwXMRHg","https://pics.filmaffinity.com/thor_ragnarok-115636540-large.jpg")
justice_league = movie.Movie("Justice League","Team of best superheroes","https://www.youtube.com/watch?v=CXXE0ueU7yE","https://cdn.empireonline.com/jpg/70/0/0/1280/960/aspectfit/0/0/0/0/0/0/c/articles/59e7c4f974a68c0707aa82cb/justice-league-poster.jpg")
spiderman = movie.Movie("Spiderman: Homecoming","Peter Parker strugles to be best of both of his alter egoes","https://www.youtube.com/watch?v=U0D3AOldjMU","https://i.ytimg.com/vi/K7BjsUvSl7c/maxresdefault.jpg")
starwars = movie.Movie("The Rouge One","A good star wars story","https://www.youtube.com/watch?v=frdj1zb9sMY","https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png")
doctor_strange = movie.Movie("Doctor Strange","Awesome  marvel movie","https://www.youtube.com/watch?v=HSzx-zryEgM","https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg")
ant_man = movie.Movie("Ant Man","Funny superhero","https://www.youtube.com/watch?v=pWdKf3MneyI","https://vignette.wikia.nocookie.net/disney/images/1/1d/Ant-Man_Poster_Cropped.png/revision/latest?cb=20150514223736")



#movie array
movies = [thor,justice_league,spiderman,starwars,doctor_strange,ant_man]

#method call to method in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
