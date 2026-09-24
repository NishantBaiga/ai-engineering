import matplotlib.pyplot as plt

# ### First Plot 
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("My First Plot")

# plt.show()




# ### Figures and Axes
# fig , ax = plt.subplots()

# ax.plot([1,2,3],[10,20,80])
# ax.set_title("Example")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")

# plt.show()




# ###line plots
# # make sure  x and y number of elements must be same 
# x=[1,2,3,4,5,6] 
# y=[10,15,13,20,25,30]

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title("sales over time")
# ax.set_xlabel("Days")
# ax.set_ylabel("Sales")

# plt.show()




# ### Multiple Lines and Legends

# epochs = [1,2,3,4,5]
# train_loss =[1.2, .9, .7, .5, .4]
# val_loss = [1.3, 1.0, .8, .7, .75]

# fig, ax = plt.subplots()

# ax.plot(epochs,train_loss, label="Training")
# ax.plot(epochs, val_loss, label="validation")

# ax.set_xlabel("Epoch")
# ax.set_ylabel("Loss")
# ax.grid(True)
# ax.legend()

# plt.show()




# ### Bar Chart
# categories = ["Python", "Java", "C++"]
# Values = [80, 65, 50]

# fig, ax = plt.subplots()

# ax.bar(categories, Values)
# ax.set_title("Skill Comparison")
# ax.set_ylabel("Score")

# plt.show()




# ### Scatter Plots
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 3, 8, 10]

# fig, ax = plt.subplots()

# ax.scatter(x, y)
# ax.set_title("Feature VS Target")
# ax.set_xlabel("Features")
# ax.set_ylabel("Target")

# plt.show()


# ### Histograms
# import numpy as np

# data = np.random.randn(1000)
# fig , ax = plt.subplots()

# ax.hist(data, bins=30)
# ax.set_title("Distribution")
# ax.set_xlabel("Value")
# ax.set_ylabel("Frequency")
# plt.show()


# ### Box Plots
# data = [10, 12, 13, 15, 16, 17, 100]
# fig, ax = plt.subplots()
# ax.boxplot(data)
# ax.set_title("Box Plot")
# ax.grid(True)
# plt.show()


