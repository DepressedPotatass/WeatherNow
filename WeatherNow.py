WeatherNoasync function getWeather(city) {
    const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${city}`);
    const data = await response.json();
    console.log(`Weather in ${city}: ${data.current.temp_c}°C, ${data.current.condition.text}`);
}

getWeather("London");