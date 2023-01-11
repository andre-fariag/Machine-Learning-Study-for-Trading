import matplotlib.pyplot as plt

#plot entire data frame
def plot_data(df,title,x_label,y_label):
    ax = df.plot(title=title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.grid()
    plt.show()

#plot a specficic region of data frame
def plot_selected(df,columns,start_index,end_index,title,x_label,y_label):
    plot_data(df.loc[start_index:end_index,columns],title,x_label,y_label)