def chart():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    bmi = pd.read_csv('arkuszwyniki.csv')
    print(bmi)
    ax = sns.barplot(x='Imie', y='BMI', data=bmi, order=bmi.sort_values('BMI').Imie, palette="coolwarm")
    for i in ax.containers:
        ax.bar_label(i,)
    plt.show()
fgh