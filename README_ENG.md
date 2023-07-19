# Website about agencies organizing walks in interesting places in Moscow

The site is an interactive map of Moscow, which displays types of outdoor activities with detailed descriptions and comments.
The published version of the site can be viewed at [https://svg40.pythonanywhere.com](https:/svg40.pythonanywhere.com)

## Run

You will need Python 3 to run the site.

Download the code from GitHub. Install dependencies:

```sh
pip install -r requirements.txt
```

Create a SQLite database

```sh
python3 manage.py migrate
```

Start the development server

```
python3 manage.py runserver
```

### Filling with content from an existing file:
  - create a file in *.json format

<i>example of compiling *.json file:</i>
```json
{
     "title": "Location name",
     "imgs": [
         "https://link_to_image1/image.jpg",
         "https://link_to_image2/image.jpg"
     ],
     "description_short": "Short description of the place",
     "description_long": "<p>Long description, tagged</p>",
     coordinates: {
         "lng": "37.797137", longitude
         "lat": "55.480924" latitude
     }
}
```
  - upload it online on [Github](https://github.com)
  - enter a command with a link to the file
```
python manage.py load_place https://raw.githubusercontent.com/link/filename.json
```

<i>Execution example:</i>
```
(PRG) C:\....>python manage.py load_place https://filename.json
WARNING:root:Created new object 'ObjectName'
WARNING:root:Images loaded
```
## Environment variables

Part of the project settings is taken from the environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`.
