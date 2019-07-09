### ML-based Password Strength Classification 
- Given a dataset of 700,000+ passwords and their classification [0,1,2]
- Created features to model this classification.

  1. password lengths
  2. number of special characters used 
  3. number of digits used
  4. number of capitalization used
  5. Contains dictionary word

- Performed Logistic Regression on training data

To do:
Create additional feature (bool) for dictionary words

**NOTE:**
In my script, I have done some processing of the data, saved, and reloaded the processed data. This is because the input file is in csv format which means each value is separated by comma. This poses an interesting situation when passwords contain comma(s).
