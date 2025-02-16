# Hydraulic Fracture Web

This project provides a web interface for calculating and visualizing hydraulic fracture propagation using the KGD model.

## Features

* Calculates fracture width and pressure distribution along the fracture length.
* Compares global and local solutions for different propagation regimes (K, M, Kt, Mt).
* Interactive plots for visualizing results.

## Getting Started

### Prerequisites

* Python 3.7 or higher
* Flask
* NumPy
* SciPy
* Highcharts

### Installation

1. Clone the repository:

```bash
git clone https://github.com/abessmer/hydraulic-fracture-web.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the App

1. Navigate to the project directory:

```bash
cd hydraulic-fracture-web
```

2. Run the Flask app:

```bash
python main.py
```

3. Open your web browser and go to `http://127.0.0.1:8080/`

## Usage

1. Enter the material parameters in the input fields.
2. Click the "Calculate" button.
3. The results will be displayed in the plots.

## License

This project is licensed under the MIT License.