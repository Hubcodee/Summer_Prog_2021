# Video Stream - using TCP

### --> Python packages requirement
`numpy`
`socket`
`cv2`

## TCP socket architecture

![TCP architecture](https://www.tutorialspoint.com/unix_sockets/images/socket_client_server.gif)

## Server and Client architecture for sending and recieving video stream 
### We need to firstly convert the capture frame into bytes (as frame is numpy array thus, we use numpy method `.tobytes()` )
### After this at client side , again we need to convert bytes to numpy array thus , we can use method `numpy.frombuffer()`

![SENDING VIDEO STREAM OVER NETWROK](https://pyimagesearch.com/wp-content/uploads/2019/04/imagezmq_client_server.png)

### PROGRESS
- [x] Trasnferring videos
- [x] Video lag handling
- [x] Buffer handling
- [ ] Error Handling 
- [ ] Public IP stream

