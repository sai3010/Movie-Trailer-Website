import fresh_tomaotes
import movie

TMNT=movie.movie("TMNT","When the world is threatened by an ancient evil, the four adolescent turtles must reunite and overcome their faults in order to stand against it. ","https://upload.wikimedia.org/wikipedia/en/5/5b/TMNTposter.jpg","https://www.youtube.com/watch?v=HeaugHGd1Kw")

pixel=movie.movie("Pixels","When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games. ","https://upload.wikimedia.org/wikipedia/en/f/f0/PixelsOfficialPoster.jpg","https://www.youtube.com/watch?v=XAHprLW48no")

msd=movie.movie("MS Dhoni","M.S. Dhoni tells the little-known story of the cricket captain's journey from ticket collector to trophy collector.","https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg","https://www.youtube.com/watch?v=6L6XqWoS8tw")

focus=movie.movie("Focus","In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop. ","https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png","https://www.youtube.com/watch?v=MxCRgtdAuBo")


xmen=movie.movie("X-Men: Apocalypse ","After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan. ","https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg","https://www.youtube.com/watch?v=Jer8XjMrUB4")


movies = [TMNT,pixel,msd,focus,xmen]
fresh_tomaotes.open_movies_page(movies)
#print(movie.movie.__doc__)
#print(movie.movie.__name__)
#print(movie.movie.__module__)
