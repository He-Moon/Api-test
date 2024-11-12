# Api-test

A Flask-based API testing project that provides a clean and modular structure for API development and testing.

## Project Structure

```bash
api_test/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── system.py    # 系统相关接口
│   │       ├── device.py    # 设备相关接口
│   │       └── auth.py      # 认证相关接口
│   ├── mqtt/
│   │   ├── __init__.py
│   │   └── client.py        # MQTT客户端
│   └── utils/
│       ├── __init__.py
│       ├── auth.py          # 认证工具
│       └── test_utils.py    # 测试工具(压测、流程测试)
├── tests/
│   ├── test_auth.py
│   ├── test_device.py
│   └── test_system.py
├── config.py                # 配置文件
├── run.py
└── requirements.txt
```

## Requirements

- Python 3.7+
- Flask 2.0.1
- Flask-CORS 3.0.10
- pytest 6.2.5
- requests 2.26.0

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/yourusername/api-test.git
cd api-test
```

2. Create and activate virtual environment (optional but recommended):

```bash
pip install -r requirements.txt
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python run.py
```

5. Test the API: Visit http://localhost:5000/api/v1/test

## Features

- Modular API structure using Flask Blueprints
- CORS support enabled
- Ready-to-use testing framework
- Clean project architecture
- Easy to extend and maintain

## API Endpoints

| Endpoint     | Method | Description                            |
| ------------ | ------ | -------------------------------------- |
| /api/v1/test | GET    | Test endpoint to verify API is working |

## Development

To add new API endpoints, modify `app/api/v1/routes.py`:

```python
@api_bp.route('/your-endpoint', methods=['GET'])
def your_endpoint():
    return jsonify({
        'message': 'Your response'
    })
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

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
