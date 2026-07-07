import pandas as pd
from geopy.geocoders import Nominatim #used for finding coordinates
from skyfield.api import Topos, load
from skyfield.data import hipparcos 
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datetime import datetime
from PIL import Image
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MiniPlanetarium:
	def __init__(self,root):
		self.root=root
		self.root.title("Mini Planetarium")
		self.root.geometry("600x650")
		self.root.resizable(False, False) #in order to fix the window size
		#setting up the bg

		from PIL import Image
		img=Image.open(r"galaxy.png")		
		bg_image=ctk.CTkImage(
			light_image=img,
			dark_image=img,
			size=(600, 700)
			)
		self.bg_label=ctk.CTkLabel(root, image=bg_image, text="")
		self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
		
		self.geolocator=Nominatim(user_agent="mini_planetarium")
		self.ts=load.timescale() #To convert to standard times
		with load.open(hipparcos.URL) as f:
			self.stars_df=hipparcos.load_dataframe(f)
		
		self.main_frame=ctk.CTkFrame(root, corner_radius=20, fg_color="#1A1A24", width=450, height=550)
		self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
		self.title_label=ctk.CTkLabel(self.main_frame, text="Mini Planetarium", font=("Times New Roman", 26, "bold"), text_color="#E0E1DD")
		self.title_label.pack(pady=(100, 70))
		
		#Date entry box		
		self.date_entry=ctk.CTkEntry(self.main_frame, placeholder_text="Enter Date (DD/MM/YYYY)", width=320, height=40)
		self.date_entry.pack(pady=10)
		#Time entry box
		self.time_entry=ctk.CTkEntry(self.main_frame, placeholder_text="Enter the time (hh:mm)(24hr format)", width=320, height=40)
		self.time_entry.pack(pady=10)
		#City entry box
		self.city_entry=ctk.CTkEntry(self.main_frame, placeholder_text="Enter city name", width=320, height=40)
		self.city_entry.pack(pady=10)
		#Sky type
		self.pollution_label=ctk.CTkLabel(self.main_frame, text="Select light pollution/sky type:", font=("Arial", 12), text_color="#b1dede")
		self.pollution_label.pack(pady=(15,2))
		self.pollution_dropdown=ctk.CTkOptionMenu(self.main_frame, values=["Low (Dark Sky)", "High(City Sky)"], width=320, height=35, fg_color="#1F1F2E", button_color="#3D3D5C")
		self.pollution_dropdown.pack(pady=5)
		#Generate Button
		self.generate_btn=ctk.CTkButton(self.main_frame, text="Generate Sky Map", command=self.generate_sky_map, width=220, height=45, font=("Times New Roman", 15, "bold"), fg_color="#4A4AEA", hover_color="#3535B3")
		self.generate_btn.pack(pady=30)
		
		
		#Working of the button
		self.status_label=ctk.CTkLabel(self.main_frame, text="",font=("Arial", 12),text_color="yellow", fg_color="transparent")
		self.status_label.pack(pady=5)
		
	def generate_sky_map(self):
		city=self.city_entry.get().strip()
		date_str=self.date_entry.get().strip()
		time_str=self.time_entry.get().strip()
		pollution=self.pollution_dropdown.get()
		if not city or not date_str or not time_str or not pollution:
			self.status_label.configure(text="Please fill all the fields!", text_color="red")
			return
		
		self.status_label.configure(text="Finding Coordinates & Fetching Stars.....", text_color="yellow")
		self.root.update_idletasks()
		self.root.update()
		
		
		try: #using this so that app doesn't crash in case of some errors
			#location coordinates
			location=self.geolocator.geocode(city, exactly_one=True)
			if not location:
				self.status_label.configure(text="City not found! Try a major city.", text_color="red")
				return
			lat, lon=location.latitude, location.longitude
			
			#date/time
			dt=datetime.strptime(date_str+' '+time_str, '%d/%m/%Y %H:%M')
			t=self.ts.utc(dt.year, dt.month, dt.day, dt.hour, dt.minute)
			
			#Setting up magnitude for visibility
			mag_limit=6.0 if "Low (Dark Sky)" in pollution else 3.0
			visible_stars=self.stars_df[self.stars_df["magnitude"]<=10.0]
			
			#Making the sky map
			fig, ax=plt.subplots(figsize=(8,8),facecolor="#0B132B")
			ax.set_facecolor("#0B132B")
			ax.scatter(visible_stars["ra_hours"], visible_stars["dec_degrees"], s=(mag_limit-visible_stars['magnitude'])*4 or (visible_stars['magnitude']-mag_limit)*4, color="white", alpha=0.9 , picker=5) #alpha=0.9 so that it looks somewhat translucent and equivalent to real star
			ax.set_title("Sky Map above "+city.capitalize()+"\n Date: "+date_str+"\n Time: "+time_str, color="white", fontsize=14)
			ax.axis("off") #essential so that we do not get the numbers of the graph in our sky map
			
			def on_pick(event):
				ind=event.ind[0]#tells the star number which user has clicked
				star_data=visible_stars.iloc[ind]
				star_mag=star_data['magnitude']
				visibility="Visible to naked eye" if star_mag<=mag_limit else "Needs Telescope"
				detail_msg="Star ID: "+ str(star_data.name)+ "\n Magnitude: "+str(star_mag)+"\n"+visibility
				
						
				plt.gca().text(star_data["ra_hours"], star_data["dec_degrees"], detail_msg, color="cyan", fontsize=10)
				fig.canvas.draw_idle()#so that it works without lagging
				
			
			fig.canvas.mpl_connect("pick_event", on_pick)

            # Try Again button
			button_ax = plt.axes([0.75, 0.02, 0.15, 0.05])
			retry_button = Button(button_ax, 'Try Again')

			def retry(event):
				plt.close(fig)

			self.date_entry.delete(0, "end")
			self.time_entry.delete(0, "end")
			self.city_entry.delete(0, "end")

			self.status_label.configure(text="Enter new details and generate again.", text_color="cyan")

			retry_button.on_clicked(retry)

			
			self.status_label.configure(text="Sky Map Generated!", text_color="green")
			plt.show()
			
		except Exception as e:
			if 'getaddrinfo failed':
				self.status_label.configure(text="Check internet connection")
			else: 
				self.status_label.configure(text="ERROR: Check date/time format!", text_color="red")
			
			print (e)

			
			
if __name__=="__main__":
	app=ctk.CTk()
	main_app= MiniPlanetarium(app)
	app.mainloop()

#end 
