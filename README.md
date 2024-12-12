# Search_Nearby-DSA
# Optimized Geospatial Restaurant Search System

## Project Overview
This project implements an efficient geospatial search system for finding nearby restaurants, inspired by functionalities similar to Google Maps. The solution was developed during a research project at IIT Delhi under the guidance of Prof. Ashish Chiplunkar.

## Key Features
* **Efficient Nearby Restaurant Search**: Quickly find restaurants within a specified radius from a given geographical point
* **Advanced Data Structures**: Utilizes a 2D Segment Tree for optimal data preprocessing and query performance
* **High-Performance Querying**: Achieves range queries with impressive time complexity

## Technical Specifications

### Time Complexity
* Data Preprocessing: O(n log n)
* Range Queries: O(m + log²(n))
   * n: Total number of data points
   * m: Number of points returned in the query

### Core Components
* Custom Heap Implementation
* Collision Detection Algorithm
* 2D Spatial Indexing

## Implementation Details

### Data Structures
* **Heap (`Heap` class)**: A custom min-heap implementation for efficient collision and time-based event management
* **Spatial Indexing**: 2D Segment Tree for fast spatial queries

### Key Functions
* `listCollisions()`: Manages complex spatial and temporal interactions between objects
* `operator()`: Calculates potential collision times and positions
* `collider()`: Handles detailed collision resolution

## Use Cases
* Restaurant location services
* Proximity-based recommendations
* Geospatial data analysis

## Technologies Used
* Python
* Advanced Data Structures
* Algorithmic Optimization

## Performance Advantages
* Sublinear query time
* Minimal memory overhead
* Scalable to large datasets

## Future Enhancements
* Support for more complex geospatial queries
* Integration with real-time location services
* Machine learning-based recommendation improvements
