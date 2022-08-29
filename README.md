# DeFi ETL Infrastructure
There is some notebooks illustrates different examples of analytical dashboards which infrastructure provides.

## Run locally

**Clone project**
    
     git clone https://github.com/bibliotekue/index-equal-weight-balance.git

**Get project folder**
    
     cd index-equal-weight-balance/
    
**Create virtual environment**

    python -m venv venv
    
**Activate virtual Environment**

    source venv/bin/activate
    
**Install dependencies**

    pip install -r requirements.txt

**Set API key and Config absolute path in secrets.py**

    TOKEN = 'your_tinkoff_api_token'
    
    CONFIG_PATH = 'your_config_absolute_path'
    
**Run script**

    python app.py -i <index_name>

There is only 3 american Indexes such as:
- SP500 (run script with _sp500_ in index argument)
- NASDAQ (run script with _nasdaq_ in index argument)
- DOW JONES (run script with _dowjones_ in index argument)
