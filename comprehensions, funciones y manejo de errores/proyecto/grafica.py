import matplotlib.pyplot as plt

def graficaBarra(labels, values):
   
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def graficaCircular(labels, values):
    fig, ax = plt.subplots()
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    ax.pie(values, labels=labels, colors=bar_colors, shadow=True)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [121, 555, 300]
    #graficaBarra(labels, values)
    graficaCircular(labels, values)