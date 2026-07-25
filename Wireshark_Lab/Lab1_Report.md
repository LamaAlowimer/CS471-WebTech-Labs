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

## Part 2: Analyzing TCP/IP Traffic
**in this picture we can see the conversation between the client &  the server.
<img width="1021" height="668" alt="image" src="https://github.com/user-attachments/assets/5ace30bc-ccf8-4187-bf0f-28bb877ee707" />


### 1. TCP Three-Way Handshake:
<img width="1812" height="142" alt="image" src="https://github.com/user-attachments/assets/7f834580-d531-466e-a8db-643c78d5eede" />



### 2. Sequence & Acknowledgment Numbers:
* **Sequence Number (Seq):** 
* **Acknowledgment Number (Ack):**

### 3. TCP Termination (FIN, ACK):

---

## Part 3: Capturing and Analyzing UDP Traffic

### 1. UDP Packets Capture Screenshot:


### 2. UDP Packet Details:
* **Source Port:** 
* **Destination Port:** 
* **Length:** 

---

## Part 4: Comparing TCP and UDP

### Table 1: Reliability and Integrity

| Criteria | Protocol | Reasons |
| :--- | :--- | :--- |
| **Reliability & Connection** | TCP | Uses a three-way handshake and acknowledgments to ensure delivery. |
| **Data Integrity & Ordering** | TCP | Uses sequence numbers to reassemble packets in the correct order. |

### Table 2: Use Cases and Performance

| Criteria | TCP | UDP |
| :--- | :--- | :--- |
| **Use Cases** | Web browsing (HTTP/HTTPS), Email, File transfer. | Streaming media, VoIP, Online gaming (real-time). |
| **Performance** | Slower due to overhead and error checking. | Faster as it lacks connection setup and error correction. |
