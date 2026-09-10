import re
from datetime import datetime, timedelta
from collections import defaultdict
import random
import uuid

class ThreatDetector:
    """Detects security threats from logs and system activity"""
    
    def __init__(self, config):
        self.config = config
        self.threat_history = []
        self.login_attempts = defaultdict(list)
        self.port_access = defaultdict(list)
        self.severity_colors = {
            'CRITICAL': '#dc2626',
            'HIGH': '#ea580c',
            'MEDIUM': '#eab308',
            'LOW': '#3b82f6',
            'INFO': '#10b981'
        }
        
    def detect_threats(self):
        """Main threat detection method"""
        threats = []
        
        # Detect failed login attempts
        threats.extend(self._detect_failed_logins())
        
        # Detect port scanning
        threats.extend(self._detect_port_scanning())
        
        # Detect privilege escalation
        threats.extend(self._detect_privilege_escalation())
        
        # Detect suspicious processes
        threats.extend(self._detect_suspicious_processes())
        
        # Generate demo threats for hackathon
        threats.extend(self._generate_demo_threats())
        
        return threats
    
    def _detect_failed_logins(self):
        """Detect multiple failed login attempts"""
        threats = []
        current_time = datetime.now()
        time_window = timedelta(seconds=self.config.FAILED_LOGIN_TIME_WINDOW)
        
        failed_logins = {
            'user@192.168.1.100': 7,
            'admin@10.0.0.50': 12,
            'root@172.16.0.25': 8
        }
        
        for source, count in failed_logins.items():
            if count >= self.config.FAILED_LOGIN_THRESHOLD:
                threat = {
                    'id': str(uuid.uuid4()),
                    'type': 'Failed Login Attempts',
                    'severity': 'HIGH' if count > 10 else 'MEDIUM',
                    'source': source,
                    'description': f'{count} failed login attempts from {source}',
                    'timestamp': current_time.isoformat(),
                    'details': {
                        'attempts': count,
                        'threshold': self.config.FAILED_LOGIN_THRESHOLD,
                        'source_ip': source.split('@')[1]
                    }
                }
                threats.append(threat)
        
        return threats
    
    def _detect_port_scanning(self):
        """Detect potential port scanning activity"""
        threats = []
        current_time = datetime.now()
        
        suspicious_ips = {
            '192.168.1.150': 25,
            '10.0.0.99': 50,
            '203.0.113.42': 15
        }
        
        for ip, port_count in suspicious_ips.items():
            if port_count >= self.config.SUSPICIOUS_PORT_THRESHOLD:
                threat = {
                    'id': str(uuid.uuid4()),
                    'type': 'Port Scanning',
                    'severity': 'CRITICAL' if port_count > 40 else 'HIGH',
                    'source': ip,
                    'description': f'Potential port scan detected from {ip}',
                    'timestamp': current_time.isoformat(),
                    'details': {
                        'ports_accessed': port_count,
                        'threshold': self.config.SUSPICIOUS_PORT_THRESHOLD,
                        'source_ip': ip
                    }
                }
                threats.append(threat)
        
        return threats
    
    def _detect_privilege_escalation(self):
        """Detect potential privilege escalation attempts"""
        threats = []
        current_time = datetime.now()
        
        escalation_attempts = [
            {'user': 'john', 'command': 'sudo -s'},
            {'user': 'alice', 'command': 'su root'},
        ]
        
        for attempt in escalation_attempts:
            threat = {
                'id': str(uuid.uuid4()),
                'type': 'Privilege Escalation Attempt',
                'severity': 'CRITICAL',
                'source': attempt['user'],
                'description': f"User '{attempt['user']}' attempted privilege escalation",
                'timestamp': current_time.isoformat(),
                'details': {
                    'username': attempt['user'],
                    'command': attempt['command'],
                    'status': 'Failed'
                }
            }
            threats.append(threat)
        
        return threats
    
    def _detect_suspicious_processes(self):
        """Detect suspicious process execution"""
        threats = []
        current_time = datetime.now()
        
        suspicious_processes = [
            {'name': 'mimikatz.exe', 'risk': 'CRITICAL'},
            {'name': 'psexec.exe', 'risk': 'HIGH'},
            {'name': 'nmap', 'risk': 'MEDIUM'}
        ]
        
        for process in suspicious_processes:
            if random.random() > 0.7:  # Random trigger for demo
                threat = {
                    'id': str(uuid.uuid4()),
                    'type': 'Suspicious Process',
                    'severity': process['risk'],
                    'source': 'system',
                    'description': f"Suspicious process detected: {process['name']}",
                    'timestamp': current_time.isoformat(),
                    'details': {
                        'process_name': process['name'],
                        'process_id': str(random.randint(1000, 9999)),
                        'parent_process': 'cmd.exe'
                    }
                }
                threats.append(threat)
        
        return threats
    
    def _generate_demo_threats(self):
        """Generate demo threats for hackathon presentation"""
        threats = []
        current_time = datetime.now()
        
        demo_threats = [
            {
                'type': 'Unauthorized File Access',
                'severity': 'HIGH',
                'source': '/etc/passwd',
                'description': 'Unauthorized access to sensitive system file'
            },
            {
                'type': 'Anomalous Network Traffic',
                'severity': 'MEDIUM',
                'source': 'eth0',
                'description': 'Unusual outbound traffic detected to suspicious IP'
            },
            {
                'type': 'Firewall Block',
                'severity': 'LOW',
                'source': '203.0.113.15',
                'description': 'Firewall blocked connection attempt'
            }
        ]
        
        # Occasionally add a demo threat
        if random.random() > 0.6:
            threat_data = random.choice(demo_threats)
            threat = {
                'id': str(uuid.uuid4()),
                'type': threat_data['type'],
                'severity': threat_data['severity'],
                'source': threat_data['source'],
                'description': threat_data['description'],
                'timestamp': current_time.isoformat(),
                'details': {
                    'event_id': random.randint(1000, 9999),
                    'category': 'Security'
                }
            }
            threats.append(threat)
        
        return threats
    
    def get_threat_stats(self):
        """Get threat statistics"""
        if not self.threat_history:
            return {
                'total_threats': 0,
                'critical': 0,
                'high': 0,
                'medium': 0,
                'low': 0,
                'avg_response_time': 0
            }
        
        stats = {
            'total_threats': len(self.threat_history),
            'critical': len([t for t in self.threat_history if t['severity'] == 'CRITICAL']),
            'high': len([t for t in self.threat_history if t['severity'] == 'HIGH']),
            'medium': len([t for t in self.threat_history if t['severity'] == 'MEDIUM']),
            'low': len([t for t in self.threat_history if t['severity'] == 'LOW']),
            'avg_response_time': 45  # milliseconds (demo)
        }
        
        return stats
    
    def add_threat_to_history(self, threat):
        """Add threat to history"""
        self.threat_history.append(threat)
        # Keep only recent threats (last 24 hours)
        cutoff_time = datetime.now() - timedelta(hours=self.config.ALERT_RETENTION_HOURS)
        self.threat_history = [t for t in self.threat_history 
                              if datetime.fromisoformat(t['timestamp']) > cutoff_time]
