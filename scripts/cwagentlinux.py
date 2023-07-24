import subprocess

# Function to install CloudWatch agent on Linux
def install_cloudwatch_agent_linux():
    try:
        # Install the CloudWatch agent package using yum
        subprocess.run(["sudo", "yum", "-y", "install", "amazon-cloudwatch-agent"])
        
        print("CloudWatch Agent installed successfully.")
        
        # Run the configuration wizard for CloudWatch agent
        subprocess.run(["sudo", "/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard"])

    except Exception as e:
        print(f"Error occurred during installation: {str(e)}")

# Main function for script execution
def main():
    category = input("Enter the category (Linux/Windows): ")

    if category.lower() == "linux":
         install_cloudwatch_agent_linux()
        
    elif category.lower() == "windows":
         print("Sorry, this script does not support Windows installations.")

    else:
         print("Invalid category. Please enter either 'Linux' or 'Windows'.")


if __name__ == "__main__":
     main()