# CS361

Microservice Communication Contract

file: microservice.py

To request data from the microservice:

 Create a text file named "surpriseme.txt" in the main program's directory, then write the text "random" to surpriseme.txt to trigger the request.

To receive data from the microservice:

 Periodically read the contents of "randomrecipe.txt" after the request in the main program's directory to view the contents of the result of the request, then delete the file "surpriseme.txt"

This microservice constantly monitors a specific text file named "surpriseme.txt" for requests. Once a request is detected, indicated by the keyword "random" within the file, the service sends a request to "themealdb.com" API to retrieve a random recipe. It then writes the obtained recipe data in JSON format to another text file named "randomrecipe.txt". Subsequently, the original request file is removed to signify completion. The service employs a loop to continually check for the existence of the request file and operates indefinitely to handle multiple requests efficiently.

![image](https://github.com/gullot/CS361/assets/114206394/9defcf3f-713a-4229-932f-8219867ecf28)

