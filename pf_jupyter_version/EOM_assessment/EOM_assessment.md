# End of Module Assessment

You've covered a lot of Python so far, and there is more in future topics - we still need to look at data science specific libraries, and python with databases, but we're going to move on for now.

We're now going to review the functionality of a different publicly accessible API, which will form the basis of your end of module assessment.

[**Open-Meteo**](https://github.com/open-meteo/open-meteo) is an open-source weather API that offers free access for non-commercial use. No API key is required, so you can start using it immediately.

The URL to access the API is = https://api.open-meteo.com/v1/forecast

In order to retrieve weather data you need to submit query parameters within your API request against the endpoint.

The parameters should be defined in a dictionary.

>As discussed when building the CaaS app, query parameters are `key:value` pairs included in the query string (after the question mark).

Properly forming your API request is a key part of your end of module assessment.

The full API documentation is provided here: [Open-Mateo API Documentation](https://open-meteo.com/en/docs)

## Assessment Brief

Write a Python Script which will return the below parameters as a 3 day weather forecast for Big Ben in London.

Your API call should include the following query parameters:

- Average Hourly temperature
- Average Hourly rain
- Daily maximum and minimum temperatures
- Current temperature

Streth & Challenge:

- Current weather code translated into a description
- Persist the retrieved json object into a file called weatehr_response.json in the same directory as your app.

<details><summary>Hint - if you get stuck:</summary>

Sample JSON object here: [weather_response.json](./weather_response.json)
We've yet to cover data persistence - you're expected to research this functionality

</details>
