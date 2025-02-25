# APT-API

### Technologies

 - Flask
 - MongoDB
 - Docker

### What's this API ?

This API is a **school project** API that has 2 functionalities:

 - Encoding images into APT data
 - Decoding APT data into images

**Note that this API is nothing serious.**

I implemented my own token in order to try to avoid abuse when I make this public for my project.
Some of the code is not that well written so really don't hesitate to open an issue or to fork this project !

### Running the app

#### Running from source

The app uses poetry for library management.

Make sure you have poetry installed on your system, then install the required libraries.

```
poetry install
```

Then, set up the enviornment variable containing the mongodb URI string

On linux and Mac OS :

```
export mongo_connection_string="mongodb://your_host:your_port"
```

After that, run the flask app using poetry

```
poetry run python run.py
```


#### Running using docker

..


#### Usage

#### Generate token

**Make sure you set the environment variable before**

```
poetry run python create_token.py
```

Use the created token in your requests.


##### Encoding

```
 curl -X POST "http://localhost:1337/encode" \
     -H "Content-Type: multipart/form-data" \
     -F "image_1=@/your/path/for/image/one" \
     -F "image_2=@/optional/path/for/image/two" \
     -F "token=your_token" \
     -o ./your_wav_filename.wav
```

The output will be saved to a wav file.

**Note that it takes ~2 minutes depending on the image you're loading for the API to generate the audio data**
**If you see that the request finished right after sending the request that means something went wrong. Do a curl without the -o flag to see the status**


##### Decoding