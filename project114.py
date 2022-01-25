import pandas as p
import plotly.express as pe
import numpy as nm

data = p.read_csv("project114TOEFLScore.csv")

toeflScore = data["TOEFL Score"].tolist()
chancesOfAdmission = data["Chance of Admit "].tolist()

Plot = pe.scatter(x=toeflScore,y=chancesOfAdmission)
Plot.show()

#----------------------------------- Finding out m , c using hit and trial method
#let's take m=1 , c = 0
m = 1
c = 0
y = []

for x in toeflScore:
    yValue = m*x + c
    y.append(yValue)

Plot = pe.scatter(x=toeflScore,y=chancesOfAdmission) 
Plot.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(toeflScore),x1 = max(toeflScore),
        y0 = min(y) , y1 = max(y)
    )
]) 

Plot.show()

#----------------------------------------------------------------------------------------

#let's take m=0.018 , c = -1.27
m = 0.018
c = -1.27
y = []

for x in toeflScore:
    yValue = m*x + c
    y.append(yValue)

Plot = pe.scatter(x=toeflScore,y=chancesOfAdmission) 
Plot.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(toeflScore),x1 = max(toeflScore),
        y0 = min(y) , y1 = max(y)
    )
]) 

Plot.show()

x = 520
y = m*x + c 

print("Chances of admission if the TOEFL score  is (using hit and trial func) --> ", y)


#------------------------------------- finding m , c using numpy --------------------------------

toeflList = nm.array(toeflScore)

chancesOfAdmissionList = nm.array(chancesOfAdmission)

m , c = nm.polyfit(toeflList,chancesOfAdmissionList,1)

y = []

for x in toeflList:
    yValue = m*x + c
    y.append(yValue)

Plot = pe.scatter(x=toeflList,y=chancesOfAdmissionList) 
Plot.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(toeflList),x1 = max(toeflList),
        y0 = min(y) , y1 = max(y)
    )
]) 

Plot.show()


x = 520
y = m*x + c 

print("Chances of admission if the TOEFL score  is (using numy func) --> ", y)
