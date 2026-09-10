import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'CHANGE_ME_IN_PRODUCTION')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    
    # SocketIO configuration
    SOCKETIO_CORS_ALLOWED_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    
    # =============================================
    # MODE SELECTION
    # =============================================
    DEMO_MODE = os.getenv('DEMO_MODE', 'false').lower() == 'true'
    
    # =============================================
    # THREAT MONITORING CONFIGURATION
    # =============================================
    THREAT_CHECK_INTERVAL = int(os.getenv('THREAT_CHECK_INTERVAL', 5))
    
    # Failed Login Detection (Windows Event Log)
    FAILED_LOGIN_ENABLED = os.getenv('FAILED_LOGIN_ENABLED', 'true').lower() == 'true'
    FAILED_LOGIN_THRESHOLD = int(os.getenv('FAILED_LOGIN_THRESHOLD', 5))
    FAILED_LOGIN_TIME_WINDOW = int(os.getenv('FAILED_LOGIN_TIME_WINDOW', 300))
    
    # Process Monitoring (psutil)
    PROCESS_MONITORING_ENABLED = os.getenv('PROCESS_MONITORING_ENABLED', 'true').lower() == 'true'
    PROCESS_CHECK_INTERVAL = int(os.getenv('PROCESS_CHECK_INTERVAL', 5))
    SUSPICIOUS_PROCESSES = os.getenv('SUSPICIOUS_PROCESSES', 'mimikatz.exe,psexec.exe').split(',')
    PROCESS_MONITORING_EXCLUDE = os.getenv('PROCESS_MONITORING_EXCLUDE', 'svchost.exe,services.exe').split(',')
    
    # Network Monitoring (psutil)
    NETWORK_MONITORING_ENABLED = os.getenv('NETWORK_MONITORING_ENABLED', 'true').lower() == 'true'
    NETWORK_CHECK_INTERVAL = int(os.getenv('NETWORK_CHECK_INTERVAL', 5))
    PORT_SCAN_DETECTION_ENABLED = os.getenv('PORT_SCAN_DETECTION_ENABLED', 'true').lower() == 'true'
    PORT_SCAN_THRESHOLD = int(os.getenv('PORT_SCAN_THRESHOLD', 10))
    PORT_SCAN_TIME_WINDOW = int(os.getenv('PORT_SCAN_TIME_WINDOW', 300))
    
    # =============================================
    # DATABASE
    # =============================================
    DATABASE_PATH = os.getenv('DATABASE_PATH', './threat_monitor.db')
    
    # =============================================
    # LOGGING
    # =============================================
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', './logs/threat_monitor.log')
    
    # =============================================
    # ALERT RETENTION & STORAGE
    # =============================================
    ALERT_RETENTION_HOURS = int(os.getenv('ALERT_RETENTION_HOURS', 24))
    MAX_STORED_THREATS = int(os.getenv('MAX_STORED_THREATS', 10000))
    
    # =============================================
    # SEVERITY LEVELS
    # =============================================
    SEVERITY_LEVELS = {
        'CRITICAL': 4,
        'HIGH': 3,
        'MEDIUM': 2,
        'LOW': 1,
        'INFO': 0
    }
    
    # =============================================
    # DEDUPLICATION
    # =============================================
    DEDUPLICATION_WINDOW = int(os.getenv('DEDUPLICATION_WINDOW', 3600))
    CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.6))

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    DEMO_MODE = False  # Real detection in development

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEMO_MODE = os.getenv('DEMO_MODE', 'false').lower() == 'true'

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DEMO_MODE = True  # Use demo mode for testing
    SOCKETIO_CORS_ALLOWED_ORIGINS = "*"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
