import paramiko

# Create an SSH client
ssh = paramiko.SSHClient()

# Load the SSH Keys
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def execute_shell_script():
    # Connect to the remote machine using a specific username and SSH key file
    #ssh.connect('192.168.68.127', username='helladarion', password='######')
    ssh.connect('192.168.68.127', username='helladarion', key_filename='/sshkeys/id_ed25519-rafa-nopw')

    # Execute the shell script
    stdin, stdout, stderr = ssh.exec_command('df -Ph; uptime; last')

    # Get the output of the command
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    # Close the SSH connection
    ssh.close()
    return output


from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
        {
            'author': 'Rafael de Paiva',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'April 1, 2020'
        },
        {
            'author': 'Tayse Sabrina',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'October 2, 2020'
        }
]

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', posts=posts, title="patch-web")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/result')
def result():
    # Call the function that executes the shell script
    output = execute_shell_script()

    return render_template('result.html', title="Shell Result", output=output)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9000, debug=True)
