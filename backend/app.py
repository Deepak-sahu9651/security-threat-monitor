from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from config import config
from threat_detector import ThreatDetector
import os
from datetime import datetime
import threading
import time

# Initialize Flask app
app = Flask(__name__)
config_name = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize threat detector
threat_detector = ThreatDetector(app.config)

# Storage for connected clients
connected_clients = set()

# ==================== ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

@app.route('/api/threats', methods=['GET'])
def get_threats():
    """Get all detected threats"""
    severity = request.args.get('severity', None)
    
    threats = threat_detector.threat_history
    
    if severity:
        threats = [t for t in threats if t['severity'] == severity]
    
    return jsonify({
        'total': len(threats),
        'threats': threats,
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/threats/<threat_id>', methods=['GET'])
def get_threat_detail(threat_id):
    """Get detailed information about a specific threat"""
    threat = next((t for t in threat_detector.threat_history if t['id'] == threat_id), None)
    
    if not threat:
        return jsonify({'error': 'Threat not found'}), 404
    
    return jsonify(threat), 200

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get threat statistics"""
    stats = threat_detector.get_threat_stats()
    stats['timestamp'] = datetime.now().isoformat()
    stats['connected_clients'] = len(connected_clients)
    
    return jsonify(stats), 200

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get configuration (non-sensitive)"""
    return jsonify({
        'threat_check_interval': app.config['THREAT_CHECK_INTERVAL'],
        'failed_login_threshold': app.config['FAILED_LOGIN_THRESHOLD'],
        'alert_retention_hours': app.config['ALERT_RETENTION_HOURS'],
        'severity_levels': app.config['SEVERITY_LEVELS']
    }), 200

# ==================== SOCKETIO EVENTS ====================

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    connected_clients.add(request.sid)
    emit('connection_response', {
        'data': 'Connected to threat monitor',
        'connected_clients': len(connected_clients),
        'timestamp': datetime.now().isoformat()
    })
    print(f'Client connected: {request.sid}. Total clients: {len(connected_clients)}')

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    connected_clients.discard(request.sid)
    print(f'Client disconnected: {request.sid}. Total clients: {len(connected_clients)}')

@socketio.on('subscribe_threats')
def handle_subscribe_threats():
    """Subscribe to threat updates"""
    emit('subscribe_response', {
        'status': 'subscribed',
        'message': 'You will receive real-time threat alerts'
    })

@socketio.on('unsubscribe_threats')
def handle_unsubscribe_threats():
    """Unsubscribe from threat updates"""
    emit('unsubscribe_response', {
        'status': 'unsubscribed'
    })

# ==================== BACKGROUND THREAT MONITORING ====================

def monitor_threats():
    """Background thread that continuously monitors for threats"""
    with app.app_context():
        while True:
            try:
                # Detect threats
                threats = threat_detector.detect_threats()
                
                # Add threats to history and broadcast
                for threat in threats:
                    threat_detector.add_threat_to_history(threat)
                    
                    # Broadcast threat to all connected clients
                    socketio.emit('new_threat', threat, broadcast=True)
                    
                    print(f"[{threat['severity']}] {threat['type']}: {threat['description']}")
                
                # Broadcast stats update
                stats = threat_detector.get_threat_stats()
                stats['connected_clients'] = len(connected_clients)
                socketio.emit('stats_update', stats, broadcast=True)
                
                # Check interval
                time.sleep(app.config['THREAT_CHECK_INTERVAL'])
                
            except Exception as e:
                print(f"Error in threat monitoring: {str(e)}")
                time.sleep(5)

# ==================== STARTUP ====================

if __name__ == '__main__':
    # Start background monitoring thread
    monitor_thread = threading.Thread(target=monitor_threats, daemon=True)
    monitor_thread.start()
    
    print("🛡️  Security Threat Monitor Backend Starting...")
    print(f"Environment: {config_name}")
    print(f"Debug: {app.config['DEBUG']}")
    print(f"Threat check interval: {app.config['THREAT_CHECK_INTERVAL']}s")
    
    # Run SocketIO server
    socketio.run(
        app,
        host='0.0.0.0',
        port=5000,
        debug=app.config['DEBUG'],
        allow_unsafe_werkzeug=True
    )
