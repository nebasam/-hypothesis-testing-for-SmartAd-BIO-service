def read_proccessed_data(csv_path):
    try:    
        db = pd.read_csv(csv_path)
        print("file read as csv")
        return db.head()
    except FileNotFoundError:
        print("file not found")
def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Plot count of {column}', size=20, fontweight='bold')
    plt.xticks(rotation=70)


def plot_counttwo(df,col1,col2):
    plt.figure(figsize=(12,8))
    plt.subplot(1,2,1)
    sns.countplot(data=df, x=col1,palette='summer')
    plt.title(f'Distribution of {col1}', size=16, fontweight='bold')
    plt.xticks(rotation=70)
    
    plt.subplot(1,2,2)
    sns.countplot(data=df, x=col2,palette='summer_r')
    plt.title(f'Distribution of {col2}', size=16, fontweight='bold')
    plt.xticks(rotation=70)
    plt.show()