""" Config File """
#pylint: disable=too-few-public-methods, line-too-long


class BaseConfig():
    """
    Generel System white Configuration.
    Can be overwritten later if needed.
    """
    SECRET_KEY = '_\#"+<gt2G*GTx7TcEX"aEKX:3$ufbWHNx?4}DL5=&'
    DEBUG = False  # Special for Developement
    APPLY_HEADERS = True  #Set to False if used with NGINX

    SPICE_DEBUG = False

class ProductionConfig(BaseConfig):
    """
    Production Configuration.
    """
    SESSION_COOKIE_SECURE = True
    SITENAME = "Subscription API"
    ENABLE_SENTRY = False

class DevelopmentConfig(BaseConfig):
    """
    Development Configuration.
    """
    SITENAME = "Subscription API DEV"
    TEMPLATE_AUTO_RELOAD = True
    DEBUG = True
    FLASK_DEBUG = True


class TestingConfig(DevelopmentConfig):
    """ UNITTEST Configuration """
    PRINT_DEBUG = False


class DockerConfig(DevelopmentConfig):
    """"
    Specific configuration for Docker Env
    """
    TEMPLATE_AUTO_RELOAD = False
    APPLY_HEADERS = False
    DEBUG = True


class DockerConfigProd(ProductionConfig):
    """"
    Specific configuration for Docker Env
    """
    APPLY_HEADERS = False
    TEMPLATE_AUTO_RELOAD = False
