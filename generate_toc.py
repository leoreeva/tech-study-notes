import os

def generate_toc():
    toc_lines = ['# Table of Contents']
    
    for dirpath, dirnames, filenames in os.walk('.'):

        if dirpath != "." and not dirpath.startswith(".\\.git") and len(filenames) > 0:
            
            # make folder name readable
            folder_name = os.path.basename(dirpath).replace('_', ' ').title()
            toc_lines.append(f'\n**{folder_name}**')

            # add files links
            i = 1
            for file in sorted(filenames):
                if file.endswith('.md'):
                    file_path = os.path.relpath(os.path.join(dirpath, file)).replace('\\','/')
                    display_name = file.replace('_', ' ').replace('.md', '').title()
                    toc_lines.append(f'{i}. [{display_name}]({file_path})')
                    i += 1
    
    return '\n'.join(toc_lines) + '\n'

# write result to theory.md
with open('table_of_contents.md', 'w') as f:
    f.write(generate_toc())
