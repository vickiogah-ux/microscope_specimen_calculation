# 🔬 Microscope Specimen Size Calculator

A professional web-based GUI application for calculating the real-life size of microscope specimens from magnified images. Built with Flask and designed for easy deployment.

## Features

- **Intuitive Web Interface**: Clean, responsive design that works on desktop and mobile
- **Real-time Calculations**: Instant results with automatic unit conversions
- **Multiple Unit Support**: Supports meters (m), centimeters (cm), millimeters (mm), micrometers (μm), and nanometers (nm)
- **API Endpoint**: RESTful API for programmatic access
- **Production Ready**: Configured for deployment on Render with Gunicorn

## Screenshots

The application features:
- Modern gradient UI with smooth animations
- Responsive form with real-time validation
- Clear result display with large, readable numbers
- Helpful instructions section

## How to Use

### Locally

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Open in Browser**
   Navigate to `http://localhost:5000`

4. **Calculate**
   - Enter the magnification power of your microscope lens
   - Input the magnified image size
   - Select the measurement units
   - Click Calculate to get the real-life specimen size

### Using the Calculator

**Formula:** Real-Life Size = Image Size ÷ Magnification

**Example:**
- Magnification: 40x
- Image Size: 500 μm
- Result: 12.5 μm (real-life size)

## Project Structure

```
.
├── app.py                  # Flask application and API routes
├── requirements.txt        # Python dependencies
├── Procfile               # Render deployment configuration
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Main web interface
└── static/
    ├── style.css         # Styling and responsive design
    └── script.js         # Frontend logic and API calls
```

## API Documentation

### POST /api/calculate

Calculate the specimen size.

**Request Body:**
```json
{
  "magnification": 40,
  "image_size": 500,
  "unit_in": "um",
  "unit_out": "um"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "result": "12.5",
  "result_raw": 12.5,
  "message": "The real life size of the specimen is 12.5 um"
}
```

**Error Response (400):**
```json
{
  "success": false,
  "error": "Magnification must be greater than 0."
}
```

### GET /api/units

Get list of supported measurement units.

**Response:**
```json
{
  "units": ["m", "cm", "mm", "um", "nm"]
}
```

## Deployment on Render

### Prerequisites
- GitHub account with the repository pushed
- Render account (free tier available at https://render.com)

### Step-by-Step Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: Microscope Calculator GUI"
   git push origin main
   ```

2. **Connect to Render**
   - Visit https://render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub account and select this repository

3. **Configure Service**
   - **Name:** microscope-calculator (or your preferred name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free (or paid for better performance)

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Your app will be available at: `https://your-app-name.onrender.com`

### Environment Setup (Optional)

If you need environment variables:
1. In Render dashboard, go to your service settings
2. Add environment variables under "Environment"
3. Example:
   - `FLASK_ENV`: production
   - `PORT`: 5000

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Server**: Gunicorn (WSGI HTTP Server)
- **Deployment**: Render

## Browser Support

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Error Handling

The application includes robust error handling for:
- Invalid magnification values (must be > 0)
- Negative image sizes
- Invalid unit selections
- Network/server errors
- Input validation on both frontend and backend

## Development

### Local Development with Debug Mode

The app runs in debug mode by default when run locally:
```bash
python app.py
```

Debug mode provides:
- Auto-reloading on code changes
- Detailed error pages
- Interactive debugger

### Production vs Development

- **Development**: `python app.py` (Flask development server)
- **Production**: `gunicorn app:app` (recommended for Render)

## Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to your fork
5. Submit a pull request

## License

This project is created for educational purposes at Covenant University (CSC 442).

## Support

For issues or questions:
1. Check the "How to Use" section
2. Verify all inputs are valid
3. Check browser console for errors (F12)
4. Review the Render logs if deployed

## Troubleshooting

### App won't start locally
- Ensure Python 3.7+ is installed
- Install dependencies: `pip install -r requirements.txt`
- Check for port conflicts on port 5000

### Deployment failed on Render
- Check build logs in Render dashboard
- Verify Procfile is correctly formatted
- Ensure all dependencies are in requirements.txt

### Calculations giving unexpected results
- Verify magnification is greater than 0
- Check that units are correctly selected
- Confirm input values are valid numbers

## Version History

### v1.0.0 (Current)
- Initial release with web GUI
- Full calculator functionality
- API endpoints
- Render deployment ready

---

**Created for:** CSC 442 - Covenant University  
**Last Updated:** 2026
