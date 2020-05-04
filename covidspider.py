import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file=pd.read_csv("covidcasesinindia.csv")
labels=file['states']

red=file['red zone']
orange=file['orange zone']
green=file['green zone']

x=np.arange(0,len(labels)*2,2)
width=0.35
fig,ax=plt.subplots()

rect1=ax.bar(x, red,width,color=['red'],label='red')
rect3=ax.bar(x+width,orange,width,color=['orange'],label='light orange')
rect2=ax.bar(x+width+width,green,width,color=['green'],label='green')

ax.set_ylabel('no. of zones')
ax.set_xlabel('states of india')
ax.set_title('Green and red zones of states of india')
ax.set_xticks((x+(width*0.5)))
ax.set_xticklabels(labels,rotation=90)
fig.tight_layout()
plt.show()
