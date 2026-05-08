def convert_unit(value, from_unit, to_unit):
    # Conversion factors to meters
    factors = {
        'm': 1.0,
        'cm': 1e-2,
        'mm': 1e-3,
        'um': 1e-6, # micrometers
        'nm': 1e-9  # nanometers
    }
    
    if from_unit not in factors or to_unit not in factors:
        raise ValueError(f"Supported units are: {', '.join(factors.keys())}")
        
    value_in_meters = value * factors[from_unit]
    value_in_target = value_in_meters / factors[to_unit]
    return value_in_target

def main():
    print("--- Microscope Specimen Size Calculator ---")
    try:
        magnification = float(input("Enter magnification size of the lens (e.g., 40): "))
        if magnification <= 0:
            print("Error: Magnification must be greater than 0.")
            return

        image_size = float(input("Enter image size of the specimen: "))
        if image_size < 0:
            print("Error: Image size cannot be negative.")
            return

        unit_in = input("Enter unit of image size (m, cm, mm, um, nm): ").strip().lower()
        unit_out = input("Enter required unit of real life size (m, cm, mm, um, nm): ").strip().lower()
        
        # Formula: Real Life Size = Image Size / Magnification
        real_size_original_unit = image_size / magnification
        
        # Convert to the requested output unit
        real_size_final_unit = convert_unit(real_size_original_unit, unit_in, unit_out)
        
        print(f"\nResult: The real life size of the specimen is {real_size_final_unit:.6g} {unit_out}")
        
    except ValueError as e:
        # Catch conversion factor errors or float parsing errors
        if str(e).startswith("could not convert string to float"):
            print("Error: Please enter valid numerical values for magnification and image size.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
