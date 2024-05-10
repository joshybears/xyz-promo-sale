# xyz-promo-sale

## How to setup and run
1. In this project, we use Pipenv to install Python dependencies that we need for our ETL script. Make sure you have Pipenv installed (https://pipenv.pypa.io/en/latest/installation.html).
2. Simply run `pipenv install` in the main directory. This will install all the libraries and dependencies that the project needs according to the Pipfile.
3. You may run `pipenv run python get_data_pandas.py` to run the script that uses Pandas to produce `result_pandas.csv`.
4. You may run `pipenv run python get_data_sql.py` to run the script that uses just SQL and CSV libs to produce `result_sql.csv`.