import subprocess

def create_user():
    # Prompt for username
    username = input("Enter the desired username: ")

    # Create the user account
    subprocess.run(['sudo', 'useradd', '-m', username])

    # Set the password for the new user (optional)
    # Replace 'password' with your desired password or remove this line to skip setting it.
    password = input("Enter a password for the user: ")
    
    subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}".encode())

    # Prompt for authorized keys
    public_key = input("Enter the public key: ")

    # Create .ssh directory and authorized_keys file
    ssh_dir = f"/home/{username}/.ssh"
    auth_keys_file = f"{ssh_dir}/authorized_keys"

    subprocess.run(['mkdir', '-p', ssh_dir])
	
    with open(auth_keys_file, "a") as f:
     f.write(public_key)
    subprocess.run(['chmod', '700', ssh_dir])
    subprocess.run(['chmod', '600', auth_keys_file])
    subprocess.run(['chown','-R','{}:{}'.format(username, username), ssh_dir])

print("User account created successfully!")

# Example usage: 
create_user()