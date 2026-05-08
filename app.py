from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def convert_unit(value, from_unit, to_unit):
    """Convert between different units of measurement."""
    # Conversion factors to meters
    factors = {
        'm': 1.0,
        'cm': 1e-2,
        'mm': 1e-3,
        'um': 1e-6,  # micrometers
        'nm': 1e-9   # nanometers
    }
    
    if from_unit not in factors or to_unit not in factors:
        raise ValueError(f"Supported units are: {', '.join(factors.keys())}")
    
    value_in_meters = value * factors[from_unit]
    value_in_target = value_in_meters / factors[to_unit]
    return value_in_target

def calculate_specimen_size(magnification, image_size, unit_in, unit_out):
    """Calculate the real life size of a specimen."""
    if magnification <= 0:
        raise ValueError("Magnification must be greater than 0.")
    if image_size < 0:
        raise ValueError("Image size cannot be negative.")
    
    # Formula: Real Life Size = Image Size / Magnification
    real_size_original_unit = image_size / magnification
    
    # Convert to the requested output unit
    real_size_final_unit = convert_unit(real_size_original_unit, unit_in, unit_out)
    
    return real_size_final_unit

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint for calculating specimen size."""
    try:
        data = request.json
        
        # Validate input
        magnification = float(data.get('magnification', 0))
        image_size = float(data.get('image_size', 0))
        unit_in = str(data.get('unit_in', 'um')).lower()
        unit_out = str(data.get('unit_out', 'um')).lower()
        
        # Calculate result
        result = calculate_specimen_size(magnification, image_size, unit_in, unit_out)
        
        return jsonify({
            'success': True,
            'result': f"{result:.6g}",
            'result_raw': result,
            'message': f'The real life size of the specimen is {result:.6g} {unit_out}'
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred.'
        }), 500

@app.route('/api/units', methods=['GET'])
def get_units():
    """Get list of supported units."""
    units = ['m', 'cm', 'mm', 'um', 'nm']
    return jsonify({'units': units})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
