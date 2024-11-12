# Api-test

A Flask-based API testing project that provides a clean and modular structure for API development and testing, including MQTT functionality.

## Project Structure

```
api_test/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── platforms/
│   │       │   ├── __init__.py
│   │       │   ├── icad/              # ICAD平台
│   │       │   │   ├── __init__.py
│   │       │   │   ├── system.py      # 系统模块API
│   │       │   │   ├── device.py      # 设备模块API
│   │       │   │   └── io.py          # IO模块API
│   │       │   └── platform2/         # 其他平台
│   │       │       ├── __init__.py
│   │       │       └── ...
│   │       └── base_client.py         # 基础客户端
│   └── utils/
│       ├── __init__.py
│       └── test_utils.py
├── tests/
│   └── platforms/
│       ├── icad/
│       │   ├── test_system.py
│       │   ├── test_device.py
│       │   └── test_io.py
│       └── platform2/
├── config.py
└── requirements.txt
```

## Requirements

- Python 3.7+
- Flask 2.0.1
- Flask-CORS 3.0.10
- pytest 6.2.5
- requests 2.26.0
- paho-mqtt 1.5.1

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/yourusername/api-test.git
cd api-test
```

2. Create and activate virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the application:

   - Open `config.py` and adjust settings as needed (e.g., MQTT broker details, API keys)

5. Run the application:

```bash
python run.py
```

6. Test the API: Visit http://localhost:5000/api/v1/system/status

## Features

- Modular API structure using Flask Blueprints
- CORS support enabled
- MQTT client for IoT device communication
- Authentication and authorization system
- Ready-to-use testing framework including stress testing
- Clean project architecture
- Easy to extend and maintain

## API Endpoints

| Endpoint                   | Method | Description        |
| -------------------------- | ------ | ------------------ |
| /api/v1/system/status      | GET    | Get system status  |
| /api/v1/auth/login         | POST   | User login         |
| /api/v1/device/list        | GET    | List all devices   |
| /api/v1/device/<device_id> | GET    | Get device details |

## MQTT Functionality

The MQTT client (`app/mqtt/client.py`) allows for real-time communication with IoT devices. To use:

1. Configure MQTT broker details in `config.py`
2. Import the MQTT client in your API endpoints:

from app.mqtt.client import mqtt_client

@api_bp.route('/device/command', methods=['POST'])
def send_device_command(): # Your logic here
mqtt_client.publish('device/command', command_payload)
return jsonify({'status': 'Command sent'})

## Development

To add new API endpoints, create or modify files in `app/api/v1/`:

from flask import Blueprint, jsonify

new_module_bp = Blueprint('new_module', **name**)

@new_module_bp.route('/your-endpoint', methods=['GET'])
def your_endpoint():
return jsonify({
'message': 'Your response'
})

Then register the blueprint in `app/__init__.py`.

## Testing

Run tests using pytest:

```bash
pytest tests/
```

For stress testing, use the utilities in `app/utils/test_utils.py`.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/api-test
