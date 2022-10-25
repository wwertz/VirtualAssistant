import requests, json

class Weather:
    def __init__(self):
        self.api_key = "7e832a539218168cfd4f2dbea4b523ef"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def getWeather(self, city_name):
        #complete url address
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city_name
        print(complete_url)
        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            xreturn = ('Temperature (in Fahrenheit) = ' +
                            str(round(1.8 * (current_temperature-273.15)+32)) +
                ' atmospheric pressure (in hPa unit) = ' +
                            str(current_pressure) +
                ' humidity (in percentage) = ' +
                            str(current_humidity) +
                ' description = ' +
                            str(weather_description))
            return xreturn

        else:
            print(" City Not Found ")
