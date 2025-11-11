import os
import re

# List of all 18 blog post files
blog_posts = [
    "shraddha-antim-sanskar-white-flower-ghaziabad-noida.html",
    "flower-decoration-delivery-independence-day-ghaziabad-greater-noida.html",
    "raksha-bandhan-flowers-delivery-canada-to-ghaziabad-noida.html",
    "teej-chulha-flower-decoration-ghaziabad-noida-greater-noida.html",
    "celebrity-wedding-jaimala-flower-decoration-ghaziabad.html",
    "chocolate-rose-flower-bouquet-delivery-ghaziabad.html",
    "big-size-flower-arrangement-ghaziabad.html",
    "haldi-mehandi-flower-decoration-vasundhara.html",
    "haldi-mehandi-flower-decoration-noida-ghaziabad.html",
    "republic-day-flower-decoration-ghaziabad-noida.html",
    "wedding-home-flower-decoration-ghaziabad.html",
    "stage-entrance-flower-decoration-ghaziabad-noida.html",
    "teacher-day-flower-delivery-ghaziabad-greater-noida.html",
    "navratri-genda-flower-patta-mala-ghaziabad.html",
    "flower-delivery-decoration-ghaziabad-noida-greater-Noida.html",
    "wedding-flower-decoration-ghaziabad-noida-greater-noida.html",
    "birthday-flower-bouquets-delivery-ghaziabad-noida-greater-noida.html",
    "corporate-flower-decoration-ghaziabad-noida-greater-Noida.html"
]

print("Updating all blog posts with new WhatsApp button component...\n")

for post_file in blog_posts:
    file_path = os.path.join(os.getcwd(), post_file)
    
    if not os.path.exists(file_path):
        print(f"  ⚠️  File not found: {post_file}")
        continue
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old WhatsApp button (inline SVG and link)
    # Pattern to match the old WhatsApp button with full SVG
    old_whatsapp_pattern = r'<a href="https://wa\.me/919599308501" target="_blank" class="whatsapp-btn"[^>]*aria-label="Contact us on WhatsApp"><svg class="whatsapp-icon"[^>]*viewBox="0 0 24 24"[^>]*xmlns="http://www\.w3\.org/2000/svg"><path d="[^"]*"/></svg></a>'
    
    # Check if old WhatsApp button exists
    if re.search(old_whatsapp_pattern, content):
        # Remove the old button
        content = re.sub(old_whatsapp_pattern, '', content)
        
        # Add new WhatsApp button include before closing body tag
        new_whatsapp_include = '\n    <!-- WhatsApp Floating Button -->\n    <script>\n        fetch(\'/blog/whatsapp-button.html\')\n            .then(r => r.text())\n            .then(html => document.body.insertAdjacentHTML(\'beforeend\', html));\n    </script>\n'
        
        # Replace closing body tag
        content = content.replace('</body>', new_whatsapp_include + '</body>')
        
        # Write the updated file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Updated: {post_file}")
    else:
        # If old button not found, just add the new one if not already present
        if 'whatsapp-button.html' not in content:
            new_whatsapp_include = '\n    <!-- WhatsApp Floating Button -->\n    <script>\n        fetch(\'/blog/whatsapp-button.html\')\n            .then(r => r.text())\n            .then(html => document.body.insertAdjacentHTML(\'beforeend\', html));\n    </script>\n'
            content = content.replace('</body>', new_whatsapp_include + '</body>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ Added WhatsApp button: {post_file}")
        else:
            print(f"  ℹ️  Already has WhatsApp component: {post_file}")

print("\n✅ All blog posts updated!")
print("- Old WhatsApp SVG buttons removed")
print("- New WhatsApp component loaded dynamically")
print("- Component file: /blog/whatsapp-button.html")
