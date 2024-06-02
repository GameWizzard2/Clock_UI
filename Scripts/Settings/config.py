class Config:
    WINDOW_TITLE = 'Clock'
    LABEL_FONT = ('times new roman', 40, 'bold')
    LABEL_BACKGROUND = 'black'
    LABEL_FOREGROUND = 'gold'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False