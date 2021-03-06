import numpy as np
objects = np.zeros((9,7)) # Planet, m,x,y,z,vx,vy,vz
#                       m                  x                        y                     z                     vx                    vy                       vz
objects[8] = np.array([1.0, -6.151489682016204E-03, 6.389988001518661E-03, 9.024482263224161E-05, -7.240886699697975E-06, -5.140115343860045E-06, 2.177046161642180E-07])
objects[7] = np.array([0.16601E-6, 3.269770816268355E-01, 7.809178409376630E-02, -2.460897254319929E-02, -1.137000888603457E-02, 2.875571677398091E-02, 3.392751290933102E-03])
objects[6] = np.array([2.4478383E-6, -3.335486637448234E-01, 6.454434722443811E-01, 2.775278968391979E-02, -1.807712391477036E-02, -9.341060307773352E-03, 9.148436818834693E-04])
objects[5] = np.array([3.04043263333E-6, 8.662512860873756E-01, 4.853172733593905E-01, 6.618573183122125E-05, -8.573558369935692E-03, 1.501090461194540E-02, 1.709280843053768E-07])
objects[4] = np.array([0.3227151E-6, 1.277801509986894E+00, 6.219298955269206E-01, -1.850763760330068E-02, -5.521569626484812E-03, 1.380800966185351E-02, 4.249657913810713E-04])
objects[3] = np.array([954.79194E-6, 2.595206719350237E+00, -4.403633991000436E+00, -3.979430059966980E-02, 6.407058239769715E-03, 4.189796152277494E-03, -1.607311949409247E-04])
objects[2] = np.array([285.8860E-6, 5.170830605761387E+00, -8.546507831937094E+00, -5.725413050971900E-02, 4.462364872259313E-03, 2.872932205004343E-03, -2.273110775246567E-04])
objects[1] = np.array([43.66244E-6, 1.552005035098798E+01, 1.226269617318254E+01, -1.555201582502495E-01, -2.467166527088185E-03, 2.902793440293295E-03, 4.286845589566771E-05])
objects[0] = np.array([51.51389E-6, 2.941559499633378E+01, -5.446448015811582E+00, -5.657536266829797E-01, 5.502446300361581E-04, 3.105160598911674E-03, -7.641310503762381E-05])
# Dette er over brøkstreken (verdier legges til disse):
numerator_x = 0
numerator_y = 0
numerator_z = 0
Total_mass = 0 # Den totale massen legges til her.
for i in range(9): # Løper gjennom alle objektene:
    objects[i][4] = objects[i][4]*365 # Gjør om til AU per år.
    objects[i][5] = objects[i][5]*365
    objects[i][6] = objects[i][6]*365
    numerator_x += objects[i][4] * objects[i][0]
    numerator_x += objects[i][5] * objects[i][0]
    numerator_x += objects[i][6] * objects[i][0]
    Total_mass += objects[i][0]
v_mc_x = numerator_x / Total_mass # Regner ut hastigheten til massesenteret.
v_mc_y = numerator_y / Total_mass
v_mc_z = numerator_z / Total_mass
for i in range(9): # Her trekker vi fra hastigheten til massesenteret for alle hastighetene:
    objects[i][4] = objects[i][4]-v_mc_x
    objects[i][5] = objects[i][5]-v_mc_y
    objects[i][6] = objects[i][6]-v_mc_z
np.savetxt("Textfiles/Initial.txt", objects, fmt="%s") # Skriver til fil.
