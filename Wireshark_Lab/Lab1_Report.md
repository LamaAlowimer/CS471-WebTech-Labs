# Lab Report 1: 

**Student Name:** لمى العويمر 
**Student ID:** 432205254
**Course:** Web Technologies (CS471)  

---

## Part 1: Capturing HTTP Traffic

### 1. HTTP Capture Screenshot:
1-HTTP packet to view its details.
<img width="1457" height="272" alt="image" src="https://github.com/user-attachments/assets/b0a9faa4-9c57-4bac-a008-6a8ec760ce73" />
these are its details:
<img width="1508" height="875" alt="image" src="https://github.com/user-attachments/assets/67074e90-ff66-4316-872c-3ec74a0cc39e" />
What I observed From the captured packets:
 there is mulitiple GET and it's becuse each peace of the web page needs it's own GET follwoed by 200 OK which indicates that the it was successful, like in this picture the browser (client) asked the server for the HTML text wich is the page in general but it was removed to a deffernet location so it responded with 301 then it requested another GET and it was succsesful <img width="1331" height="120" alt="image" src="https://github.com/user-attachments/assets/13d2fb91-d54c-4f79-8805-97fb27b433ec" />
after it asked for the icon that appers next to the title of the web page then it responsed with PNG the picture of it <img width="1352" height="47" alt="image" src="https://github.com/user-attachments/assets/8edb0011-aa5c-4d16-b648-0cd00eb2da23" />
<img width="530" height="141" alt="image" src="https://github.com/user-attachments/assets/6a8280c8-cc99-4d14-a5c6-a2fa962c5883" />

### 2. Packet Analysis:
* **Request Method:** GET
* **Requested URL:** /online
* <img width="461" height="76" alt="image" src="https://github.com/user-attachments/assets/f5276b10-22f9-4184-a95b-53110e30b21e" />

* **Response Code:** 301
* <img width="518" height="86" alt="image" src="https://github.com/user-attachments/assets/2a73ed50-fad9-41c1-8dff-8b3d696cdbbf" />
---

## Part 2: TCP/IP Traffic
**in this picture we can see the conversation between the client &  the server.
<img width="1280" height="1079" alt="image" src="https://github.com/user-attachments/assets/adf62dce-8a7b-40db-b4e3-a83235a80d89" />



### 1. TCP Three-Way Handshake:
<img width="1754" height="155" alt="image" src="https://github.com/user-attachments/assets/2164ef27-733d-4c96-9f7f-ffa84e87c96b" />
### TCP data packets exchanged between the client and server
<img width="1801" height="123" alt="image" src="https://github.com/user-attachments/assets/3e6b563e-39c8-46e2-ae75-c888087690a7" />
### TCP termination process (FIN, ACK packets):
<img width="1853" height="933" alt="image" src="https://github.com/user-attachments/assets/3fe5231d-89ef-41ee-9bfd-b76996164a13" />

---

## Part 3: Capturing and Analyzing UDP Traffic

### 1. UDP Packets Capture Screenshot:
<img width="1900" height="914" alt="image" src="https://github.com/user-attachments/assets/6400f3cf-725c-4512-94d5-1b4d52da2c4e" />


### 2. UDP Packet Details:
* **Source Port,Destination Port,Length:** <img width="889" height="191" alt="image" src="https://github.com/user-attachments/assets/7963c9fa-fed9-47d4-9a6b-b986800b8b27" />

* **Data:** <img width="1909" height="417" alt="image" src="https://github.com/user-attachments/assets/20074136-ea34-4d5b-a020-cec2079650ea" />
---
## Part 4: Comparing TCP and UDP

### 1: Reliability and Integrity

| Criteria | Protocol | Reasons |
| :--- | :--- | :--- |
| **Reliability & Connection** | TCP | Uses a three-way handshake and acknowledgments to ensure delivery. |
| **Data Integrity & Ordering** | TCP | Uses sequence numbers to reassemble packets in the correct order. |

### 2: Use Cases and Performance

| Criteria | TCP | UDP |
| :--- | :--- | :--- |
| **Use Cases** | Web browsing (HTTP/HTTPS), Email, File transfer. | Streaming media, VoIP, Online gaming (real-time). |
| **Performance** | Slower due to overhead and error checking. | Faster as it lacks connection setup and error correction. |
