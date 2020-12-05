# Flask and ReactJS

Web app using Flask and React.js to generate four (4) types of printable random objects and store them in a single file, each object is separated by a ",".  
These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.  
Sample extracted output:

```
hisadfnnasd,126263,assfdgsga12348fas,13123.123, 
lizierdjfklaasf,123192u3kjwekhf,89181811238,122, 
nmarcysfa900jkifh,3.781,2.11,....
```

The output is 2MB in size. Once file generation is done the output is visible as a link which can be then downloaded by clicking on it. Also, there is a button on the page such that by clicking on this button the total number of each random objects will be displayed.


## Dovelopment environment:

- run Flask API on port 5000
- run ReactJS server with NodeJS container on port 3000 [http://localhost:3000](http://localhost:3000)

## Getting Started

Start Docker containers:
```
docker-compose up
```

## Unit Tests

Attach Web container and run:
```
pytest
```


