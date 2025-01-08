# TaskTracker

## Overview

TaskTracker is a Python-based application designed for real-time monitoring of system operations on Windows. This tool aims to enhance system efficiency and performance by providing users with continuous insights into CPU, memory, and disk usage.

## Features

- **Real-Time Monitoring**: Get up-to-the-minute statistics on system performance.
- **CPU Usage Tracking**: Monitor how much of your CPU is being consumed.
- **Memory Usage Insights**: Keep an eye on the system's memory utilization.
- **Disk Usage Overview**: Check the current disk usage status.

## Requirements

- Python 3.6 or above
- `psutil` library

## Installation

1. Ensure you have Python 3.6 or newer installed on your Windows system.
2. Install the required library by running:
    ```
    pip install psutil
    ```

## Usage

1. Clone the repository or download the `task_tracker.py` file.
2. Run the script using:
    ```
    python task_tracker.py
    ```
3. The program will start monitoring system performance, printing logs every 5 seconds.

## Customization

- You can adjust the logging interval by modifying the `log_interval` parameter in the `TaskTracker` class instantiation:
  ```python
  tracker = TaskTracker(log_interval=10)  # Logs every 10 seconds
  ```

## Stopping the Program

- To stop the monitoring, simply press `Ctrl+C` in the command line where the script is running.

## License

This project is licensed under the MIT License.