import pandas as pd

from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

from sksurv.ensemble import RandomSurvivalForest
from sksurv.datasets import get_x_y

if __name__ == "__main__":

    # Load the data (adjust the filename as needed)
    df = pd.read_csv("data.csv")

    # 'event' - event status (i.e. falls in our case)
    # 'time' - time passed to reach the event; 3 possibilities here:
    # 1) time to the first fall
    # 2) time to when we lost a patient for some reasons (e.g. lost to follow up)
    # 3) time duration of the entire study (this applies to patients that did not fall but were not lost to follow up either)
    # Note: both 'event' and 'time' are column names that represent the above; adjust names as needed
    # event_value - whatever is the value that indicates the patient experienced the event
    event_value = 1
    X, y = get_x_y(df, ['event', 'time'], event_value)

    # Only needed if we have categorical variables
    cat_cols = ['gender']
    X[cat_cols] = OrdinalEncoder().fit_transform(X[cat_cols])

    # Train/test split
    # May need to stratify on the event due to the imbalance
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Risk estimator
    # We can start with 100 trees first and increase if the performance is poor
    # We can also play with max_depth and max_features if we overfit or it takes too long to train
    rsf = RandomSurvivalForest(n_estimators=100, min_samples_split=10, min_samples_leaf=15, n_jobs=-1, random_state=1)

    # Train
    rsf.fit(X_train, y_train)

    # Evaluate on the test set
    score = rsf.score(X_test, y_test)

    print(score)
    # Might be useful to write it to a file