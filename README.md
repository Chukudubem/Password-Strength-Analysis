### ML-based Password Strength Classification 
- Given a dataset of 700,000+ passwords and their classification [0,1,2]
- Created features to model this classification.
- Performed Logistic Regression on training data

To do:
Create additional feature (bool) for dictionary words

NOTE:
In my script, I have done some processing of the data, saved, and reloaded the processed data. This is because the input file is in csv format which means each value is separated by comma. This poses an interesting situation when passwords contain commas.
