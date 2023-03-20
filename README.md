# DataScience
🐍 Python Scripts for query methods.

## 1. A script that automatically downloads data from an API: `API_kotlin.py`
```python
import requests
import json

url = "https://api.example.com/data"
response = requests.get(url)
data = json.loads(response.text)
print(data)
```
This script uses the `requests` library to send an HTTP request to an API and the json library to parse the JSON response.

## 2. A script that reads data from a CSV file and converts it to a Pandas dataframe: `csv_kotlin.py`
```python
import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print(df.head())
```
This script uses the `pandas` library to read data from a CSV file and convert it into a Pandas dataframe, which is a useful data structure for data analysis.

## 3. A script that uses the Scikit-learn library to create a linear regression model: `scss.py`
```python
from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('data.csv')
X = data[['feature_1', 'feature_2']]
y = data['target']
model = LinearRegression()
model.fit(X, y)
print(model.coef_)
```
This script uses the `Scikit-learn` library to create a linear regression model and fit it to the data.

## 4. A script that uses the Matplotlib library to create a bar chart: `matplotlib.py`
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.bar(x, y)
plt.show()
```
This script uses the `Matplotlib` library to create a simple bar chart.

## 5. A script that automates the task of sending an email with an attachment: `send_mail.py`
```python
import smtplib
import os

FROM_EMAIL = 'example@gmail.com'
FROM_PWD = 'password'
TO_EMAIL = 'recipient@example.com'
SUBJECT = 'Datos adjuntos'
FILE_PATH = 'data.csv'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(FROM_EMAIL, FROM_PWD)

with open(FILE_PATH, 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(FILE_PATH)
    msg = 'Subject: {}\n\n'.format(SUBJECT)
    msg += 'Adjunto encontrará los datos solicitados.'
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg, file_data)
    
server.quit()
```
This script uses the `smtplib` library to send an email with an attached file. This type of script is useful for automating the task of sending reports or data to colleagues or clients.

# Examples

## 1. Datos meteorológicos
```python
import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=API_KEY'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    temperatura = data['main']['temp']
    presion = data['main']['pressure']
    humedad = data['main']['humidity']
    print('La temperatura en Londres es', temperatura, 'K')
    print('La presión atmosférica en Londres es', presion, 'hPa')
    print('La humedad en Londres es', humedad, '%')
else:
    print('No se pudo obtener los datos meteorológicos')
```
En este ejemplo, se utiliza la API de OpenWeatherMap para obtener los datos meteorológicos de Londres. Se utiliza la biblioteca requests para enviar una solicitud HTTP a la API y la biblioteca json para analizar la respuesta JSON.

## 2. Datos de criptomonedas
```python
import requests
import json

url = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    for moneda in data:
        nombre = moneda['name']
        precio = moneda['price_usd']
        capitalizacion = moneda['market_cap_usd']
        print(nombre, 'tiene un precio de', precio, 'USD y una capitalización de mercado de', capitalizacion, 'USD')
else:
    print('No se pudo obtener los datos de criptomonedas')
```
En este ejemplo, se utiliza la API de CoinMarketCap para obtener los datos de las 10 criptomonedas más populares. Se utiliza la biblioteca requests para enviar una solicitud HTTP a la API y la biblioteca json para analizar la respuesta JSON.

## 3. Datos de noticias
```python
import requests
import json

url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    for noticia in data['articles']:
        titulo = noticia['title']
        descripcion = noticia['description']
        url = noticia['url']
        print(titulo)
        print(descripcion)
        print(url)
else:
    print('No se pudo obtener los datos de noticias')
```
En este ejemplo, se utiliza la API de NewsAPI para obtener las principales noticias de EE. UU. Se utiliza la biblioteca requests para enviar una solicitud HTTP a la API y la biblioteca json para analizar la respuesta JSON.

```python

```
## From scratch 
[Scratschpads.pdf](https://github.com/DimaGutierrez/DataScience/blob/main/Scratchpads.pdf)
### Files
`databases.py` `logistic_regression.py` `neural_networks.py` `statistics.py` `network_analysis.py`
    
           
         
