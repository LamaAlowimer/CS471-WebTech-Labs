# Lab Report 1: Protocol Analysis with Wireshark

**Student Name:** لمى العويمر 
**Student ID:** 432205254
**Course:** Web Technologies (CS471)  

---

## Part 1: Capturing HTTP Traffic

### 1. HTTP Packets Capture Screenshot:
!(image_771a3a.png)

### 2. Packet Analysis:
* **Request Method:** GET
* **Requested URL:** /online
* **Response Code:** 301

---

## Part 2: Analyzing TCP/IP Traffic

### 1. TCP Three-Way Handshake:
* **SYN Packet:** [ضعي هنا اسم صورة الـ SYN]
* **SYN-ACK Packet:** [ضعي هنا اسم صورة الـ SYN-ACK]
* **ACK Packet:** [ضعي هنا اسم صورة الـ ACK]

### 2. Sequence & Acknowledgment Numbers:
* **Sequence Number (Seq):** [أدخلي الرقم الموجود في Wireshark]
* **Acknowledgment Number (Ack):** [أدخلي الرقم الموجود في Wireshark]

### 3. TCP Termination (FIN, ACK):
*(ضعي هنا اسم صورة الـ FIN/ACK)*

---

## Part 3: Capturing and Analyzing UDP Traffic

### 1. UDP Packets Capture Screenshot:
*(ضعي هنا اسم صورة الـ UDP)*

### 2. UDP Packet Details:
* **Source Port:** [أدخلي المنفذ]
* **Destination Port:** [أدخلي المنفذ]
* **Length:** [أدخلي الطول]

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