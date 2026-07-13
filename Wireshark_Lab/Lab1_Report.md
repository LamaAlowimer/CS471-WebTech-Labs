# Lab Report 1: 

**Student Name:** لمى العويمر 
**Student ID:** 432205254
**Course:** Web Technologies (CS471)  

---

## Part 1: Capturing HTTP Traffic

### 1. HTTP Packets Capture Screenshot:
<img width="925" height="487" alt="image" src="https://github.com/user-attachments/assets/5bb4cfa3-0c34-4c67-8ce0-a4b6fe591de6" />


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
