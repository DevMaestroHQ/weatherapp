
# WeatherApp

WeatherApp is a Python-based application that uses Streamlit to fetch and display weather information for any location. It leverages modern Python tools and APIs, specifically WeatherAPI and AccuWeatherAPI, to provide accurate and up-to-date weather data in a simple, user-friendly interface.

## Features

- Retrieve current weather data for any city or location
- Display temperature, humidity, wind speed, and weather conditions
- Interactive and easy-to-use Streamlit web interface
- Modular code for easy extension and customization

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DevMaestroHQ/weatherapp.git
   cd weatherapp
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the Streamlit app:

```bash
streamlit run main.py
```

Then, open the provided local URL in your web browser and follow the prompts to check the weather for your desired city.

## Configuration

- **API Keys:**  
  This app requires API keys from [WeatherAPI](https://www.weatherapi.com/) and/or [AccuWeatherAPI](https://developer.accuweather.com/).
  
  Create a `.env` file in the project root and add your API keys:

  ```
  WEATHERAPI_KEY=your_weatherapi_key_here
  ACCUWEATHERAPI_KEY=your_accuweatherapi_key_here
  ```

## Project Structure

```
weatherapp/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── ... (other modules and files)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements, bug fixes, or new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [WeatherAPI](https://www.weatherapi.com/) and [AccuWeatherAPI](https://developer.accuweather.com/) for providing weather data APIs
- [Streamlit](https://streamlit.io/) for the interactive web app framework
- Python community for libraries and support

---

Feel free to update this README with any additional details relevant to your version of the WeatherApp!
