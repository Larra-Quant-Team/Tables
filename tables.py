from mongo_api.mongo_api import _MongoSeries, _MongoDoc, _MongoTable

class EquityMaster(_MongoSeries):
    _name = 'equity_master'
    _key_ls = ['country', 'currency', 'asset', 'investable', 
               'ind_sector', 'ind_group', 'ind_industry',
               'ind_internal', 'ind_esg', 'field']
    _drop_weekends = True
    _override_boolean_key = ['investable']

class IndicesMaster(_MongoSeries):
    _name = 'indices_master'
    _key_ls = ['country', 'currency', 'asset', 'field']
    _drop_weekends = True 