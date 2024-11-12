import pytest
import logging
from datetime import datetime
from pathlib import Path

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        filename=log_dir / f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
