import subprocess
import csv

# Function to run Volatility 3 plugin
def run_plugin(plugin_name, memory_file):
    try:
        command = f"vol -f {memory_file} {plugin_name}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Plugin '{plugin_name}' ran successfully.")
            print(result.stdout)
        else:
            print(f"Plugin '{plugin_name}' failed to run.")
            print(result.stderr)
    except Exception as e:
        print(f"Error running plugin '{plugin_name}': {e}")

# Main program
def main():
    # Path to the memory dump file
    memory_file = "0zapftis.vmem"
    
    # Path to the CSV file containing successful plugins
    csv_file = "successful_plugins.csv"
    
    # Read plugins from CSV file
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        plugins = [row[0] for row in reader]

    # Run each plugin
    for plugin in plugins:
        run_plugin(plugin, memory_file)

if __name__ == "__main__":
    main()
#write csv file
#python q14.py
