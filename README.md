# I. Project Overview
ReadForChange: A system for supporting environmental causes through reading and donation. Users engage with articles about sustainability, with a portion of the reading fee automatically donated to global environmental projects. By reading, users contribute to a cleaner, greener future while learning about the importance of environmental action. This system is built using Python and Tkinter. 

# II. Python Concepts, Libraries
 **Function:** 

- Functions in this project serve as reusable blocks of code that perform specific tasks like handling user input, processing donations, or updating progress trackers.

**Tkinter:**

- Tkinter was used for the graphical user interface (GUI), creating an intuitive interface with buttons, labels, and forms for navigating the platform. The Treeview widget is used to display data such as login history and donor lists.

**Tkinter Entry:**

- The username_entry and password_entry fields are used to capture user input (username and password) on the login screen. The Entry widget is employed to create these fields, where users type their credentials.

**Messagebox:**

- messagebox.showerror() handles errors (e.g., invalid login), while messagebox.showinfo() provides feedback after a successful login or registration.

**Article Browsing and Donations**
- Tkinter Button: The create_button() function dynamically generates buttons for each article, allowing users to browse the content.
- Donation Processing: After reading, users are prompted to donate. The process_donation() function updates the total donations and the user's individual donations.
- Messagebox: After a donation, messagebox.showinfo() thanks users for their contribution
- Error Handling: Error handling was implemented to ensure the program operates smoothly even when issues arise. It uses try and except blocks to catch runtime errors and notify the user when something goes wrong (invalid input).

**Donation Tracker and Donor List**
- Tkinter Treeview: The ttk.Treeview() widget displays the login history and donor list in tabular form, showing usernames and their donation details.
- Process: The show_donor_list() function populates the Treeview with data from the self.donors dictionary.

**Goal Tracker**
- Tkinter Labels: Donation progress is displayed with tk.Label() widgets, showing the goal and current total donations.
Conditional Message: A congratulatory message appears when the donation goal is reached, displayed through another Label widget.

**Dashboard and Navigation**
- Tkinter Buttons: Dynamic navigation buttons allow users to easily access different sections of the platform, such as articles, goal tracker, login history, and donor list.
Logout Process
- Logout: The logout() method resets the logged-in user and brings the user back to the login screen via setup_login_screen().

**Libraries Used**
- PIL (Pillow): Enhances visual elements like background images.
- Image.open(): Opens images.
- ImageTk.PhotoImage(): Converts image to Tkinter-compatible format.
- Image.resize(): Resizes images to fit the window.
- datetime: Tracks and displays timestamps for logins and donations using datetime.now(). This helps maintain accurate logs of user activities.
  
# III. SDG and Its Integration into the Project
**SDG 4 - Quality Education:**
- The system acts as an educational tool by providing accessible and engaging content on environmental issues. Users not only learn about sustainability challenges but are also  encouraged to take action, thus supporting a culture of sustainability and environmental stewardship. The platform promotes lifelong learning about environmental topics.

**SDG 8 - Decent Work and Economic Growth:**
- The system promotes economic growth by supporting sustainability initiatives that create green jobs and economic opportunities. Through its educational content and donation  mechanism,  ReadForChange encourages investments in projects that drive sustainable economic development and provide decent work opportunities in the green economy. By raising  awareness about environmental challenges and solutions, the app contributes to the creation of a green job market.

**SDG 13 - Climate Action:**
- By promoting articles that educate users on issues like deforestation, ocean pollution, and clean energy, the app raises awareness and fosters action against climate change. This aligns with the goal of reducing greenhouse gas emissions and encouraging climate-positive actions.

**SDG 14 - Life Below Water:**
- The system promotes the preservation of oceans, seas, and marine resources by offering articles that educate users on ocean pollution, coral reef conservation, and marine biodiversity. Through this content, ReadForChange helps raise awareness about the threats to marine ecosystems and advocates for sustainable practices to protect life below water.

**SDG 17 - Partnerships for the Goals:**
- The system connects individuals to broader environmental causes by facilitating donations. By linking users’ contributions to real-world outcomes, it fosters collaboration and community action. This partnership aspect promotes cooperation among individuals and organizations working toward common environmental goals.


# IV. Instructions for Running the Program
Steps:
1.Download the ReadForChange Files.zip.

2.Extract the ReadForChange Files.zip.
- It should contain the following files:
- ReadForChange.py
- README.md
- ReadForChange.png (for background images)

3.Ensure you have Python installed on your machine. You can download it.

4. Install the required libraries for the program. You can do this via pip:
- pip install pillow
- pip install tkinter

5.Open the ReadForChange.py file in your favorite text editor or IDE, such as Visual Studio Code.

6. Run the program:
- In Visual Studio Code, you can run the program by pressing Ctrl + Alt + N or use the terminal with the command:
