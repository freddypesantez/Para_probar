import numpy as np


image_number = [21,15,17,18,48,17,19,28,44,40, 100]

x = y = z = np.arange(0.0,5.0,1.0)
#np.savetxt('test.out', x, delimiter=',')   # X is an array
#np.savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays
#np.savetxt('test.out', xc)   # use exponential notation

X1 = np.loadtxt('galery_0.out')
X2 = np.loadtxt('galery_1.out')
X3 = np.loadtxt('galery_2.out')
X4 = np.loadtxt('galery_3.out')
X5 = np.loadtxt('galery_4.out')
X6 = np.loadtxt('galery_5.out')
X7 = np.loadtxt('galery_6.out')
X8 = np.loadtxt('galery_7.out')
X9 = np.loadtxt('galery_8.out')
X10 = np.loadtxt('galery_9.out')
X11 = np.loadtxt('galery_10.out')


####################################
image_test = X9[9,3:515]
####################################



def dist_L2(vector1, vector2):
        distancia = np.sqrt(np.sum((vector1 - vector2)**2))
        return distancia

distance_vector = np.zeros((367,4))

for i in range (21):
    distance_vector[i,0] = X1[i,0]
    distance_vector[i,1] = X1[i,1]
    distance_vector[i,2] = X1[i,2]
    distance_vector[i,3] = dist_L2(image_test,X1[i,3:515])

for i in range (15):
    distance_vector[i+21,0] = X2[i,0]
    distance_vector[i+21,1] = X2[i,1]
    distance_vector[i+21,2] = X2[i,2]
    distance_vector[i+21,3] = dist_L2(image_test,X2[i,3:515])

for i in range (17):
    distance_vector[i+21+15,0] = X3[i,0]
    distance_vector[i+21+15,1] = X3[i,1]
    distance_vector[i+21+15,2] = X3[i,2]
    distance_vector[i+21+15,3] = dist_L2(image_test,X3[i,3:515])

for i in range (18):
    distance_vector[i+21+15+17,0] = X4[i,0]
    distance_vector[i+21+15+17,1] = X4[i,1]
    distance_vector[i+21+15+17,2] = X4[i,2]
    distance_vector[i+21+15+17,3] = dist_L2(image_test,X4[i,3:515])

for i in range (48):
    distance_vector[i+21+15+17+18,0] = X5[i,0]
    distance_vector[i+21+15+17+18,1] = X5[i,1]
    distance_vector[i+21+15+17+18,2] = X5[i,2]
    distance_vector[i+21+15+17+18,3] = dist_L2(image_test,X5[i,3:515])

for i in range (17):
    distance_vector[i+21+15+17+18+48,0] = X6[i,0]
    distance_vector[i+21+15+17+18+48,1] = X6[i,1]
    distance_vector[i+21+15+17+18+48,2] = X6[i,2]
    distance_vector[i+21+15+17+18+48,3] = dist_L2(image_test,X6[i,3:515])

for i in range (19):
    distance_vector[i+21+15+17+18+48+17,0] = X7[i,0]
    distance_vector[i+21+15+17+18+48+17,1] = X7[i,1]
    distance_vector[i+21+15+17+18+48+17,2] = X7[i,2]
    distance_vector[i+21+15+17+18+48+17,3] = dist_L2(image_test,X7[i,3:515])

for i in range (28):
    distance_vector[i+21+15+17+18+48+17+19,0] = X8[i,0]
    distance_vector[i+21+15+17+18+48+17+19,1] = X8[i,1]
    distance_vector[i+21+15+17+18+48+17+19,2] = X8[i,2]
    distance_vector[i+21+15+17+18+48+17+19,3] = dist_L2(image_test,X8[i,3:515])

for i in range (44):
    distance_vector[i+21+15+17+18+48+17+19+28,0] = X9[i,0]
    distance_vector[i+21+15+17+18+48+17+19+28,1] = X9[i,1]
    distance_vector[i+21+15+17+18+48+17+19+28,2] = X9[i,2]
    distance_vector[i+21+15+17+18+48+17+19+28,3] = dist_L2(image_test,X9[i,3:515])

for i in range (40):
    distance_vector[i+21+15+17+18+48+17+19+28+44,0] = X10[i,0]
    distance_vector[i+21+15+17+18+48+17+19+28+44,1] = X10[i,1]
    distance_vector[i+21+15+17+18+48+17+19+28+44,2] = X10[i,2]
    distance_vector[i+21+15+17+18+48+17+19+28+44,3] = dist_L2(image_test,X10[i,3:515])

for i in range (100):
    distance_vector[i+21+15+17+18+48+17+19+28+44+40,0] = X11[i,0]
    distance_vector[i+21+15+17+18+48+17+19+28+44+40,1] = X11[i,1]
    distance_vector[i+21+15+17+18+48+17+19+28+44+40,2] = X11[i,2]
    distance_vector[i+21+15+17+18+48+17+19+28+44+40,3] = dist_L2(image_test,X11[i,3:515])
        
#index = np.zeros(367)
#similarity = np.zeros(367)

index = []
similarity = []

for k in range (367):
    j = np.argmin(distance_vector[:,3])
    if distance_vector[j,3] < 50:
        index.append(distance_vector[j,0])
        similarity.append(distance_vector[j,3])
#        index[k] = distance_vector[j,0]
#        similarity[k] = distance_vector[j,3]
    distance_vector= np.delete(distance_vector,j,axis=0)

index = index[1:367]
similarity = similarity[1:367]




print(index)
print(similarity)
    
