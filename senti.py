import pyprind
import pandas as pd
import os
basepath="C:/Users/Pradnya Borkar/Desktop/New folder/aclImdb"
labels={'pos':1,'neg':0}
pbar=pyprind.ProgBar(50000)
df=pd.DataFrame()
for s in ('test','train'):
	for l in ('pos','neg'):
		path=os.path.join(basepath,s,l)
		for file in os.listdir(path):
			with open(os.path.join(path, file),'r', encoding='utf-8') as infile:
				txt = infile.read()
			df = df.append([[txt, labels[l]]],ignore_index=True)
			pbar.update()
df.columns = ['review', 'sentiment']

import numpy as np
np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
df.to_csv('C:/Users/Pradnya Borkar/Desktop/New folder/aclImdb/movie_data.csv', index=False, encoding='utf-8')
df = pd.read_csv('C:/Users/Pradnya Borkar/Desktop/New folder/aclImdb/movie_data.csv', encoding='utf-8')
#print(df)
"""
output:
exec(open('C:/Users/Pradnya Borkar/Desktop/senti.py').read())
0% [##############################] 100% | ETA: 00:00:00
Total time elapsed: 00:03:44
                                              review  sentiment
0  In 1974, the teenager Martha Moxley (Maggie Gr...          1
1  OK... so... I really like Kris Kristofferson a...          0
2  ***SPOILER*** Do not read this, if you think a...          0
>>> exec(open('C:/Users/Pradnya Borkar/Desktop/senti.py').read())
0% [##############################] 100% | ETA: 00:00:00
Total time elapsed: 00:05:51
                                                  review  sentiment
0      In 1974, the teenager Martha Moxley (Maggie Gr...          1
1      OK... so... I really like Kris Kristofferson a...          0
2      ***SPOILER*** Do not read this, if you think a...          0
3      hi for all the people who have seen this wonde...          1
4      I recently bought the DVD, forgetting just how...          0
5      Leave it to Braik to put on a good show. Final...          1
6      Nathan Detroit (Frank Sinatra) is the manager ...          1
7      To understand "Crash Course" in the right cont...          1
8      I've been impressed with Chavez's stance again...          1
9      This movie is directed by Renny Harlin the fin...          1
10     I once lived in the u.p and let me tell you wh...          0
11     Hidden Frontier is notable for being the longe...          1
12     It's a while ago, that I have seen Sleuth (197...          0
13     What is it about the French? First, they (appa...          0
14     This very strange movie is unlike anything mad...          1
15     I saw this movie on the strength of the single...          0
16     There are some great philosophical questions. ...          0
17     I was cast as the Surfer Dude in the beach sce...          1
18     I had high hopes for this one until they chang...          0
19     Set in and near a poor working class town in t...          1
20     Opulent sets and sumptuous costumes well photo...          0
21     i saw the film and i got screwed, because the ...          0
22     I'm getting a little tired of people misusing ...          0
23     How offensive! Those who liked this movie have...          0
24     What else can you say about this movie,except ...          0
25     Certain aspects of Punishment Park are less th...          1
26     First of all, I'd like to tell you that I'm in...          0
27     You should not take what I am about to say lig...          1
28     I love the Jurassic Park movies, they are thre...          0
29     The first series of Lost kicked off with a ban...          1
...                                                  ...        ...
49970  Tom Fontana's unforgettable "Oz" is hands down...          1
49971  Last weekend I bought this 'zombie movie' from...          0
49972  I watched the first few moments on TCM a few y...          1
49973  I saw this movie for the first time in 1988 wh...          1
49974  Al Pacino? Kim Basinger? Tea Leoni? Ryan O'Nea...          0
49975  Stanwyck at her villainous best, Robinson her ...          1
49976  An allegation of aggravated sexual assault alo...          0
49977  i thought this movie was wonderfully plotted i...          1
49978  Just like most people, I couldn't wait to see ...          0
49979  Dark comedy? Gallows humor? How does one make ...          1
49980  ****Probably will contain spoilers****<br /><b...          0
49981  I must be that one guy in America that didn't ...          0
49982  THE PLOT: A trucker (Kristofferson) battles a ...          0
49983  The Ladies Man is laugh out loud funny, with a...          1
49984  Well, the artyfartyrati of Cannes may have lik...          0
49985  The director was probably still in his early l...          0
49986  You know when you're on the bus and someone de...          0
49987  Five minutes into this movie you realize that ...          0
49988  ...If you've been laughing too much for a long...          0
49989  I love dissing this movie. My peers always try...          0
49990  OK. I think the TV show is kind of cute and it...          0
49991  Big disappointment. CLASH BY NIGHT is much to ...          0
49992  Cassidy(Kacia Brady)puts a gun in her mouth bl...          0
49993  With rapid intercutting of scenes of insane pe...          1
49994  When "Girlfight" came out, the reviews praised...          1
49995  OK, lets start with the best. the building. al...          0
49996  The British 'heritage film' industry is out of...          0
49997  I don't even know where to begin on this one. ...          0
49998  Richard Tyler is a little boy who is scared of...          0
49999  I waited long to watch this movie. Also becaus...          1

[50000 rows x 2 columns]
"""
