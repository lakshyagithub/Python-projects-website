import matplotlib.pyplot as plt

data = [
        [10, 10, 10, 10, 10, 10, 10, 10 , 10, 10, 10],
        [10, 10, 10, 0, 0, 0, 0, 0 , 10, 10, 10],
        [10, 10, 0, 4, 4, 4, 4, 4, 0, 10, 10],
        [10, 0, 4, 4, 4, 4, 4, 4, 4, 0, 10],
        [10, 0, 4, 4, 4, 0, 4, 4, 4, 0, 10],
        [10, 0, 0, 0, 0, 10, 0, 0 , 0, 0, 10],
        [10, 0, 10, 10, 10, 0, 10, 10 , 10, 0, 10],
        [10, 10, 0, 10, 10, 10, 10, 10 , 0, 10, 10],
        [10, 10, 10, 0, 0, 0, 0, 0 , 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10 , 10, 10, 10]]

plt.imshow(data, cmap="hot")
plt.show()