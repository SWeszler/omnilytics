# Omnilytics Programming Challenge

Write a Web app using React.js to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.
Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....

 The output should be 2MB in size. Once file generation is done the output should be available as a link which can be then downloaded by clicking on it. Also, there should be a button on the page so by clicking on this button the total number of each random object will be displayed.

Note: The backend API must be written using Flask (Python) or Express frameworks. All the communication between frontend and backend MUST be done via these APIs only.


## Dovelopment environment:
- run Flask API on port 8000
- run ReactJS server with NodeJS container on port 9000

## Getting Started
- first time run:
docker-compose up --build
once docker image is built, you only need:
docker-compose up
to start containers
- run front-end app:
attach nodejs container:
go to project folder:
cd client/omnilytics
execute:
yarn start


