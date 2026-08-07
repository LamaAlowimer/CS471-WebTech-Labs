# Django Forms (Part 2) (Lab 11): 

**Student Name:** لمى العويمر 
**Student ID:** 432205254
**Course:** Web Technologies (CS471)  

---
### Task 1 
#### view.py

##### In this part, I wrote the view functions to do the basic operations for the students using Django Forms. It simply allows the website to list, add, update, or delete a student from the database.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/50d5d8d3-5e82-4c66-8323-ed20d1e9904c" />

#### urls.py

##### Here I added the URL paths for Task 1. These lines connect the website's links to the view functions, allowing us to list, add, edit, and delete students.

<img width="500"  alt="image" src="https://github.com/user-attachments/assets/827727f3-3e70-4a93-80d2-d0c4c1e444db" />

#### HTML files

##### Here I built the front-end page to show the list of students. It uses a loop to display their names and addresses, and includes action buttons to easily manage (edit or delete) each record.

<img width="560" alt="image" src="https://github.com/user-attachments/assets/63e4334d-bc75-4818-ac6c-b734b3c1dd7f" />

---

### Task 2

#### view.py

##### Here I implemented the Many-to-Many relationship and wrote these view functions to handle listing, adding, editing, and deleting students, allowing each student to be associated with multiple addresses using the updated Django forms.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b4aff605-6e79-4dc7-95df-680dd0210138" />

#### urls.py
##### Here I added the URL paths for Task 2. These lines connect the website's links to the new view functions, allowing us to list, add, edit, and delete students along with their multiple addresses.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/bf37a5bb-4632-472a-8a19-9e2178989b47" />

#### HTML files
##### Here I built the front-end page to show the list of students for Task 2. It uses a main loop to display their names, and an inner loop to list all the addresses linked to them, plus the action buttons to easily edit or delete each record.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/07801be4-f564-47b4-a74a-36c32d92d939" />

##### This is for both Task 1,2

##### Here I built the front-end form page. It uses a POST method with a security token to safely send data, and dynamically displays the input fields so users can easily add a new student or update an existing one.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/093891f3-e9c4-4745-b59c-899e2fd61ff9" />

---

### Task 3:
##### Here, I updated the settings to allow users to upload images. This code simply tells the project which folder to save the pictures in, and creates a link so they can show up on the website

<img width="500" alt="image" src="https://github.com/user-attachments/assets/50377d80-0300-4f6c-a618-858b98b664ea" />

#### Here, I configured the required URLs for handling images. While the top paths link to the profile functions, the bottom code specifically allows the web server to access and show the pictures we uploaded into the 'media' folder.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/ea2056e5-0ddc-470f-846c-3e81e38da0d6" />

<img width="500" alt="image" src="https://github.com/user-attachments/assets/e37ad9f3-8cd5-4cc8-ab9f-0002fbe05e37" />

##### Here I built the front-end page for the Profile Gallery. It uses a loop to create a table showing each user's ID, name, and their uploaded profile picture. It also includes an 'Add Profile' button at the top to easily insert new records.

<img width="600" alt="image" src="https://github.com/user-attachments/assets/e43e121b-023f-47cd-b1fb-62313be3d906" />

##### Here is the final output of our implementation. It shows a clear interface that lists each user's ID, name, and uploaded picture, confirming that both the back-end logic and the front-end design are fully functional.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/ff8b044b-c1b7-4685-a533-461cf57661cf" />

















