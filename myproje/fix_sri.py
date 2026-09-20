import os
import re

templates_dir = 'users/templates/users'

def fix_html_files():
    # ለ FontAwesome እና Bootstrap የተለመዱ የ SRI ሃሾች
    fa_integrity = 'integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer"'
    bootstrap_css_integrity = 'integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous"'
    bootstrap_js_integrity = 'integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"'

    count = 0
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated = False
                
                # FontAwesome ሊንክ ላይ integrity ከሌለ መጨመር
                if 'font-awesome' in content and 'integrity' not in content:
                    content = content.replace('rel="stylesheet"', f'rel="stylesheet" {fa_integrity}')
                    updated = True

                # Bootstrap CSS ላይ integrity ከሌለ መጨመር
                if 'bootstrap.min.css' in content and 'integrity' not in content:
                    content = content.replace('rel="stylesheet"', f'rel="stylesheet" {bootstrap_css_integrity}')
                    updated = True

                if updated:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed: {file_path}")
                    count += 1

    print(f"\nSuccessfully updated {count} HTML files with SRI attributes!")

if __name__ == '__main__':
    fix_html_files()
