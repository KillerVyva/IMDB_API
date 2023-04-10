import requests
from tkinter import *
from tkinter import scrolledtext

# Constant variables
URL = "https://ott-details.p.rapidapi.com/advancedsearch"
GENRE = ['Action', 'Drama', 'Comedy', 'Romance', 'Adventure', 'Western', 'Animation', 'Crime', 'Documentary', 'Horror', 'Sci-Fi', 'Thriller', 'Biography']
IMDB = [1, 2, 3, 4, 5, 6, 7, 8, 9]
TYPE = ['Movie', 'Show']
SORT = ['latest', 'highestrated' , 'lowestrated']


# Return params from 'window' Movie Parser
def queryString():
        return {
                "start_year":spin_box_from.get(),
                "end_year":spin_box_to.get(),
                "min_imdb":rating_var.get(),
                "max_imdb":"9.9",
                "genre":genre_var.get(),
                "type":"movie",
                "language":"english",
                "sort":sort_var.get(),
                "page":"1"
                }

 
def movieRequest():
        headers = {
        	"X-RapidAPI-Key": "41e061974dmsh18bf5ae977b7e56p175278jsndc3acf21ed26",
        	"X-RapidAPI-Host": "ott-details.p.rapidapi.com"
        }

        response = requests.request("GET", URL, headers=headers, params=queryString())
        
        # Data from RapidAPI
        data = response.json()
        
        if data is not None:
                window = Tk()
                window.title("JSON Viewer")

                # Create a scrolled text widget
                text_widget = scrolledtext.ScrolledText(window, wrap=WORD)
                text_widget.pack(expand=YES, fill=BOTH)

                # Insert JSON data into the text widget
                for movie in data['results']:
                    text_widget.insert(END, f"Title: {movie['title']}\n"
                                            f"Released: {movie['released']}\n"
                                            f"Genre: {' '.join(movie['genre'])}\n"
                                            f"IMDB: {movie['imdbrating']}\n\n")

                # Disable text editing
                text_widget.configure(state='disabled')

                # Create a label for displaying a message
                label = Label(window, text="JSON Data:")
                label.pack()

                # Create a text widget for displaying JSON values
                text_widget = Text(window, wrap=WORD, height=10)
                text_widget.pack(expand=YES, fill=BOTH)

                # Insert JSON values into the text widget
                for key, value in data.items():
                    text_widget.insert(END, f"{key}: {value}\n")

                # Disable text editing
                text_widget.configure(state='disabled')


# Create main window
window = Tk()
window.title('Movie parser')
window.config(padx=70, pady=70)

canvas = Canvas(height=250, width=250) # Area for logo
logo_img = PhotoImage(file='logo_0.png')
canvas.create_image(125, 90, image=logo_img) # Logo position
canvas.grid(row=0, column=0, columnspan=3)

rating_txt = Label(text='IMDB(from):') # txt IMDB
rating_txt.grid(row=1, column=0) # Grid position
rating_var = StringVar(window)
rating_var.set(IMDB[0]) # Set start value
rating_select = OptionMenu(window, rating_var, *IMDB) # Option manu with IMDB list values
rating_select.grid(row=1, column=1, columnspan=2) # Grid position

genre_text = Label(text='Genre:')
genre_text.grid(row=2, column=0)
genre_var = StringVar(window)
genre_var.set(GENRE[0])
genre_select = OptionMenu(window, genre_var, *GENRE)
genre_select.grid(row=2, column=1, columnspan=2)

sort_txt = Label(text='Sort:')
sort_txt.grid(row=3, column=0)
sort_var = StringVar(window)
sort_var.set(SORT[0])
sort_select = OptionMenu(window, sort_var, *SORT)
sort_select.grid(row=3, column=1, columnspan=2)

# The year FROM which you start looking for movies
start_value1 = StringVar(value=2017)
date_select1 = Label(text='Date(from):')
date_select1.grid(row=4, column=0)
spin_box_from = Spinbox(window, from_=1990, to=2023, increment=1, textvariable=start_value1)
spin_box_from.grid(row=4, column=1, columnspan=2)

# The year TO which we are looking for movies
start_value2 = StringVar(value=2023)
date_select2 = Label(text='Date(to):')
date_select2.grid(row=5, column=0)
spin_box_to = Spinbox(window, from_=1990, to=2023, increment=1, textvariable=start_value2)
spin_box_to.grid(row=5, column=1, columnspan=2)

searchButt = Button(window, text='Search', width=30, activebackground='green', activeforeground='blue',
                    command=movieRequest)
searchButt.grid(row=6, column=0, columnspan=3)


# Turn of window resizing
window.resizable(False, False)
# Infinite look which runs forever until the user exits the window
window.mainloop()

