import fresh_tomatoes
import media


#favorite movies with name, description, poster thumbnail, trailer
akira = media.Movie("Akira",
                        "A dystopian tale of post-WW3 Tokyo",
                        "https://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",
                        "https://youtu.be/-UhLderbuGI?t=6s")


trainspotting = media.Movie("Trainspotting",
                        "A harrowing tale of heroin addiction in scotland",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Trainspotting_ver2.jpg",
                        "https://youtu.be/8LuxOYIpu-I?t=3s")


the_matrix = media.Movie("The Matrix",
                        "A computer programmer discovers the true nature of reality",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://youtu.be/m8e-FF8MsqU")


moonlight = media.Movie("Moonlight",
                        "A poetic portrayal of the struggles of a "
                        "gay black man growing up",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",
                        "https://youtu.be/9NJj12tJzqc?t=7s")

princess_mononoke = media.Movie("Princess Mononoke",
                        "A beautiful story about the relationship "
                        "between humans and nature",
                        "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                        "https://www.youtube.com/watch?v=4OiMOHRDs14")


elf = media.Movie("Moonlight",
                        "Will Ferrell brings you the funniest "
                          "christmas movie of all time",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg",
                        "https://www.youtube.com/watch?v=pHTVCq6TDBs")

#calling function to run favorite movies
movies = [akira, trainspotting, the_matrix, moonlight, princess_mononoke, elf]
fresh_tomatoes.open_movies_page(movies)
