import numpy as np
import random

class GA:
    def __init__(self, param1, param2,pop,eva,cr,mt):
        # Instance-level attributes
        self.lower_bound = param1
        self.upper_bound = param2
        self.pop= pop
        self.maxeva=eva
        self.eva=0
        self.dim= len(param1)
        self.acc= np.empty((self.pop,))
        self.cr=cr #crossover
        self.mt=mt #mutation
        self.chromo = np.empty(shape=(self.pop, self.dim))
        self.global_chromo=np.empty((self.dim,))
        self.global_acc=0.00
    def initial(self):
        random_seed = random.randint(0, 1000)
        random.seed(random_seed)

        for i in range(len(self.chromo)):
            for j in range(len(self.chromo[i])):
            #    self.chromo[i][j]=random.uniform(self.lower_bound[j], self.upper_bound[j])
               self.chromo[i][j]=random.randint(self.lower_bound[j], self.upper_bound[j])
        
    def transition(self):
        temp=self.choose()
        self.crossover(temp)
        self.mutation()
    def choose(self):
        temp=self.chromo
        for i in range(len(temp)):
            a = random.randint(0,len(self.chromo)-1)
            while True:
                b = random.randint(0,len(self.chromo)-1)

                if b!=a:
                    break
            if self.acc[a] > self.acc[b]:
                temp[i]=self.chromo[a]
            else : 
                temp[i]=self.chromo[b]

        return temp
    def crossover(self,chro_temp):

        split_point=random.randint(0,len(chro_temp[0])-1)
        for i in range(1,len(chro_temp),2):
            for j in range(len(chro_temp[i])):
                if (j < split_point):
                    self.chromo[i - 1][j] = chro_temp[i - 1][j]
                    self.chromo[i][j] = chro_temp[i][j]
                else:
                    if random.uniform(0.0,1.0) < self.cr:
                        self.chromo[i - 1][j] = chro_temp[i][j]
                    else:
                        self.chromo[i - 1][j] = chro_temp[i - 1][j]
                    if random.uniform(0.0,1.0) < self.cr:
                        self.chromo[i][j] = chro_temp[i - 1][j]
                    else:
                        self.chromo[i][j] = chro_temp[i][j]
    def mutation(self):
        for  i in range(self.pop):
            if random.uniform(0.0,1.0) < self.mt:
                M_point = random.randint(0, self.dim - 1)
                # self.chromo[i][M_point]=random.uniform(self.lower_bound[M_point],self.upper_bound[M_point])
                if self.chromo[i][M_point]==0:
                    self.chromo[i][M_point]=1
                else: 
                    self.chromo[i][M_point]=0
    def evaluation(self,acc_arr):
        self.acc=acc_arr
        if(np.max(acc_arr)>self.global_acc):
            self.global_acc=np.max(acc_arr)
            self.global_chromo=self.chromo[acc_arr.argmax()]
        self.chromo[acc_arr.argmin()]=self.global_chromo