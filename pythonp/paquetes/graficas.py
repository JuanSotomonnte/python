import matplotlib.pyplot as plt # type: ignore

def generargrafica():
    labels=['a','b','c','d']
    values=[100,200,300,400]

    fig,ax=plt.subplots()
    ax.bar(labels,values)
    plt.show

    if __name__== '__main__':
        generargrafica(labels,values)
