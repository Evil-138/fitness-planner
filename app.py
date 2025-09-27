from flask import Flask, render_template, request
from helper_ai import generate_workout_logic
import os

app = Flask(__name__)
# Set to False in production
app.config['DEBUG'] = False

@app.route('/')
def index():
    """
    Render the index page with the workout planner form.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Process the form data and generate a workout plan.
    """
    goal = request.form.get('goal')
    level = request.form.get('level')
    days = int(request.form.get('days'))
    
    # Generate workout plan using helper function
    workout_plan = generate_workout_logic(goal, level, days)
    
    return render_template('result.html', workout_plan=workout_plan)

if __name__ == '__main__':
    # Use PORT environment variable if available (for Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)