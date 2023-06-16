import subprocess


def install_packages():
    packages = {
        'pygame': '==2.1.2',
        'pygame_menu': '==4.4.2'
    }

    for package, version in packages.items():
        try:
            subprocess.check_call(['pip', 'install', f'{package}{version}'])
            print(f'Successfully installed {package}{version}')
        except subprocess.CalledProcessError as e:
            print(f'An error occurred while installing {package}{version}: {str(e)}')


if __name__ == '__main__':
    install_packages()
