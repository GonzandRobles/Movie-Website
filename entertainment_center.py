# -*- coding: utf-8 -*-

import fresh_tomatoes
import media


pi = media.Movie("Director: Darren Aranofsky",
                 "Script: Darren Aranofsky",
                 "Pi",
                 "Plot: A paranoid mathematician searches for a key number that will unlock the universal patterns found in nature.",
                 "https://www.movieposter.com/posters/archive/main/68/MPW-34133",
                 "https://www.youtube.com/watch?v=jo18VIoR2xU")

requiem_for_a_dream = media.Movie("Director: Darren Aranofsky",
                                  "Script: Hubert Selby Jr.",
                                  "Requiem for a Dream",
                                  "Plot: The drug-induced utopias of four Coney Island people are shattered when their addictions become stronger.",
                                  "http://images.moviepostershop.com/requiem-for-a-dream-movie-poster-2000-1020308633.jpg",
                                  "https://www.youtube.com/watch?v=0nU7dC9bIDg")

cronos = media.Movie ("Director: Guillermo del Toro",
                      "Script: Guillermo del Toro",
                      "Cronos",
                      "Plot: A mysterious device designed to provide its owner with eternal life resurfaces after four hundred years, leaving a trail of destruction in its path.",
                      "https://horrorpediadotcom.files.wordpress.com/2013/02/cronos-del-toro.jpg",
                      "hhttps://www.youtube.com/watch?v=tpqZnXGLilM")

deep_crimson = media.Movie ("Director: Arturo Ripstein",
                            "Script: Paz Alicia Garciadiego",
                            "Profundo Carmesi",
                            "Plot: The life of a man who preys on unsuspecting women for a living is changed when he finds an accomplice in the woman who loves and controls him.",
                            "https://palomitasconchoco.files.wordpress.com/2012/04/kinopoisk_ru-profundo-carmes_26_23237_3b-519875.jpg",
                            "https://www.youtube.com/watch?v=h9-SqFDT010")

memento = media.Movie ("Director: Christopher Nolan",
                       "Script: Jonathan Nolan",
                       "Memento",
                       "Plot: A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle.",
                       "http://pre07.deviantart.net/4c62/th/pre/f/2012/022/b/1/memento_poster_by_pooner-d4nc6qs.jpg",
                       "https://www.youtube.com/watch?v=UFuFFdK7i44")

city_of_god = media.Movie ("Director: Fernando Meirelles",
                           "Script: Braulio Mantovani",
                           "Cidade de Deus",
                           "Plot: Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
                           "http://www.cinematex.ro/posters/0/movie186.jpg",
                           "https://www.youtube.com/watch?v=nVliCPEaWq0")

movies = [pi, requiem_for_a_dream, cronos, deep_crimson, memento, city_of_god]
fresh_tomatoes.open_movies_page(movies)

print (pi.director, pi.screenwriter, pi.title, pi.storyline)
print (requiem_for_a_dream.director, requiem_for_a_dream.screenwriter, requiem_for_a_dream.title, requiem_for_a_dream.storyline)
print (cronos.director, cronos.screenwriter, cronos.title, cronos.storyline)
print (deep_crimson.director, deep_crimson.screenwriter, deep_crimson.title, deep_crimson.storyline)
print (memento.director, memento.screenwriter, memento.title, memento.storyline)
print (city_of_god.director, city_of_god.screenwriter, city_of_god.title, city_of_god.storyline)



