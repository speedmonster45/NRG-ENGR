# NRG Engineering - Static Website

Welcome to the **NRG Engineering** website! This repository hosts the static website of NRG Engineering, designed with modular CSS and optimized for scalability. The project uses modern best practices like Tailwind CSS for styling and a clean development workflow for efficient deployment.

## Features

- **Responsive Design**: Optimized for mobile, tablet, and desktop views using a mobile-first approach.
- **Modular CSS**: Styles are organized into separate files for better maintainability and scalability.
- **Tailwind CSS Integration**: We use Tailwind CSS for utility-based styling and rapid UI development.
- **Static Website Hosting**: Hosted on **AWS S3** with continuous integration and deployment through GitHub Actions.

## Project Structure

The project is structured to maintain separation of concerns between the styles, layout, components, and utilities. Below is a breakdown of the structure:

```plaintext
/
├── assets/
│   ├── css/
│   │   ├── base.css       # Base styles and resets
│   │   ├── layout.css     # Layout and grid system
│   │   ├── components.css # UI components (buttons, forms, nav)
│   │   └── utilities.css  # Utility classes (spacing, text alignment)
│   ├── images/            # All images and assets used in the site
│   └── js/                # JavaScript files (if any)
├── index.html             # Main HTML file for the homepage
├── about.html             # About page
├── contact.html           # Contact page
└── README.md              # Project documentation
