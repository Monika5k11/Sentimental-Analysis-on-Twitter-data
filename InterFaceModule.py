#User Inter Face module
import tkinter as tk
import TweetProcessModule as tpm
import TwitterAPIInitializerModule as tim

def startProcess():
    api = tim.TwitterClient()
    pro = tpm.TweetHandler()
    tweets = pro.get_tweets(api,query =keyword.get() , count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    ptweetsc = str(int(100*len(ptweets)/len(tweets)))
    ntweetsc = str(int(100*len(ntweets)/len(tweets)))
    neutweetc = str(int(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    posLabel = tk.Label(window,text ="Positive Tweet Percentage: "+ptweetsc,bg='#20bce3',fg="green",font="Bahnschrift 20")
    posLabel.pack()
    negLabel = tk.Label(window,text ="Negative Tweet Percentage: "+ntweetsc,bg='#20bce3',fg="red",font="Bahnschrift 20")
    negLabel.pack()
    neuLabel = tk.Label(window,text ="Neutral Tweet Percentage: "+neutweetc,bg='#20bce3',fg="yellow",font="Bahnschrift 20")
    neuLabel.pack()
    ptwt="\t\t\t------POSITIVE TWEETS------\t\t\t\n"
    ntwt="\t\t\t------NEGATIVE TWEETS------\t\t\t\n"
    for tweet in ptweets[:10]:
        ptwt = ptwt + tweet['text'] + "\n\n"
    for tweet in ntweets[:10]:
        ntwt = ntwt + tweet['text'] +"\n\n"
    Output = tk.Text(window,bg="blue",fg="white")
    Output.pack()
    Output.insert(tk.END,(ptwt+ntwt).encode('latin-1','ignore'))
    
        
    
window = tk.Tk(className='Tweezer')
window.geometry("900x730")
window.resizable(width=False, height=False)
bgimage = tk.PhotoImage(file='twitter.png')
bgl = tk.Label(window, image=bgimage)
bgl.place(x=0, y=0, relwidth=1, relheight=1)
heading = tk.Label(window,text="Tweezer",bg='#20bce3',fg="White",font="Bahnschrift 36")
heading.pack()
label1 = tk.Label(window,text="Enter a keyword",bg='#20bce3',fg="White",font="Bahnschrift 16")
label1.pack()
keyword = tk.StringVar()
KeyInput = tk.Entry(window,width=100,font="Bahnschrift 15",textvariable=keyword)
KeyInput.pack()
get = tk.Button(window,text="Fetch",font="Bahnschrift 20",fg="#20bce3",bg="white",command=startProcess)
get.pack()
window.mainloop()

      
