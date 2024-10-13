# Weather Alert Script

This Python script scrapes weather data from [weather.com](https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR) to check for potential heavy rain and sends an email alert if the rain intensity is higher than 60%.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview
The script performs the following tasks:
1. Scrapes weather data from a specified location on weather.com.
2. Parses the weather data for rain percentage throughout the day.
3. Sends an email alert if the rain probability exceeds 60%.

## Requirements
To run this script, you need:
- Python 3.x
- `requests` library for HTTP requests
- `BeautifulSoup` from `bs4` for parsing HTML
- `smtplib` for sending emails

You can install the required Python packages using the following command:

```bash
pip install requests beautifulsoup4
## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/weather-alert.git
    ```

2. Navigate to the project directory:
    ```bash
    cd weather-alert
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the `page` variable with your desired location's weather.com URL:
    ```python
    page = requests.get("https://weather.com/el-GR/weather/today/l/GRXX0004:1:GR")
    ```

2. Customize the email credentials in the `send_gmail()` function:
    ```python
    gmail_user = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    ```

3. Run the script:
    ```bash
    python weather_alert.py
    ```

## Customization

- **Weather Location**: You can change the location by modifying the `page` URL to match the desired weather.com page for your location.

- **Rain Threshold**: You can change the rain threshold (currently 60%) by modifying the condition in the `get_todays_rain()` function:
    ```python
    if max(rain_list) > 60:
    ```

- **Email Content**: Edit the subject and message in the `send_gmail()` function to customize the email notification:
    ```python
    subject = "Weather Alert"
    message = "Warning: Heavy rain expected today."
    ```

## Contributing

Feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
