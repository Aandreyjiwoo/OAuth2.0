from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
# A secret key is required to use Flask sessions securely
app.secret_key = "REPLACE_WITH_A_RANDOM_SECRET_KEY" 

oauth = OAuth(app)

# Configure GitHub OAuth
github = oauth.register(
    name='github',
    client_id='Ov23lioG1KcH24y9288X',       
    client_secret='6e8c9ac9347ac0e79fce8e6aa06494d14050ff27',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# Home route just for convenience
@app.route('/')
def home():
    if 'user' in session:
        return 'Welcome! <a href="/profile">View Profile</a> | <a href="/logout">Logout</a>'
    return '<a href="/login">Login with GitHub</a>'

# Create Login Route
@app.route('/login')
def login():
    return github.authorize_redirect(url_for('callback', _external=True))

# Create Callback Route
@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    
    resp = github.get('user')
    user = resp.json()
    
    session['user'] = user
    return redirect('/')

# Create Protected API (Profile)
@app.route('/profile')
def profile():
    # Check if user is authenticated
    if 'user' not in session:
        return "Unauthorized", 401
    
    user_data = session['user']
    
    # Create a simple HTML page to display the user's data nicely
    html_content = f"""
    <html>
    <head><title>My Profile</title></head>
    <body style="font-family: Arial, sans-serif; text-align: left; margin: 50px 20px;">
        <h2>Welcome, {user_data.get('name') or user_data.get('login')}!</h2>
        
        <img src="{user_data.get('avatar_url')}" alt="User Avatar" style="width: 150px; border-radius: 50%; border: 2px solid #ccc; display: block; margin-bottom: 20px;">
        
        <p><strong>GitHub Username:</strong> {user_data.get('login')}</p>
        <p><strong>Public Repositories:</strong> {user_data.get('public_repos')}</p>
        <p><a href="{user_data.get('html_url')}" target="_blank">View GitHub Profile</a></p>
        
        <br>
        <div style="border-top: 1px solid #eee; pt: 10px; width: fit-content;">
            <a href="/">Back to Home</a> 
            <br></br>
            <a href="/logout">Logout</a>
        </div>
    </body>
</html>
    """
    
    return html_content
# Create Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# --- BONUS CHALLENGE ---
# Create a new protected route
@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    return jsonify({
        "message": "Success! You have accessed the bonus secure data.",
        "username": session['user'].get('login')
    })

# Run Application
if __name__ == '__main__':
    app.run(debug=True)