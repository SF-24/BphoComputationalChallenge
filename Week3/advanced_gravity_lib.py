import advanced_gravitational_motion_example as asi
AU = 149597900000.0

# Create the objects
asi.create_object(1988475000000000000000000000000, 0, 0, 500, 0, 0.2, "red")
asi.create_object(198847500000000000000000000000, 2.0*AU, 1.0*AU, -10000, -1000, 0.1, "blue")
asi.create_object(198847500000000000000000000000, -2.0*AU, 1.0*AU, 10000, 100, 0.1, "green")

# Simulate the motion and render it
asi.simulate()
asi.render()
