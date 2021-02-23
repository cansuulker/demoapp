import ssl


class Config(object):
    # some other settings
    # ...
    # db settings
    MONGODB_SETTINGS = {
        'MONGODB_HOST': 'mongodb+srv://admin:arU1TensYAUHbzVB@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority',
        'MONGODB_SSL': True,
    }