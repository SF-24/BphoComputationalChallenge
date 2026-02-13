import advanced_gravity_lib as asi
AU = 149597900000.0
solar_mass=1988475000000000000000000000000

# Create the objects. You can add as many as you want,
# However, the more objects you have, the more resources it will require to run.
asi.create_object(solar_mass, 0, 0, 500, 0, 0.2, "red")
asi.create_object(solar_mass/10, 2.0*AU, 1.0*AU, -10000, -1000, 0.1, "blue")
asi.create_object(solar_mass/10, -2.0*AU, 1.0*AU, 10000, 100, 0.1, "green")
asi.create_object(solar_mass/100, 0, -1.0*AU, 120, 1000, 0.1, "orange")

# Simulate the motion and render it
asi.simulate()
asi.render()
asi.export(filename="gravity")
