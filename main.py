
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd 
import csv
df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
#fig=ff.create_distplot([data],["mathScores"],show_hist=False)
#fig.show()
#mean=statistics.mean(data)
#standardDeviation=statistics.stdev(data)
#print(mean,standardDeviation)
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return(mean)
meanlist=[]    
for i in range(0,1000):
    setofmeans=randomsetofmeans(100)
    meanlist.append(setofmeans)    
standardDeviation=statistics.stdev(meanlist)
mean=statistics.mean(meanlist)
print(mean,standardDeviation)
fig=ff.create_distplot([meanlist],['studentMarks'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name='mean'))
fig.show()

fsds,fsde=mean-standardDeviation,mean+standardDeviation
ssds,ssde=mean-(2*standardDeviation),mean+(2*standardDeviation)
tsds,tsde=mean-(3*standardDeviation),mean+(3*standardDeviation)
print(fsds,fsde)
print(ssds,ssde)
print(tsds,tsde)

fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode='lines',name='sd1 start'))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode='lines',name='sd1 end'))

fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode='lines',name='sd2 start'))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='sd2end'))

fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode='lines',name='sd3start'))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode='lines',name='sd3 end'))

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()

meanOfSample1=statistics.mean(data)
print(meanOfSample1)

fig=ff.create_distplot([meanlist],["studentMarks"],show_hist=False)
fig.show()