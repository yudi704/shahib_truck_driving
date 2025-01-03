import os
import django
from django.template import loader
import sys

# Set the DJANGO_SETTINGS_MODULE for the environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shahib_truck_driving.settings')

# Set the environment variable directly within the script
os.environ['DJANGO_ENV'] = 'production'

# Initialize Django settings
django.setup()

def render_templates(output_dir="staticfiles"):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # List of templates to pre-render with the correct path for those in the `partials` folder
    templates = [
        "partials/about.html", 
        "partials/contact.html", 
        "partials/footer.html", 
        "partials/navbar.html", 
        "partials/reviews.html", 
        "partials/services.html", 
        "base.html", 
        "home.html"
    ]

    for template_name in templates:
        # Load and render each template
        try:
            template = loader.get_template(template_name)  # This should now find files in `partials`
            rendered_content = template.render({})  # Pass any context variables if needed
            # Write the rendered content to an HTML file in the output directory
            output_path = os.path.join(output_dir, template_name)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the subdirectories exist
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered_content)
            print(f"Rendered {template_name} to {output_path}")
        except Exception as e:
            print(f"Error rendering {template_name}: {e}")

if __name__ == "__main__":
    render_templates()
