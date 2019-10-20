categary_choice = input(" Enter your categary choice:")
if categary_choice == ("Fiction"):
    genre = input(" Enter your genre in fiction categary:")
    if (genre == "Comedy") or (genre == "comedy"):
        print(" Go to the section A.")
    elif (genre == "Comic novel") or (genre =="comic novel"):
        print(" Go to the section B.")
    elif (genre == "Science fiction") or (genre =="science fiction"):
        print(" Go to the section C.")  
    elif (genre == "Fantasy") or (genre =="fantasy"):
        print(" Go to the section D.")
    elif (genre == "Historical fiction") or (genre =="historical fiction"):
        print(" Go to the section E.")
elif categary_choice == ("Nonfiction"):
    genre = input (" Enter the genre you want to read in nonfiction categary:")
    if (genre == "History & Geography") or (genre ==" history & geography"):
        print(" Go to the section F.")
    elif (genre == "Arts") or (genre =="arts"):
        print(" Go to the section G.")
    elif (genre == "Science & Technology") or (genre =="science & technology"):
        print(" Go to the section H.")
    elif (genre == "Other") or (genre =="other"):
        print(" Go to the section I.")


