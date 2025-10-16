#!/usr/bin/env python3
"""
Matplotlib Sample Visualizations
A comprehensive example of various matplotlib plotting techniques
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle
import seaborn as sns

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_sample_data():
    """Generate sample datasets for visualization"""
    np.random.seed(42)
    
    # Line plot data
    x_line = np.linspace(0, 10, 100)
    y_sin = np.sin(x_line)
    y_cos = np.cos(x_line)
    
    # Scatter plot data
    n_points = 50
    x_scatter = np.random.randn(n_points)
    y_scatter = 2 * x_scatter + np.random.randn(n_points)
    colors_scatter = np.random.rand(n_points)
    sizes_scatter = np.random.uniform(50, 300, n_points)
    
    # Bar chart data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    # Histogram data
    hist_data = np.random.normal(0, 1, 1000)
    
    # Pie chart data
    pie_labels = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint']
    pie_sizes = [30, 25, 20, 25]
    
    return {
        'x_line': x_line, 'y_sin': y_sin, 'y_cos': y_cos,
        'x_scatter': x_scatter, 'y_scatter': y_scatter, 
        'colors_scatter': colors_scatter, 'sizes_scatter': sizes_scatter,
        'categories': categories, 'values': values,
        'hist_data': hist_data,
        'pie_labels': pie_labels, 'pie_sizes': pie_sizes
    }

def create_line_plot(data):
    """Create a line plot with multiple lines"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(data['x_line'], data['y_sin'], 
            label='sin(x)', linewidth=2, color='#1f77b4')
    ax.plot(data['x_line'], data['y_cos'], 
            label='cos(x)', linewidth=2, color='#ff7f0e')
    
    ax.set_title('Trigonometric Functions', fontsize=16, fontweight='bold')
    ax.set_xlabel('X values', fontsize=12)
    ax.set_ylabel('Y values', fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    
    return fig

def create_scatter_plot(data):
    """Create a scatter plot with color and size variations"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(data['x_scatter'], data['y_scatter'], 
                        c=data['colors_scatter'], s=data['sizes_scatter'],
                        alpha=0.7, cmap='viridis')
    
    ax.set_title('Scatter Plot with Color and Size Variations', 
                 fontsize=16, fontweight='bold')
    ax.set_xlabel('X values', fontsize=12)
    ax.set_ylabel('Y values', fontsize=12)
    
    # Add colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Color Scale', fontsize=12)
    
    return fig

def create_bar_chart(data):
    """Create a bar chart"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(data['categories'], data['values'], 
                  color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc'])
    
    ax.set_title('Sample Bar Chart', fontsize=16, fontweight='bold')
    ax.set_xlabel('Categories', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)
    
    return fig

def create_histogram(data):
    """Create a histogram"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    n, bins, patches = ax.hist(data['hist_data'], bins=30, alpha=0.7, 
                              color='skyblue', edgecolor='black')
    
    ax.set_title('Normal Distribution Histogram', fontsize=16, fontweight='bold')
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    
    # Add mean line
    mean_val = np.mean(data['hist_data'])
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {mean_val:.2f}')
    ax.legend()
    
    return fig

def create_pie_chart(data):
    """Create a pie chart"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    wedges, texts, autotexts = ax.pie(data['pie_sizes'], labels=data['pie_labels'],
                                     autopct='%1.1f%%', colors=colors, startangle=90)
    
    ax.set_title('Ice Cream Flavor Preferences', fontsize=16, fontweight='bold')
    
    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    return fig

def create_subplot_grid():
    """Create a grid of subplots"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Subplot Grid Example', fontsize=20, fontweight='bold')
    
    # Top left: Line plot
    x = np.linspace(0, 4*np.pi, 100)
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Top right: Exponential curve
    x = np.linspace(0, 5, 100)
    axes[0, 1].plot(x, np.exp(-x), 'r-', linewidth=2)
    axes[0, 1].set_title('Exponential Decay')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Bottom left: Random scatter
    x = np.random.randn(50)
    y = np.random.randn(50)
    axes[1, 0].scatter(x, y, alpha=0.6, s=50)
    axes[1, 0].set_title('Random Scatter')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Bottom right: Step function
    x = np.linspace(0, 10, 100)
    y = np.floor(x) % 2
    axes[1, 1].step(x, y, 'g-', linewidth=2)
    axes[1, 1].set_title('Step Function')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def create_advanced_plot():
    """Create an advanced plot with annotations and custom styling"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Generate data
    x = np.linspace(0, 10, 200)
    y1 = np.sin(x) * np.exp(-x/5)
    y2 = np.cos(x) * np.exp(-x/8)
    
    # Plot lines
    ax.plot(x, y1, 'b-', linewidth=2, label='Damped Sine', alpha=0.8)
    ax.plot(x, y2, 'r-', linewidth=2, label='Damped Cosine', alpha=0.8)
    
    # Fill between curves
    ax.fill_between(x, y1, y2, alpha=0.2, color='gray')
    
    # Add annotations
    ax.annotate('Maximum Point', xy=(np.pi/2, np.exp(-np.pi/10)), 
                xytext=(4, 0.8), arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=12, ha='center')
    
    # Customize plot
    ax.set_title('Advanced Matplotlib Plot with Annotations', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Set axis limits
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    
    # Add text box
    textstr = 'Damped oscillations\nwith exponential decay'
    props = dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    
    return fig

def main():
    """Main function to generate and display all plots"""
    print("Generating matplotlib sample visualizations...")
    
    # Create sample data
    data = create_sample_data()
    
    # Generate all plots
    plots = {
        'Line Plot': create_line_plot(data),
        'Scatter Plot': create_scatter_plot(data),
        'Bar Chart': create_bar_chart(data),
        'Histogram': create_histogram(data),
        'Pie Chart': create_pie_chart(data),
        'Subplot Grid': create_subplot_grid(),
        'Advanced Plot': create_advanced_plot()
    }
    
    # Save all plots
    for name, fig in plots.items():
        filename = f"{name.lower().replace(' ', '_')}.png"
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved: {filename}")
    
    # Show all plots
    plt.show()
    
    print("\nAll plots generated successfully!")
    print("Files saved:")
    for name in plots.keys():
        filename = f"{name.lower().replace(' ', '_')}.png"
        print(f"  - {filename}")

if __name__ == "__main__":
    main()
