"""
Pipe pressure drop calculator
By: Alex Kalmbach.
Date: 11/03/2024
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
from typing import Any

from properties import density_data, viscosity_data, get_property
from fluid_dynamic_equations import darcy_weisbach, colebrook_white_solver_fsolve, reynolds_num
from math import pi

COPPER_EPSILON = 0.00006  # Roughness for copper. Default: 0.00006
STEEL_EPSILON = 0.0017  # Roughness for steel. Default: 0.0017 seems to work well.

# Library of inner diameters based on type L copper and schedule 40 steel nominal sizes
copper_pipe_sizes = {0.5: 0.545, 0.75: 0.785, 1: 1.025, 1.25: 1.265,
                     1.5: 1.505, 2: 1.985, 2.5: 2.465, 3: 2.945, 4: 3.905, 5: 4.875, 6: 5.845}

steel_pipe_sizes = {0.5: 0.62, 0.75: 0.82, 1: 1.05, 1.25: 1.38,
                    1.5: 1.61, 2: 2.07, 2.5: 2.47, 3: 3.07, 4: 4.03, 5: 5.05, 6: 6.07}

# Valid temperatures and glycol percentages from data
valid_temps = sorted({entry["temperature"] for entry in density_data})
valid_glycols = ["0", "30", "40", "50"]

def calculate_pressure_drop():
    "Calcs pressure drop based on pipe type, fluid type, and flow"
    try:
        # Retrieve values from the dropdowns and inputs
        pipe_type = pipe_type_var.get()
        pipe_diam_choice = float(pipe_size_var.get())
        gpm = float(gpm_entry.get())
        fluid_temp = int(temp_var.get())
        prop_glycol = int(glycol_var.get())
        pipe_length = 100  # Default to 100 ft

        # Set pipe properties based on selected pipe type
        if pipe_type == "copper":
            pipe_inner_diam = copper_pipe_sizes[pipe_diam_choice]
            epsilon = COPPER_EPSILON
        elif pipe_type == "steel":
            pipe_inner_diam = steel_pipe_sizes[pipe_diam_choice]
            epsilon = STEEL_EPSILON
        else:
            messagebox.showerror("Error", "Invalid pipe type selected.")
            return

        # Retrieve fluid properties
        visc_centipoise = get_property(data=viscosity_data, temperature=fluid_temp, glycol_percentage=prop_glycol)
        fluid_dyn_visc = visc_centipoise * 0.000671969  # Convert centipoise to lbm/ft*s
        fluid_density = get_property(data=density_data, temperature=fluid_temp, glycol_percentage=prop_glycol)

        # Calculations
        pipe_area = (pi * (pipe_inner_diam / 12) ** 2) / 4  # Area in ft^2
        fluid_velocity = (0.4084 * gpm) / (pipe_inner_diam ** 2)  # Velocity in ft/s
        reynolds: float | Any = reynolds_num(density=fluid_density, velocity=fluid_velocity, diam=pipe_inner_diam, visc=fluid_dyn_visc)
        #Laminar flow condition. See Moody Chart.
        if reynolds < 2000:
            friction_factor = 64/reynolds
        else:
            friction_factor = colebrook_white_solver_fsolve(re=reynolds, epsilon=epsilon, diam=pipe_inner_diam)

        relative_roughness = round(epsilon / pipe_inner_diam, 4)
        pressure_drop = darcy_weisbach(f=friction_factor, length=pipe_length, velocity=fluid_velocity, diam=pipe_inner_diam)

        # Display the result in a message box
        messagebox.showinfo("Results",
                            f"Fluid velocity: {round(fluid_velocity, 2)} ft/s\n"
                            f"Reynolds number: {round(reynolds)}\n"
                            f"Friction factor: {friction_factor}\n"
                            f"Relative roughness: {relative_roughness}\n"
                            f"Pressure drop: {pressure_drop} ft of head per 100 feet of pipe.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Pipe Pressure Drop Calculator")
root.geometry("400x500")
root.configure(bg="#1E1E1E")

# Title Label with Cool Font
title_font = font.Font(family="Helvetica", size=18, weight="bold")
title_label = tk.Label(root, text="Pipe Pressure Drop Calculator", font=title_font, fg="#FFD700", bg="#1E1E1E")
title_label.pack(pady=20)

# Pipe Type Dropdown
pipe_type_var = tk.StringVar()
pipe_type_label = tk.Label(root, text="Pipe Type:", fg="white", bg="#1E1E1E")
pipe_type_label.pack(pady=5)
pipe_type_dropdown = ttk.Combobox(root, textvariable=pipe_type_var, values=["copper", "steel"])
pipe_type_dropdown.pack()

# Pipe Size Dropdown
pipe_size_var = tk.StringVar()
pipe_size_label = tk.Label(root, text="Pipe Size (inches):", fg="white", bg="#1E1E1E")
pipe_size_label.pack(pady=5)
pipe_size_dropdown = ttk.Combobox(root, textvariable=pipe_size_var, values=list(copper_pipe_sizes.keys()))
pipe_size_dropdown.pack()

# GPM Entry
gpm_label = tk.Label(root, text="Flow Rate (GPM):", fg="white", bg="#1E1E1E")
gpm_label.pack(pady=5)
gpm_entry = ttk.Entry(root)
gpm_entry.pack()

# Temperature Dropdown
temp_var = tk.StringVar()
temp_label = tk.Label(root, text="Fluid Temperature (°F):", fg="white", bg="#1E1E1E")
temp_label.pack(pady=5)
temp_dropdown = ttk.Combobox(root, textvariable=temp_var, values=valid_temps)
temp_dropdown.pack()

# Glycol Percentage Dropdown
glycol_var = tk.StringVar()
glycol_label = tk.Label(root, text="Propylene Glycol Percentage:", fg="white", bg="#1E1E1E")
glycol_label.pack(pady=5)
glycol_dropdown = ttk.Combobox(root, textvariable=glycol_var, values=valid_glycols)
glycol_dropdown.pack()

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Pressure Drop", command=calculate_pressure_drop)
calculate_button.pack(pady=20)

# Add a style for button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10, "bold"), foreground="black", background="black")
calculate_button.configure(style="TButton")

root.mainloop()
