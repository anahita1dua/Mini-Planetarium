import customtkinter as ctk
from PIL import Image
import random

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CosmicAtlasApp(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Cosmic Atlas")
		self.geometry("900x700")
		self.planets_data={
			"Mercury":{"radius": "2,439.7 km", "moons": "0", "dist": "46 million km-70 million km", "period":"87.969 Earth days", "fact":"Days (176 earth days) are longer than years."},
			"Venus":{"radius": "6,051.8 km", "moons": "0", "dist": "108 million km-109 million km", "period":"224.701 Earth days", "fact":"It spins backward and days (243 earth days are longer than year. It is also the brightest object in night sky after sun and moon"},
			"Earth":{"radius": "6,371.0 km", "moons": "1", "dist": "147 million km-152 million km", "period":"365.256 Earth days", "fact":"It is the only planet not named after a Diety. Its name comes from old English and Germanic words meaning 'ground' or 'soil'"},
			"Mars":{"radius": "3389.5 km", "moons": "2 (Phabos, Deimos)", "dist": "207 million km-249 million km", "period":"686.980 Earth days", "fact":"Its Olympus Mons (the massive shield volcano) is three times taller than Mount Everest"},
			"Jupiter":{"radius": "69,886.0 km", "moons": "95: Galilean moons(4) (large), Inner and Outer moons (91) (small and irregularly shaped)", "dist": "741 million km-817 million km", "period":"4,332.589 Earth days", "fact":"It is the largest planet which though is a failed star (made up of H and He)and it's moon 'Ganymede' is largest moon in the solar system (bigger than the planet Mercury!)"},
			"Saturn":{"radius": "58,232.0 km", "moons": "274 (24 regular and 250 small, irregular)", "dist": "839 million km-934 million km", "period":"10,759.2 Earth days", "fact":"It is the second largest planet, though it can float on water (less dense than water), it's ring is made up of ice, the moon 'Titan' is the only moon to have planet like atmosphere and is larger than Mercury"},
			"Uranus":{"radius": "25,362.0 km", "moons": "28 (5 major+14 inner+9 irregular)", "dist": "2741 million km-3004 million km", "period":"30,687.2 Earth days", "fact":"It is the only planet to spin on its side (it has 42 years of complete light then 42 of complete darkness) and has the coldest atmosphere, it also has 13 sets of faint rings"},
			"Neptune":{"radius": "24,622.2 km", "moons": "16: Triton (largest)+inner and outer", "dist": "4,460 million km-4,537 million km", "period":"60,190.0 Earth days", "fact":"It was discovered using Math, its largest moon 'Triton' is the only large moon with retrogate orbit which means it rotates opposite to Neptune and the gravitational force expirienced here is similar to Earth"}
		}
		self.random_facts=["Mercury: Despite being the closest planet to the Sun, permanently shadowed polar craters contain large deposits of water ice.", "Mercury: Its cooling iron core has caused the planet to shrink by about 14 km in diameter, leaving giant wrinkle-like cliffs across the surface.", "Mercury: A year lasts only 88 Earth days, making it the fastest-orbiting planet in the Solar System.", "Mercury: It has no moons and no ring system.", "Mercury: Temperatures swing dramatically from about 430°C during the day to -180°C at night due to its extremely thin atmosphere.", "Mercury: One solar day (sunrise to sunrise) lasts 176 Earth days—twice as long as its year.", "Mercury: Solar winds create a faint sodium tail that stretches millions of kilometers behind the planet, giving it a comet-like appearance.", "Mercury: The Sun appears more than three times larger in its sky than it does from Earth.", "Mercury: It is the second-densest planet in the Solar System, with an iron core making up roughly 85% of its radius.", "Mercury: The Caloris Basin is one of the largest impact craters in the Solar System, spanning about 1,550 km across.", "Venus: It rotates backward (clockwise), opposite to the rotation direction of most planets.", "Venus: A single rotation takes 243 Earth days, longer than its 225-day year.", "Venus: With surface temperatures around 475°C, it is hotter than Mercury despite being farther from the Sun.", "Venus: It is the brightest planet visible from Earth and is often called the Morning Star or Evening Star.", "Venus: Atmospheric pressure at its surface is about 90 times greater than the Earth", "Venus: Like Mercury, it has no moons and no rings.","Venus: More than 1,600 major volcanoes have been identified on its surface.", "Venus: Scientists believe massive volcanic resurfacing events renewed much of the planet's surface 300–500 million years ago.", "Venus: Although similar to Earth in size and composition, its extreme greenhouse atmosphere makes it completely inhospitable.", "Venus: Winds high in the atmosphere can reach speeds of 360 km/h despite the planet's slow rotation.", "Earth: It is the only planet not named after a Greek or Roman deity.", "Earth: It lies within the Sun's habitable 'Goldilocks Zone', allowing liquid water to exist on its surface.", "Earth: About 70.8% of the planet is covered by water.", "Earth: Rotation causes Earth to bulge at the equator, making it an oblate spheroid rather than a perfect sphere.", "Earth: Its magnetic field shields life from harmful solar radiation and creates the auroras.", "Earth: The planet travels around the Sun at roughly 107,000 km/h.", "Earth: Its atmosphere is composed mainly of nitrogen (78%) and oxygen (21%).", "Earth: It is the only known planet with active plate tectonics.", "Earth: The Moon helps stabilize Earth's axial tilt and drives ocean tides.", "Earth: Around 100 tons of meteoroid material enters the atmosphere every day, mostly burning up as shooting stars.", "Mars: Its reddish color comes from iron oxide, essentially making it a planet covered in rust.","Mars: Olympus Mons is the tallest volcano in the Solar System, standing about 21.9 km high.","Mars: Valles Marineris is one of the largest canyon systems known, stretching thousands of kilometers across the planet.", "Mars: It has two small, irregularly shaped moons named Phobos and Deimos.", "Mars: Phobos is slowly spiraling inward and may eventually crash into Mars or break apart into a ring.", "Mars: Average surface temperatures hover around -62°C.", "Mars: A Martian day, called a sol, lasts 24 hours, 39 minutes, and 35 seconds.", "Mars: Planet-wide dust storms can engulf the entire planet for months.", "Mars: Its atmosphere is about 100 times thinner than Earth's and consists mostly of carbon dioxide.", "Mars: Ancient riverbeds and lake deposits suggest liquid water once flowed across its surface.", "Jupiter: It contains more than twice the mass of all the other planets combined.", "Jupiter: The Great Red Spot is a gigantic storm that has persisted for at least 300 years.", "Jupiter: As a gas giant, it lacks a solid surface.", "Jupiter: It has the shortest day of any planet, rotating once every 9 hours and 56 minutes.", "Jupiter: The planet currently has 95 officially recognized moons.", "Jupiter: Ganymede, its largest moon, is bigger than the planet Mercury.","Jupiter: Io is the most volcanically active world in the Solar System.", "Jupiter: Europa may conceal a vast global ocean beneath its icy crust.", "Jupiter: It possesses a faint ring system made mostly of dust.", "Jupiter: Its immense gravity helps deflect or capture many potentially dangerous comets and asteroids.", "Saturn: It is the least dense planet and would theoretically float in a sufficiently large body of water.", "Saturn: Its rings stretch about 282,000 km wide yet are often only around 10 meters thick.", "Saturn: The rings consist mainly of water ice mixed with rock and dust.", "Saturn: It currently holds the record for the most known moons, with 146 confirmed satellites.", "Saturn: Titan is the only moon known to possess a thick atmosphere and stable surface lakes.", "Saturn: Enceladus ejects massive plumes of water ice from a hidden subsurface ocean.", "Saturn: A persistent hexagon-shaped jet stream surrounds its north pole.", "Saturn: Rapid rotation causes it to be noticeably flattened at the poles.", "Saturn: Every 29.5 years, its rings appear to vanish from Earth's perspective when viewed edge-on.", "Saturn: Winds in its upper atmosphere can exceed 1,800 km/h.", "Uranus: It rotates on its side with an axial tilt of about 98 degrees.", "Uranus: Each pole experiences around 42 years of continuous sunlight followed by 42 years of darkness.", "Uranus: Hydrogen sulfide in its atmosphere would give the planet a rotten-egg smell.", "Uranus: It is classified as an ice giant due to its icy mantle rich in water, ammonia, and methane.", "Uranus: It has the coldest atmospheric temperatures measured in the Solar System, reaching -224°C.", "Uranus: The planet is surrounded by 13 faint rings.", "Uranus: Its moons are named after characters from the works of Shakespeare and Alexander Pope.","Uranus: It was the first planet discovered using a telescope, by William Herschel in 1781.", "Uranus: One orbit around the Sun takes 84 Earth years.", "Uranus: Along with Venus, it is one of only two planets that rotate in a retrograde direction.", "Neptune: It has the fastest winds in the Solar System, reaching speeds of up to 2,100 km/h.", "Neptune: It was discovered through mathematical predictions before being directly observed.", "Neptune: Methane in its atmosphere gives it its striking deep-blue color.", "Neptune: A single year lasts 165 Earth years.", "Neptune: Triton is the only large moon known to orbit opposite its planet's rotation.","Neptune: Triton contains active cryovolcanoes that erupt ice and nitrogen instead of molten rock.","Neptune: Voyager 2 photographed the Great Dark Spot, a massive storm that later disappeared.","Neptune: It possesses five known ring systems.","Neptune: Extreme pressures deep inside the planet may cause carbon to crystallize into diamonds that rain toward its core.","Neptune: Sunlight takes more than four hours to reach Neptune, compared to about eight minutes for Earth."]

		#Applying bg image
		bg_img=Image.open("Galaxy.png")
		self.bg_img=ctk.CTkImage(bg_img, size=(900,700))
		self.bg_label=ctk.CTkLabel(self, image=self.bg_img, text="")
		self.bg_label.place(x=0, y=0, relx=1, rely=1)
		#Setting up frames
		self.home_frame=ctk.CTkFrame(self, fg_color="transparent")
		self.planet_page_frame=ctk.CTkFrame(self, fg_color="transparent")
		self.setup_home_page()
		self.show_home()
	
	#Home Page
	def setup_home_page(self):
		#title
		ctk.CTkLabel(self.home_frame, text="COSMIC ATLAS", font=("Merriweather", 50, "bold"), text_color="white").pack(pady=(20,5))
		ctk.CTkLabel(self.home_frame, text="~Exploring the Solar System.....", font=("Arial", 24, "italic"), text_color="#AAAAAA").pack()
		#bulb
		self.bulb_btn=ctk.CTkButton(self.home_frame, text="💡", width=50, font=("Arial", 30), fg_color="#333333", hover_color="#555555", command=self.open_fact_popup)
		self.bulb_btn.place(relx=0.9, rely=0.05)
		#solar system image
		solar_img=Image.open("solar_system.png")
		self.solar_img=ctk.CTkImage(light_image=solar_img, dark_image=solar_img, size=(600, 300))
		self.system_img=ctk.CTkLabel(self.home_frame, image=self.solar_img, text="", fg_color="#1a1a1a", corner_radius=20)
		self.system_img.pack(pady=40)
		#Planet choice dropdown
		ctk.CTkLabel(self.home_frame, text="Select a planet to know more about it:", font=("Arial", 16)).pack(pady=5)
		self.planet_dropdown=ctk.CTkOptionMenu(self.home_frame, values=["Select", "Mercury", "Venus", "Earth", "Mars", "Jupiter","Saturn", "Uranus", "Neptune"], width=200)
		self.planet_dropdown.pack(pady=10)
		self.planet_dropdown.set("Select")
		self.error_label=ctk.CTkLabel(self.home_frame, text="", text_color="red", font=("Arial", 14, "bold"))
		self.error_label.pack(pady=5)
		#Explore planet button
		ctk.CTkButton(self.home_frame, text="Explore Planet", command=self.check_selection, fg_color="#1f538d").pack(pady=10)
		
	def check_selection(self):
		selected=self.planet_dropdown.get()
		if selected=="Select":
			self.error_label.configure(text="Please select a planet!")
		else:
			self.error_label.configure(text="")
			self.show_planet_page()
				
	#Planet Page
	def show_planet_page(self):
		selected=self.planet_dropdown.get()
		data=self.planets_data[selected]
		for widget in self.planet_page_frame.winfo_children():
			widget.destroy()
		#heading
		ctk.CTkLabel(self.planet_page_frame, text=selected.upper(), font=("Times New Roman", 30, "bold")).pack(pady=20)
		content_frame=ctk.CTkFrame(self.planet_page_frame, fg_color="transparent")
		content_frame.pack(fill="both", expand=True, padx=50)
		#photo
		raw_img=Image.open(f"{selected}.png")
		planet_img=ctk.CTkImage(light_image=raw_img, dark_image=raw_img, size=(300, 300))
		self.planet_img=planet_img
		ctk.CTkLabel(content_frame, image=planet_img , text="", width=300, height=300, fg_color="#333333", corner_radius=15).grid(row=0, column=0, padx=20)
		#data
		stats_text=f"Radius:  {data['radius']} \n\n Moons: {data['moons']} \n\n Distance from the sun: { data['dist']} \n\n Orbital Period: {data['period']} \n\n Fun Fact: {data['fact']}"
		ctk.CTkLabel(content_frame, text=stats_text, font=("Arial", 16), justify="left").grid(row=0, column=1, sticky="nw", padx=20 )
		#try again feature
		self.try_btn=ctk.CTkButton(self.planet_page_frame, text="Try another planet", command=self.show_home, width=120, font=("Arial", 15),  fg_color="#555555")
		self.try_btn.place(relx=0.2, rely=0.9)
		self.home_frame.pack_forget()
		self.planet_page_frame.pack(fill="both", expand=True)
	def show_home(self):
		self.planet_page_frame.pack_forget()
		self.home_frame.pack(fill="both", expand= True)
		
	#random fact (bulb working)
	def open_fact_popup(self):
		popup=ctk.CTkToplevel(self)
		popup.title("Random Space Fact")
		popup.geometry("400x250")
		popup.attributes("-topmost", True)
		popup.update_idletasks()
		x=((popup.winfo_screenwidth()//2)-400//2)
		y=((popup.winfo_screenwidth()//2)-250//2)
		popup.geometry(f"+{x}+{y}")
		ctk.CTkLabel(popup, text="DID YOU KNOW?", font=("Arial", 20, "bold"), text_color="orange").pack(pady=20)
		fact=random.choice(self.random_facts)
		ctk.CTkLabel(popup, text=fact, font=("Times New Roman", 18), wraplength=350).pack(pady=10) #wraplength: so that when the line is over text automatically comes in next line
		
	#closing the popup
		def go_home_and_close():
			popup.destroy()
			self.show_home()
		ctk.CTkButton(popup, text="X (Close and go home)", fg_color="#aa0000", hover_color="#ff0000", command=go_home_and_close).pack(pady=20)
			
if __name__=="__main__":
	app=CosmicAtlasApp()
	app.mainloop()