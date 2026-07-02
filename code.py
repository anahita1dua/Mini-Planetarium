import customtkinter as ctk
import pandas as pd
from geopy.geocoders import Nominatim #used for finding coordinates
from skyfield.api import Topos, load
from skyfield.api import hipparcos 
import matplotlib.pyplot as plt
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")