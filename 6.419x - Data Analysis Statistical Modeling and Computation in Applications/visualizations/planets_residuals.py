import numpy as np
import matplotlib.pyplot as plt
from stats.regression import Regression
import os

def plot_planets_regression():
    """Create regression plots for planetary orbital data."""
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Planet data
    x_array = np.array([0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])  # semi-major axis (AU)
    y_array = np.array([0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])  # orbital period (Earth years)

    # Create regression model
    reg = Regression(x_array, y_array)

    # Create two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot 1: Original data and regression line
    ax1.scatter(x_array, y_array, color='blue', alpha=0.7, label='Observed')
    x_line = np.linspace(min(x_array), max(x_array), 100)
    y_line = reg.predict(x_line)
    ax1.plot(x_line, y_line, color='red', label='Regression Line')
    ax1.set_xlabel('Semi-major Axis (AU)')
    ax1.set_ylabel('Orbital Period (Earth Years)')
    ax1.legend()
    ax1.set_title('Planet Orbital Period vs Semi-major Axis')
    ax1.grid(True, alpha=0.3)

    # Plot 2: Residuals
    residuals = reg.residuals()
    ax2.scatter(x_array, residuals, color='green', alpha=0.7)
    ax2.axhline(y=0, color='red', linestyle='--')
    ax2.set_xlabel('Semi-major Axis (AU)')
    ax2.set_ylabel('Residuals (Earth Years)')
    ax2.set_title('Residuals vs Semi-major Axis')
    ax2.grid(True, alpha=0.3)

    # Add R² value as text
    r2_text = f'R² = {reg.r_squared():.4f}'
    ax1.text(0.05, 0.95, r2_text, transform=ax1.transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()

    # Save the plot in images directory
    plt.savefig('images/planets_regression.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    plot_planets_regression()

