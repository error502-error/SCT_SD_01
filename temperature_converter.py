def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, scale):
    scale = scale.lower()
    if scale == 'c':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        return f"{value}°C = {f:.2f}°F = {k:.2f}K"
    elif scale == 'f':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        return f"{value}°F = {c:.2f}°C = {k:.2f}K"
    elif scale == 'k':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        return f"{value}K = {c:.2f}°C = {f:.2f}°F"
    else:
        return "Invalid scale! Use 'C', 'F', or 'K'."

def main():
    print("Temperature Converter")
    value = float(input("Enter temperature value: "))
    scale = input("Enter scale (C/F/K): ")
    result = convert_temperature(value, scale)
    print(result)

if __name__ == "__main__":
    main()
