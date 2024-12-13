import tkinter as tk           # Import the tkinter library for GUI creation
from tkinter import messagebox # Import messagebox for displaying popup messages
from tkinter import ttk        # Import ttk for advanced widgets like Treeview
from PIL import Image, ImageTk # Import PIL for handling images
from datetime import datetime  # For tracking donation dates

# Define the ReadForChange class for managing the application
class ReadForChange:
    def __init__(self, root):
        self.root = root
        self.root.title("Read for Change")
        self.root.geometry("1400x900")

        self.users = {}  # Store user data {username: password}
        self.logged_in_user = None
        self.total_donations = 0
        self.user_donations = 0
        self.donors = {}  # Store donor information as a dictionary to consolidate donations
        self.login_history = []  # Store login history

        self.donation_goal = 50000  # Define the donation goal

          # Preload articles with content
        self.articles = [
            {
                "title": "Saving the Oceans", "fee": 5, "cause": "Pollution and Overfishing", "content": """
                Our oceans are vast and essential to life on Earth, regulating the climate, providing food, and sustaining ecosystems. However, pollution, overfishing, and climate change are taking a significant toll, endangering marine life and the health of our oceans. If we don't take immediate action, these vital resources could be lost forever.
                
                Plastic pollution is one of the most pressing issues facing our oceans today. Millions of tons of plastic waste end up in the seas each year, killing marine life and disrupting delicate ecosystems. From large oceanic garbage patches to microplastics entering the food chain, the long-term damage is profound and irreversible unless we act.
                
                Overfishing poses another severe threat to marine environments, depleting fish stocks and disrupting the balance of ecosystems. Unsustainable fishing methods, such as trawling, destroy habitats and kill non-target species, while the depletion of fish populations impacts both marine biodiversity and the livelihoods of fishing communities.
                
                Climate change is accelerating ocean degradation, causing rising sea temperatures, ocean acidification, and coral bleaching. These changes have devastating consequences for marine life, particularly coral reefs, which are home to a vast array of species. The threat to our oceans from climate change calls for urgent global efforts to reduce emissions and protect marine habitats.
                
                The health of our oceans is directly tied to the well-being of all life on Earth. By tackling pollution, overfishing, and climate change, we can restore and preserve these invaluable ecosystems for future generations.
                """,
            },
            {
                "title": "Reforesting Our Planet", "fee": 10, "cause": "Deforestation", "content": """
                Forests cover nearly 30% of the Earth's land and play a crucial role in maintaining ecological balance. They provide oxygen, shelter, and food for countless species, yet deforestation continues to threaten these ecosystems at an alarming rate. Reforesting our planet is an essential step in combating climate change and preserving biodiversity.
                
                Forests act as carbon sinks, absorbing large amounts of CO2 from the atmosphere and mitigating the effects of climate change. By planting trees and restoring forests, we can significantly reduce the amount of greenhouse gases in the atmosphere and help reverse the damage caused by deforestation.
                
                Reforestation also contributes to preserving biodiversity by restoring natural habitats for wildlife. Forests are home to millions of species, and through reforestation efforts, we can provide these species with the shelter they need to thrive, ultimately preventing species extinction and enhancing ecosystem resilience.
                
                In addition to environmental benefits, reforestation offers substantial economic advantages. Restoring forests can create jobs in rural areas, support sustainable timber industries, and promote eco-tourism, contributing to a green economy and improving local livelihoods.
                
                Reforesting our planet is a powerful solution to the environmental challenges we face today. By taking action to plant trees, restore ecosystems, and promote sustainable forestry practices, we can safeguard the health of our planet for future generations.
                """
            },
            {
                "title": "Clean Energy Revolution", "fee": 7, "cause": "Environmental Degradation", "content": """
                The transition to clean energy is no longer just an ideal but a necessity for combating climate change. With fossil fuel resources depleting and their harmful effects on the environment becoming undeniable, the clean energy revolution offers a sustainable path forward to meet the world’s growing energy demands.
                
                Solar energy is one of the most abundant and cost-effective forms of renewable energy available today. Harnessing the power of the sun to generate electricity not only reduces our reliance on fossil fuels but also helps to lower carbon emissions and cut energy costs in the long run.
                
                Wind energy is another key player in the clean energy revolution, offering a reliable and clean source of power. Wind farms, both onshore and offshore, generate significant amounts of electricity without the carbon footprint associated with traditional energy sources, making them an essential part of the renewable energy mix.
                
                Innovations in energy storage and grid technology are essential for making renewable energy more reliable and accessible. Improved battery storage systems and smart grid technologies can store excess energy produced by solar and wind farms, ensuring a steady supply of clean energy even when production fluctuates.
                
                The clean energy revolution is transforming the way we power our world, offering a sustainable and eco-friendly alternative to fossil fuels. By embracing solar, wind, and advanced energy storage solutions, we can create a cleaner, more resilient energy system for future generations.
                """
            },
            {
                "title": "Preserving Biodiversity", "fee": 8, "cause": "Climate Change", "content": """
                Biodiversity is the variety of life on Earth, from the smallest microorganisms to the largest animals, and it is essential for the health of ecosystems. However, human activities such as deforestation, pollution, and climate change are pushing species to the brink of extinction, making the preservation of biodiversity more urgent than ever.
                
                Biodiversity plays a crucial role in supporting ecosystem services, such as pollination, soil fertility, and water purification. These services are vital for food production, clean water, and a stable climate, meaning that biodiversity loss threatens both human well-being and the planet’s ecological balance.
                
                Habitat destruction is one of the leading causes of biodiversity loss. As forests, wetlands, and other natural habitats are cleared for agriculture and urbanization, species lose their homes, and ecosystems are disrupted, making it harder for many species to survive.
                
                Conservation efforts, such as establishing protected areas, wildlife corridors, and restoring degraded ecosystems, are critical for maintaining biodiversity. These strategies not only protect endangered species but also help preserve the intricate connections that sustain life on Earth.
                
                Protecting biodiversity is not just about saving individual species; its about safeguarding the ecological systems that sustain life. By prioritizing conservation and habitat protection, we can ensure a rich and resilient natural world for future generations.
                """
            },
            {
                "title": "Sustainable Agriculture", "fee": 6, "cause": "Biodiversity Loss", "content": """
                As the global population continues to grow, the demand for food is rising, putting pressure on agricultural systems to produce more. Sustainable agriculture offers a way to meet these demands while protecting the environment, improving food security, and ensuring the long-term health of the planet’s resources.
                
                Industrial agriculture, with its heavy reliance on chemical pesticides, synthetic fertilizers, and monoculture farming, is degrading soil health and contributing to water pollution. Sustainable farming practices, such as crop rotation and organic farming, improve soil fertility and reduce environmental harm.
                
                Agroecology, which integrates ecological principles into farming, promotes biodiversity and strengthens ecosystems. By using diverse farming methods, agroecology enhances resilience to climate change, reduces reliance on chemical inputs, and fosters more sustainable food systems.
                
                Technological innovations in agriculture, such as precision farming and vertical farming, are revolutionizing food production. These methods optimize resource use, reduce waste, and increase yields, making it possible to grow more food using fewer inputs and less land.
                
                Sustainable agriculture is crucial for feeding the growing global population while ensuring the health of our planet. By adopting eco-friendly farming practices and embracing innovative technologies, we can create a food system that is both productive and sustainable for generations to come.
                """
            }
        ]

         # Background image setup
        self.bg_image = Image.open(r"C:\Users\ADMIN\Desktop\ReadForChange Files\ReadForChange.png")
        self.bg_image = self.bg_image.resize((1400, 900), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.setup_login_screen()
    def set_background(self):
         """Sets the background image for every screen."""
         bg_label = tk.Label(self.root, image=self.bg_photo)
         bg_label.place(relwidth=1, relheight=1)

    def create_button(self, text, command, relx, rely, width=22, color="#007BFF"):
        """Helper function to create a styled button."""
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            width=width,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            relief="raised",
            bd=2,
            activebackground="#0056b3",
        )
        button.place(relx=relx, rely=rely, anchor="center")

    def setup_login_screen(self):
        self.clear_screen()
        self.set_background()

        tk.Label(
            self.root,
            text="Welcome to Read For Change",
            font=("Arial", 24, "bold"),
            bg="white",
        ).place(relx=0.5, rely=0.2, anchor="center")
        tk.Label(
            self.root,
            text="Login or Register to Start Contributing",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.3, anchor="center")

        # Username field
        tk.Label(self.root, text="Username:", font=("Arial", 12), bg="white").place(
            relx=0.4, rely=0.4, anchor="center"
        )
        self.username_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.username_entry.place(relx=0.55, rely=0.4, anchor="center")

        # Password field
        tk.Label(self.root, text="Password:", font=("Arial", 12), bg="white").place(
            relx=0.4, rely=0.5, anchor="center"
        )
        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*", width=30)
        self.password_entry.place(relx=0.55, rely=0.5, anchor="center")

        # Buttons
        self.create_button("Login", self.login_user, relx=0.40, rely=0.6)
        self.create_button("Sign Up", self.signup_user, relx=0.6, rely=0.6)

    def signup_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            if username in self.users:
                messagebox.showerror("Error", "User already exists!")
            else:
                self.users[username] = password
                messagebox.showinfo(
                    "Success", "User created successfully. You can log in now."
                )
        else:
            messagebox.showerror("Error", "Please fill in both fields.")

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            self.user_donations = 0
            self.login_history.append({"username": username, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login credentials.")

    def show_dashboard(self):
  
        self.set_background()

        tk.Label(
            self.root,
            text=f"Welcome, {self.logged_in_user}!",
            font=("Arial", 18, "bold"),
            bg="white",
        ).place(relx=0.5, rely=0.2, anchor="center")
        tk.Label(
            self.root,
            text=f"Total Donations: ${self.total_donations}",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.3, anchor="center")

        #button
        self.create_button("Browse Articles", self.browse_articles, relx=0.5, rely=0.6)
        self.create_button("Goal Tracker", self.show_goal_tracker, relx=0.5, rely=0.4)
        self.create_button("Login History", self.show_login_history, relx=0.5, rely=0.5)
        self.create_button("View Donor List", self.show_donor_list, relx=0.5, rely=0.7)
        self.create_button("Logout", self.logout, relx=0.5, rely=0.8)

    def show_goal_tracker(self):
        self.clear_screen()
        self.set_background()

        tk.Label(
            self.root,
            text=f"Donation Goal: ${self.donation_goal}",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.2, anchor="center")
        tk.Label(
            self.root,
            text=f"Total Donations: ${self.total_donations}",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.3, anchor="center")

        # Show goal status
        if self.total_donations >= self.donation_goal:
            tk.Label(
                self.root,
                text="Congratulations! Goal Achieved!",
                font=("Arial", 16, "bold"),
                fg="green",
                bg="white",
            ).place(relx=0.5, rely=0.4, anchor="center")

        self.create_button("Back", self.show_dashboard, relx=0.5, rely=0.8)

    def show_login_history(self):
        self.clear_screen()
        self.set_background()

        tk.Label(
            self.root, text="Login History", font=("Arial", 16, "bold"), bg="white"
        ).place(relx=0.5, rely=0.1, anchor="center")

        tree = ttk.Treeview(self.root, columns=("Username", "Time"), show="headings", height=10)
        tree.heading("Username", text="Username")
        tree.heading("Time", text="Time")
        tree.place(relx=0.5, rely=0.4, anchor="center")

        for entry in self.login_history:
            tree.insert("", "end", values=(entry["username"], entry["time"]))

        self.create_button("Back", self.show_dashboard, relx=0.5, rely=0.85)

    def browse_articles(self):
        self.clear_screen()
        self.set_background()

        tk.Label(
            self.root, text="Browse Articles", font=("Arial", 16, "bold"), bg="white"
        ).place(relx=0.5, rely=0.2, anchor="center")
        for i, article in enumerate(self.articles):
            self.create_button(
                f"{article['title']} - ${article['fee']}",
                lambda a=article: self.read_article(a),
                relx=0.5,
                rely=0.3 + i * 0.1,
            )

    def read_article(self, article):
        self.clear_screen()
        self.set_background()

        tk.Label(
            self.root, text=article["title"], font=("Arial", 18, "bold"), bg="white"
        ).place(relx=0.5, rely=0.2, anchor="center")
        tk.Label(
            self.root,
            text=f"Cause: {article['cause']}",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.3, anchor="center")
        tk.Label(
            self.root,
            text=f"Fee: ${article['fee']}",
            font=("Arial", 14),
            bg="white",
        ).place(relx=0.5, rely=0.4, anchor="center")
        tk.Label(
            self.root,
            text=article["content"],
            font=("Arial", 12),
            wraplength=1000,
            justify="left",
            bg="white",
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Add a "Finish Article" button
        self.create_button(
            "Finish Article",
            lambda a=article: self.process_donation(a),
            relx=0.5,
            rely=0.85,           
        )
        
    def process_donation(self, article):
        self.total_donations += article["fee"]
        self.user_donations += article["fee"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
     # Consolidate donation info for users
        if self.logged_in_user in self.donors:
            self.donors[self.logged_in_user]['donations'] += article['fee']
        else:
            self.donors[self.logged_in_user] = {'donations': article['fee'], 'date': date}

        messagebox.showinfo(
            "Thank You",
            f"Thank you for supporting {article['title']}! Your contribution of ${article['fee']} has been recorded and directly go to donations. Your Contribution Reduce {article['cause']}",
        )
        
        self.show_dashboard()

        # Add the donation to the donor list
        if self.logged_in_user not in self.donors:
            self.donors[self.logged_in_user] = 0
        self.donors[self.logged_in_user] += article['fee']

        self.show_dashboard()

    def show_donor_list(self):
        self.clear_screen()
        self.set_background()

        tk.Label(self.root, text="Donor List", font=("Arial", 16, "bold"), bg="white").place(
            relx=0.5, rely=0.2, anchor="center"
        )
        tree = ttk.Treeview(self.root, columns=("Username", "Total Donations"), show="headings", height=10)
        tree.heading("Username", text="Username")
        tree.heading("Total Donations", text="Amount Donated")
        tree.place(relx=0.5, rely=0.4, anchor="center")

        for username, amount in self.donors.items():
            tree.insert("", "end", values=(username, amount))

        self.create_button("Back", self.show_dashboard, relx=0.5, rely=0.85)

    def logout(self):
        self.logged_in_user = None
        self.setup_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the application
root = tk.Tk()
app = ReadForChange(root)
root.mainloop()
