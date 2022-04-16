# Hand-Gesture-Recognition

# Blog Link-https://medium.com/analytics-vidhya/hand-gesture-recognition-for-deaf-mute-people-using-leap-motion-sensor-1d4fda415d76
# BUSINESS PROBLEM

Business problem is very simple,  Lets say i own a mcdonalds store or a Dominos store which stays too busy all the time, now one day a mute couple came to my store and tried to place orders but the staff at the counter did not understand their language and mind you, store is very busy, People are highly impatient when it comes to order their food.
My staff can't give too much time on one customer so he/she asked the mute couple to wait for a while.
Now for everyone around, it's not a big issue but for the couple it can be highly embarrassing. Being a store owner i don't want to give customers bad experience so i decided to think about this problem.
One Solution could be to train every staff member with sign language which could be very costly and impractical.
Another solution is add self ordering machines like ATM'S where anybody can come and simply place order via machine and grab their meal, this could be a good solution but I as an owner want to give those customers a special treatment.
Another solution is to add a Machine Learning System to the store which can understand the sign language and can translate sign language to ENGLISH/HINDI to the staff, this will give people a special treatment and also could be fun for other customers specially to the kids.

# CONSTRAINTS

1.Low Latency(In Real time within in few nano seconds the model should translate sign language to english language)
2.Errors can be more embarrassing for the mute/deaf people and that can affect the Brand Value.

# MACHINE LEARNING FORMULATION

This is a very simple Multi-Class classification problem where we have 26 classes (A to Z)
DATA
Data is manually produced by Leap Motion Sensor for every alphabet, Total 26000 rows has been taken from the Sensor and every five rows represent one instance of alphabet so we have 200 rows for every alphabet

# DATA
Data is manually produced by Leap Motion Sensor for every alphabet, Total 26000 rows has been taken from the Sensor and every five rows represent one instance of alphabet so we have 200 rows for every alphabet

# PERFORMANCE METRIC
Now here, it is a Multi-Class Classification problem, We want High Precision and High Recall so F1 score will be a good metric and we don't have any imbalance in the data so F1_weighted will work fine. Another metric can be multiclass logloss.

# DATA COLLECTION
LMC was connected to python to extract the values for training our model, to connect LMC with python we used LEAP.PY file given by LMC API. We imported Leap.py file from the folder provide by Leap. 
Code in leap.py shows the different libraries such as circle gestures,key tap gesture and swipe gestures were used. I have taken into consideration the finger names, bones in each finger and their start and end points.
In each frame the LMC gives us the value for each finger its position, it is distal bone co-ordinate, the palm width, palm positions and palm radius
