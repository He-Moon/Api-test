import pytest
import logging
from datetime import datetime
from app.api.v1.platforms.icad import ICADClient
from config import Config

@pytest.fixture(scope="session")
def test_config():
    """
    Test configuration fixture that provides test parameters
    
    Returns:
        dict: Configuration parameters including:
            - user_id: Admin username for authentication
            - password: Admin password for authentication
            - project_id: Target project identifier
            - ping_intervals: List of intervals in seconds for ping tests
            - test_duration: Duration in seconds for each ping test
    """
    return {
        "user_id": "admin",
        "password": "password",
        "project_id": 1,
        "ping_intervals": [0.1, 0.5, 1],
        "test_duration": 60
    }

@pytest.fixture(scope="session")
def icad_client():
    """
    Creates and configures ICAD client instance with logging setup
    
    Returns:
        ICADClient: Configured client instance for ICAD platform
    """
    client = ICADClient(Config.PLATFORMS['icad'])
    logging.basicConfig(
        filename=f'test_icad_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return client

def test_login_flow(icad_client, test_config):
    """
    Tests the complete login flow including user authentication and project sign-in
    
    Parameters:
        icad_client: ICAD client instance
        test_config: Test configuration containing credentials
    
    Verifies:
        1. User authentication success
        2. Project sign-in success
    """
    # Test user authentication
    logging.info(f"Attempting authentication for user: {test_config['user_id']}")
    auth_result = icad_client.authenticate(test_config["user_id"], test_config["password"])
    logging.info(f"Authentication response: {auth_result}")
    assert auth_result["IsSuccess"] == True
    
    # Test project sign-in
    logging.info(f"Attempting project sign-in for project ID: {test_config['project_id']}")
    project_result = icad_client.system.project_sign_in(test_config["project_id"])
    logging.info(f"Project sign-in response: {project_result}")
    assert project_result["IsSuccess"] == True

def test_ping_frequency(icad_client, test_config):
    """
    Tests the system ping functionality at different intervals
    
    Parameters:
        icad_client: ICAD client instance
        test_config: Test configuration containing ping intervals and duration
    
    Test Flow:
        1. Iterates through different ping intervals (0.1s, 0.5s, 1s)
        2. For each interval, sends ping requests for specified duration
        3. Tracks success and error counts
        4. Logs detailed results including response data
    """
    for interval in test_config["ping_intervals"]:
        success_count = error_count = 0
        start_time = datetime.now()
        
        logging.info(f"Starting ping test with interval: {interval}s")
        
        while (datetime.now() - start_time).seconds < test_config["test_duration"]:
            try:
                logging.debug(f"Sending ping request at {datetime.now()}")
                result = icad_client.system.ping()
                
                # Log complete response data
                logging.debug(f"Ping response data: {result}")
                
                if result["IsSuccess"]:
                    success_count += 1
                    logging.debug(f"Ping successful - Response: {result}")
                else:
                    error_count += 1
                    logging.warning(f"Ping failed - Error response: {result}")
            except Exception as e:
                error_count += 1
                logging.error(f"Ping exception occurred: {str(e)}", exc_info=True)
                
        # Detailed test results summary
        test_summary = f"""
        ====== Ping Test Summary ======
        Interval: {interval}s
        Duration: {test_config["test_duration"]}s
        Total Requests: {success_count + error_count}
        Successful Requests: {success_count}
        Failed Requests: {error_count}
        Error Rate: {error_count/(success_count + error_count)*100:.2f}%
        =============================="""
        
        logging.info(test_summary)
        print(test_summary)  # Console output for immediate feedback