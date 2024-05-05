import pandas as pd
from txtai import Embeddings

# Read the text file into a list of lines
with open('/home/rajat/apps/jobtask/train_data.txt', 'r') as file:
    lines = file.readlines()

# Split each line into its components and create a DataFrame
data = [line.strip().split(' ::: ') for line in lines]
df = pd.DataFrame(data, columns=['Title', 'Year', 'Genre', 'Summary'])

# Display the DataFrame
print(df)

# We will see category of movie types we have from the dataset
movie_category = df['Genre'].unique()
#print(df['Genre'].nunique())
print(movie_category)
count = df['Genre'].value_counts()
print(count)

drama =[]
thriller=[]
adult=[]
documentary =[]
comedy =[]
crime =[]
reality_tv=[]
horror =[]
sport =[]
animation=[]
action=[]
fantasy =[]
short =[]
sci_fi=[]
music=[]
adventure =[]
talk_show =[]
western=[]
family=[]
mystery=[]
history =[]
news=[]
biography =[]
romance =[]
game_show=[]
musical=[]
war=[]


training_array = []
for index,row in df.iterrows():
    if row['Genre']=='drama':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        drama.append(object)

        del object
    elif row['Genre']=='thriller':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        thriller.append(object)

        del object
    elif row['Genre']=='adult':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        adult.append(object)

        del object
    elif row['Genre']=='documentary':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        documentary.append(object)

        del object
    elif row['Genre']=='comedy':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        comedy.append(object)

        del object
    elif row['Genre']=='crime':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        crime.append(object)

        del object
    elif row['Genre']=='reality-tv':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        reality_tv.append(object)

        del object
    elif row['Genre']=='horror':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        horror.append(object)

        del object
    elif row['Genre']=='sport':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        sport.append(object)

        del object
    elif row['Genre']=='animation':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        animation.append(object)

        del object
    elif row['Genre']=='action':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        action.append(object)

        del object
    elif row['Genre']=='fantasy':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        fantasy.append(object)

        del object
    elif row['Genre']=='short':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        short.append(object)

        del object
    elif row['Genre']=='sci-fi':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        sci_fi.append(object)

        del object
    elif row['Genre']=='music':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        music.append(object)

        del object
    elif row['Genre']=='adventure':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        adventure.append(object)

        del object
    elif row['Genre']=='talk-show':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        talk_show.append(object)

        del object
    elif row['Genre']=='western':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        western.append(object)

        del object
    elif row['Genre']=='family':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        family.append(object)

        del object

    elif row['Genre']=='mystery':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        mystery.append(object)

        del object
    elif row['Genre']=='history':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        history.append(object)

        del object
    elif row['Genre']=='news':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        news.append(object)

        del object
    elif row['Genre']=='biography':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        biography.append(object)

        del object
    elif row['Genre']=='romance':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        romance.append(object)

        del object
    elif row['Genre']=='game-show':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        game_show.append(object)

        del object
    elif row['Genre']=='musical':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        musical.append(object)

        del object
    elif row['Genre']=='war':
        object = f"The Genre is - " + str(row['Genre']) + f". Movie Name is " + str(row['Year']) + f". The Summary of the movie is ---- " +str(row['Summary'])
        war.append(object)

        del object


training_array.append(drama)
training_array.append(thriller)
training_array.append(adult)
training_array.append(documentary)
training_array.append(comedy)
training_array.append(crime)
training_array.append(reality_tv)
training_array.append(horror)
training_array.append(sport)
training_array.append(animation)
training_array.append(action)
training_array.append(fantasy)
training_array.append(short)
training_array.append(sci_fi)
training_array.append(music)
training_array.append(adventure)
training_array.append(talk_show)
training_array.append(western)
training_array.append(family)
training_array.append(mystery)
training_array.append(history)
training_array.append(news)
training_array.append(biography)
training_array.append(romance)
training_array.append(game_show)
training_array.append(musical)
training_array.append(war)



print(len(training_array[0]))
print(len(drama))
print(len(training_array))
for i in range(0,len(movie_category)):
    embeddings = Embeddings(hybrid=True, keyword=True, content=True)
    embeddings.index(training_array[i])
    embeddings.save(f'/home/rajat/apps/jobtask/moviemaster/{movie_category[i]}')




