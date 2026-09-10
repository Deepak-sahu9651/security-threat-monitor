import os
from datetime import timedelta

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('DEBUG', True)
    
    # SocketIO configuration
    SOCKETIO_CORS_ALLOWED_ORIGINS = "*"
    
    # Threat detection configuration
    THREAT_CHECK_INTERVAL = 5  # seconds
    LOG_FILE_PATHS = [
        '/var/log/auth.log',  # Linux
        '/var/log/secure',    # RHEL/CentOS
        'C:\\Windows\\System32\\winevt\\Logs\\Security.evtx'  # Windows
    ]
    
    # Threat thresholds
    FAILED_LOGIN_THRESHOLD = 5  # failed logins in time window
    FAILED_LOGIN_TIME_WINDOW = 300  # 5 minutes in seconds
    SUSPICIOUS_PORT_THRESHOLD = 10  # port access attempts
    
    # Severity levels
    SEVERITY_LEVELS = {
        'CRITICAL': 4,
        'HIGH': 3,
        'MEDIUM': 2,
        'LOW': 1,
        'INFO': 0
    }
    
    # Alert retention
    ALERT_RETENTION_HOURS = 24

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SOCKETIO_CORS_ALLOWED_ORIGINS = "*"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
