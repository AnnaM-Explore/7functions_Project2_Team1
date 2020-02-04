def extract_municipality_hashtags(df):
    import numpy, pandas
    municipality_dict = {'@CityofCTAlerts': 'Cape Town',
                         '@CityPowerJhb': 'Johannesburg',
                         '@eThekwiniM': 'eThekwini',
                         '@EMMInfo': 'Ekurhuleni',
                         '@centlecutility': 'Mangaung',
                         '@NMBmunicipality': 'Nelson Mandela Bay',
                         '@CityTshwane': 'Tshwane'}
    def extract_hashtags(tweet):
        return [word for word in tweet.split() if word.startswith('#')] or numpy.nan
    def extract_municipality(tweet):
        return [word for word in tweet.split() if word in municipality_dict] or numpy.nan
    df['hashtags'] = df['Tweets'].apply(extract_hashtags)
    df['municipality'] = df['Tweets'].apply(extract_municipality)
    return df
