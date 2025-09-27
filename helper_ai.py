def generate_workout_logic(goal, level, days):
    """
    Rule-based expert system that generates workout plans based on:
    - goal: The fitness goal (build_muscle, lose_fat, general_fitness)
    - level: Experience level (beginner, intermediate, advanced)
    - days: Number of workout days per week (3, 4, 5)
    
    Returns a dictionary where:
    - Keys are workout day names (e.g., 'Day 1: Upper Body')
    - Values are lists of exercises with sets and reps
    """
    workout_plan = {}
    
    # Build Muscle - Beginner
    if goal == 'build_muscle' and level == 'beginner':
        if days == 3:
            workout_plan = {
                'Day 1: Full Body': [
                    'Squats: 3 sets of 8-10 reps',
                    'Push-ups: 3 sets of 8-12 reps',
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Planks: 3 sets of 30 seconds'
                ],
                'Day 2: Full Body': [
                    'Lunges: 3 sets of 10 reps per leg',
                    'Dumbbell Bench Press: 3 sets of 10 reps',
                    'Lat Pulldowns: 3 sets of 10 reps',
                    'Bicycle Crunches: 3 sets of 15 reps per side'
                ],
                'Day 3: Full Body': [
                    'Romanian Deadlifts: 3 sets of 10 reps',
                    'Shoulder Press: 3 sets of 10 reps',
                    'Inverted Rows: 3 sets of 8-10 reps',
                    'Side Planks: 3 sets of 20 seconds per side'
                ]
            }
        elif days == 4:
            workout_plan = {
                'Day 1: Upper Body': [
                    'Push-ups: 3 sets of 8-12 reps',
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Dumbbell Shoulder Press: 3 sets of 10 reps',
                    'Tricep Dips: 3 sets of 8-10 reps'
                ],
                'Day 2: Lower Body': [
                    'Squats: 3 sets of 10 reps',
                    'Romanian Deadlifts: 3 sets of 10 reps',
                    'Lunges: 3 sets of 10 reps per leg',
                    'Calf Raises: 3 sets of 12 reps'
                ],
                'Day 3: Upper Body': [
                    'Dumbbell Bench Press: 3 sets of 10 reps',
                    'Lat Pulldowns: 3 sets of 10 reps',
                    'Lateral Raises: 3 sets of 12 reps',
                    'Tricep Pushdowns: 3 sets of 10 reps'
                ],
                'Day 4: Lower Body': [
                    'Goblet Squats: 3 sets of 10 reps',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Step-ups: 3 sets of 10 reps per leg',
                    'Planks: 3 sets of 30 seconds'
                ]
            }
        elif days == 5:
            workout_plan = {
                'Day 1: Push': [
                    'Push-ups: 3 sets of 8-12 reps',
                    'Dumbbell Shoulder Press: 3 sets of 10 reps',
                    'Tricep Dips: 3 sets of 8-10 reps',
                    'Chest Flyes: 3 sets of 12 reps'
                ],
                'Day 2: Pull': [
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Lat Pulldowns: 3 sets of 10 reps',
                    'Face Pulls: 3 sets of 12 reps',
                    'Bicep Curls: 3 sets of 10 reps'
                ],
                'Day 3: Legs': [
                    'Squats: 3 sets of 10 reps',
                    'Romanian Deadlifts: 3 sets of 10 reps',
                    'Lunges: 3 sets of 10 reps per leg',
                    'Calf Raises: 3 sets of 12 reps'
                ],
                'Day 4: Upper Body': [
                    'Dumbbell Bench Press: 3 sets of 10 reps',
                    'Seated Rows: 3 sets of 10 reps',
                    'Lateral Raises: 3 sets of 12 reps',
                    'Skull Crushers: 3 sets of 10 reps'
                ],
                'Day 5: Lower Body': [
                    'Goblet Squats: 3 sets of 10 reps',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Step-ups: 3 sets of 10 reps per leg',
                    'Ab Crunches: 3 sets of 15 reps'
                ]
            }
    
    # Lose Fat - Intermediate
    elif goal == 'lose_fat' and level == 'intermediate':
        if days == 3:
            workout_plan = {
                'Day 1: Full Body HIIT': [
                    'Circuit: 4 rounds with 30 seconds rest between exercises',
                    'Burpees: 30 seconds',
                    'Mountain Climbers: 30 seconds',
                    'Jump Squats: 30 seconds',
                    'Push-ups: 30 seconds',
                    'Kettlebell Swings: 30 seconds'
                ],
                'Day 2: Cardio & Core': [
                    'Treadmill Intervals: 20 minutes (1 min sprint, 1 min walk)',
                    'Plank Variations: 3 sets of 45 seconds each',
                    'Russian Twists: 3 sets of 20 reps',
                    'Mountain Climbers: 3 sets of 30 seconds',
                    'Bicycle Crunches: 3 sets of 20 reps per side'
                ],
                'Day 3: Full Body Strength': [
                    'Deadlifts: 4 sets of 8 reps',
                    'Dumbbell Bench Press: 4 sets of 10 reps',
                    'Barbell Rows: 4 sets of 10 reps',
                    'Lunges: 3 sets of 12 reps per leg',
                    'Superset: Tricep Pushdowns & Bicep Curls: 3 sets of 12 reps each'
                ]
            }
        elif days == 4:
            workout_plan = {
                'Day 1: Upper Body & HIIT': [
                    'Bench Press: 4 sets of 8 reps',
                    'Bent Over Rows: 4 sets of 10 reps',
                    'Shoulder Press: 3 sets of 10 reps',
                    'HIIT Finisher: 10 minutes (30s work, 30s rest)',
                    'Exercises: Burpees, Mountain Climbers, Push-ups'
                ],
                'Day 2: Lower Body & Core': [
                    'Squats: 4 sets of 10 reps',
                    'Romanian Deadlifts: 4 sets of 10 reps',
                    'Walking Lunges: 3 sets of 20 steps',
                    'Hanging Leg Raises: 3 sets of 12 reps',
                    'Plank with Shoulder Taps: 3 sets of 40 seconds'
                ],
                'Day 3: Cardio Circuit': [
                    'Circuit: 5 rounds with minimal rest',
                    'Jump Rope: 1 minute',
                    'Box Jumps: 45 seconds',
                    'Battle Ropes: 45 seconds',
                    'Kettlebell Swings: 45 seconds',
                    'Rowing Machine: 1 minute'
                ],
                'Day 4: Full Body Strength': [
                    'Deadlifts: 4 sets of 8 reps',
                    'Incline Dumbbell Press: 4 sets of 10 reps',
                    'Pull-ups or Lat Pulldowns: 4 sets of 8-10 reps',
                    'Bulgarian Split Squats: 3 sets of 10 reps per leg',
                    'Superset: Lateral Raises & Face Pulls: 3 sets of 12 reps each'
                ]
            }
        elif days == 5:
            workout_plan = {
                'Day 1: Push & HIIT': [
                    'Bench Press: 4 sets of 8 reps',
                    'Shoulder Press: 4 sets of 10 reps',
                    'Incline Dumbbell Flyes: 3 sets of 12 reps',
                    'Tricep Dips: 3 sets of 12 reps',
                    'HIIT Finisher: 10 minutes (30s work, 30s rest)',
                    'Exercises: Burpees, Push-ups, Mountain Climbers'
                ],
                'Day 2: Pull & Core': [
                    'Pull-ups or Lat Pulldowns: 4 sets of 8-10 reps',
                    'Bent Over Rows: 4 sets of 10 reps',
                    'Face Pulls: 3 sets of 15 reps',
                    'Bicep Curls: 3 sets of 12 reps',
                    'Hanging Leg Raises: 3 sets of 12 reps',
                    'Russian Twists: 3 sets of 20 reps'
                ],
                'Day 3: Legs & HIIT': [
                    'Squats: 4 sets of 10 reps',
                    'Romanian Deadlifts: 4 sets of 10 reps',
                    'Walking Lunges: 3 sets of 20 steps',
                    'Calf Raises: 3 sets of 15 reps',
                    'HIIT Finisher: 10 minutes (30s work, 30s rest)',
                    'Exercises: Jump Squats, Box Jumps, Kettlebell Swings'
                ],
                'Day 4: Cardio Circuit': [
                    'Circuit: 5 rounds with minimal rest',
                    'Jump Rope: 1 minute',
                    'Kettlebell Swings: 45 seconds',
                    'Box Jumps: 45 seconds',
                    'Battle Ropes: 45 seconds',
                    'Rowing Machine: 1 minute'
                ],
                'Day 5: Full Body & Core': [
                    'Deadlifts: 4 sets of 8 reps',
                    'Incline Bench Press: 4 sets of 10 reps',
                    'Pull-ups or Lat Pulldowns: 4 sets of 8-10 reps',
                    'Lunges: 3 sets of 12 reps per leg',
                    'Plank Variations: 3 sets of 45 seconds each',
                    'Bicycle Crunches: 3 sets of 20 reps per side'
                ]
            }
    
    # General Fitness - Beginner
    elif goal == 'general_fitness' and level == 'beginner':
        if days == 3:
            workout_plan = {
                'Day 1: Cardio & Core': [
                    'Brisk Walking: 20 minutes',
                    'Bodyweight Squats: 3 sets of 12 reps',
                    'Modified Push-ups: 3 sets of 8 reps',
                    'Plank: 3 sets of 20 seconds',
                    'Bird-dogs: 3 sets of 8 reps per side'
                ],
                'Day 2: Strength & Mobility': [
                    'Dumbbell Goblet Squats: 3 sets of 10 reps',
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Wall Angels: 3 sets of 10 reps',
                    'Cat-Cow Stretches: 2 minutes'
                ],
                'Day 3: Functional Fitness': [
                    'Step-ups: 3 sets of 10 reps per leg',
                    'Modified Push-ups: 3 sets of 8 reps',
                    'Chair Squats: 3 sets of 10 reps',
                    'Standing Dumbbell Curls: 3 sets of 10 reps',
                    'Supermans: 3 sets of 10 reps',
                    'Cooldown: 5 minutes of stretching'
                ]
            }
        elif days == 4:
            workout_plan = {
                'Day 1: Cardio & Core': [
                    'Brisk Walking: 20 minutes',
                    'Bodyweight Squats: 3 sets of 12 reps',
                    'Modified Push-ups: 3 sets of 8 reps',
                    'Plank: 3 sets of 20 seconds',
                    'Bird-dogs: 3 sets of 8 reps per side'
                ],
                'Day 2: Upper Body': [
                    'Dumbbell Chest Press: 3 sets of 10 reps',
                    'Seated Dumbbell Shoulder Press: 3 sets of 10 reps',
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Standing Dumbbell Curls: 3 sets of 10 reps',
                    'Tricep Kickbacks: 3 sets of 10 reps per arm'
                ],
                'Day 3: Active Recovery & Mobility': [
                    'Light Walking: 15 minutes',
                    'Arm Circles: 2 sets of 10 in each direction',
                    'Hip Circles: 2 sets of 10 in each direction',
                    'Cat-Cow Stretches: 2 minutes',
                    'Child\'s Pose: 60 seconds',
                    'Downward Dog: 60 seconds'
                ],
                'Day 4: Lower Body & Core': [
                    'Dumbbell Goblet Squats: 3 sets of 10 reps',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Step-ups: 3 sets of 10 reps per leg',
                    'Calf Raises: 3 sets of 15 reps',
                    'Bicycle Crunches: 3 sets of 10 reps per side',
                    'Side Planks: 3 sets of 15 seconds per side'
                ]
            }
        elif days == 5:
            workout_plan = {
                'Day 1: Total Body': [
                    'Bodyweight Squats: 3 sets of 12 reps',
                    'Modified Push-ups: 3 sets of 8 reps',
                    'Seated Dumbbell Shoulder Press: 3 sets of 10 reps',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Plank: 3 sets of 20 seconds'
                ],
                'Day 2: Cardio Focus': [
                    'Brisk Walking: 25 minutes',
                    'Marching in Place: 3 sets of 1 minute',
                    'Step Touches: 3 sets of 1 minute',
                    'Arm Circles: 2 sets of 30 seconds each direction',
                    'Cooldown Stretches: 5 minutes'
                ],
                'Day 3: Upper Body': [
                    'Dumbbell Chest Press: 3 sets of 10 reps',
                    'Dumbbell Rows: 3 sets of 10 reps per arm',
                    'Lateral Raises: 3 sets of 10 reps',
                    'Standing Dumbbell Curls: 3 sets of 10 reps',
                    'Tricep Kickbacks: 3 sets of 10 reps per arm'
                ],
                'Day 4: Lower Body': [
                    'Dumbbell Goblet Squats: 3 sets of 10 reps',
                    'Step-ups: 3 sets of 10 reps per leg',
                    'Glute Bridges: 3 sets of 12 reps',
                    'Calf Raises: 3 sets of 15 reps',
                    'Leg Raises: 3 sets of 10 reps'
                ],
                'Day 5: Mobility & Core': [
                    'Cat-Cow Stretches: 2 minutes',
                    'Bird-dogs: 3 sets of 8 reps per side',
                    'Bicycle Crunches: 3 sets of 10 reps per side',
                    'Side Planks: 3 sets of 15 seconds per side',
                    'Child\'s Pose: 60 seconds',
                    'Downward Dog: 60 seconds'
                ]
            }
    
    # Default case - general plan if combination doesn't match specific rules
    else:
        workout_plan = {
            'Day 1: Full Body': [
                'Squats: 3 sets of 10 reps',
                'Push-ups: 3 sets of 10 reps',
                'Dumbbell Rows: 3 sets of 10 reps per arm',
                'Planks: 3 sets of 30 seconds'
            ],
            'Day 2: Full Body': [
                'Lunges: 3 sets of 10 reps per leg',
                'Dumbbell Chest Press: 3 sets of 10 reps',
                'Lat Pulldowns: 3 sets of 10 reps',
                'Bicycle Crunches: 3 sets of 15 reps per side'
            ]
        }
        
        # Add more days based on days parameter
        if days >= 3:
            workout_plan['Day 3: Full Body'] = [
                'Romanian Deadlifts: 3 sets of 10 reps',
                'Shoulder Press: 3 sets of 10 reps',
                'Bodyweight Rows: 3 sets of 10 reps',
                'Side Planks: 3 sets of 20 seconds per side'
            ]
        if days >= 4:
            workout_plan['Day 4: Full Body'] = [
                'Step-ups: 3 sets of 10 reps per leg',
                'Push-ups: 3 sets of 10 reps',
                'Face Pulls: 3 sets of 12 reps',
                'Plank to Push-up: 3 sets of 6 reps'
            ]
        if days >= 5:
            workout_plan['Day 5: Full Body'] = [
                'Goblet Squats: 3 sets of 10 reps',
                'Incline Push-ups: 3 sets of 10 reps',
                'Inverted Rows: 3 sets of 10 reps',
                'Mountain Climbers: 3 sets of 20 reps per side'
            ]
    
    return workout_plan
