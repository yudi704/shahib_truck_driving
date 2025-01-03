import os
import django
from django.template import loader
from django.conf import settings

import sys

print(sys.path)

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # Replace with your project settings module
django.setup()

def render_templates(output_dir="staticfiles"):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # List of templates to pre-render
    templates = ["about.html", "contact.html", "footer.html", "navbar.html", "reviews.html", "services.html", "base.html", "home.html"]

    for template_name in templates:
        # Load and render each template
        template = loader.get_template(template_name)
        rendered_content = template.render({})  # Pass any context variables if needed
        
        # Write the rendered content to an HTML file in the output directory
        output_path = os.path.join(output_dir, template_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_content)
        print(f"Rendered {template_name} to {output_path}")

if __name__ == "__main__":
    render_templates()
