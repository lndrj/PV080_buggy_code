import sys 
import os
import yaml
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)
    
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    """
    Person class for name
    """
    def __init__(self, name):
        self.name = name

def print_nametag(format_string, person):
    """
    Formatting function for nametags
    """
    print(format_string.format(person=person))

def fetch_website(urllib_version, url):
    """
    Fetching website using urllib
    """
    # Import the requested version (2 or 3) of urllib
    if urlib_version == "2":
        import urllib2 as urllib
    elif urllib_version == "3":
        import urllib3 as urllib
    else:
        raise ValueError("Invalid urllib version")
    
    #exec(f"import urllib{urllib_version} as urllib", globals())

    # Fetch and print the requested URL
 
    try: 
        http = urllib.PoolManager()
        r = http.request('GET', url)
        return r.data
    except:
        print('Exception')

def load_yaml(filename):
    """
    Loading yaml file
    """
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    """
    Authentication method to verivy if passwords are correct
    """
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)