
# MOVIES IN THE CITY API

The project is an API designed to provide information about movies currently being shown in a particular city.



## API Reference
Flask was used to construct this API. It delivers the required data by scraping data from paytm.com/movies. To obtain results, simply hit the api; no specific key is required. 

#### Get all movies in your city

```http
  GET /?city={YourCityName}
```

| Parameter | Type     | Description                |
| - | - | - |
| `city` | `string` | **\*Required**. Your city name |



## Run Locally

Clone the project

```bash
  git clone https://github.com/Madhav-Gohel/MOVIES-IN-THE-CITY-API.git
```

Go to the project directory

```bash
  cd MOVIES-IN-THE-CITY-API
```
\
Install dependencies `(Windows)`

```bash
  pip install -r requirements.txt
```
Install dependencies `(Linux/Mac)`

```bash
  pip3 install -r requirements.txt
```
\
Start the server `(Windows)`

```bash
  python app.py
```
Start the server `(Linux/Mac)`

```bash
  python3 app.py
```

## Tech Stack

**Server:** Python, Flask
