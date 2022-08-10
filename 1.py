import numpy as np
import matplotlib.pyplot as plt

def prediction(theta_0, theta_1,x):
  return (theta_0,theta_1*x)

def prediction_difference(theta_0,theta_1,x,y):
  return (theta_0+theta_1*x)-y

def gradient_descent(theta_0,theta_1,x,y,iterations,alpha):
  m=len(x)
  cost_list=[]

  for i in range(iterations):
    error = prediction_difference(theta_0,theta_1,x,y)
    cost = (error*error) / (2*m)
    cost_list.append(cost)

    theta_0 = theta_0-alpha*error.mean()
    theta_1 = theta_1-alpha*(error*x).mean()

    if i % 10 == 0:
      plt.scatter(house_size,house_price)
      plt.plot(house_size,prediction(theta_0,theta_1,x),color = 'red')
      plt.show()

  return theta_0,theta_1,cost_list

#입력변수(집크기) 초기화 (데이터를 1/10크기로 줄임)
house_size = np.array([0.9,1.4,2,2.1,2.6,3.3,3.35,3.9,4.4,4.7,5.2,5.75,6.7,6.9])

#목표변수(집가격) 초기화 (데이터를 1/10크기로 줄임)
house_price = np.array([0.3,0.75,0.45,1.1,1.45,0.9,1.8,0.9,1.5,2.2,1.75,2.3,2.49,2.6])

#theta값 초기화 (아무 값이나 지정)

theta_0 = 2.5
theta_1 = 0

theta_0,theta_1,cost_list=gradient_descent(theta_0,theta_1,house_size,house_price,200,0.1)

theta_0,theta_1

plt.plot(cost_list)