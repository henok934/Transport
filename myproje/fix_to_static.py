import os

templates_dir = 'users/templates/users'

def replace_cdns():
    count = 0
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                
                # 1. FontAwesome CDN ወደ Static መቀየር
                if 'font-awesome' in content:
                    content = content.replace(
                        'href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"',
                        'href="{% static \'css/all.min.css\' %}"'
                    )

                # 2. Bootstrap CSS CDN ወደ Static መቀየር
                if 'bootstrap.min.css' in content:
                    content = content.replace(
                        'href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"',
                        'href="{% static \'css/bootstrap.min.css\' %}"'
                    )
                    content = content.replace(
                        'href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"',
                        'href="{% static \'css/bootstrap.min.css\' %}"'
                    )

                # 3. {% load static %} በመጀመሪያው መስመር መኖሩን ማረጋገጥ (ከሌለ መጨመር)
                if content != original_content:
                    if '{% load static %}' not in content:
                        content = '{% load static %}\n' + content
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {file_path}")
                    count += 1

    print(f"\nSuccessfully migrated {count} files to use local static assets!")

if __name__ == '__main__':
    replace_cdns()
