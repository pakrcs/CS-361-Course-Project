from flask import Flask, request, jsonify

app = Flask(__name__)

courses_data = [
    {
        'id': 1,
        'name': 'Pinehurst No. 2',
        'location': 'Pinehurst, NC',
        'par': 70,
        'rating': 76.5,
        'description': '''Donald Ross’s masterpiece, No. 2 at Pinehurst has served as the site of more 
        single golf championships than any other course in America. This results in one of the more 
        finely balanced and difficult courses across not just America, but the world.'''
    },
    {
        'id': 2,
        'name': 'Augusta National Golf Club',
        'location': 'Augusta, GA',
        'par': 72,
        'rating': 76.2,
        'description': '''Home of the prestigious Masters Tournament, this course is consistently ranked 
        towards the top of America's greatest golf courses. Featuring the iconic 12th hole with its narrow 
        green, water hazard, and unpredictable winds, this hole proves to be a challenge for even pros.'''
    },
    {
        'id': 3,
        'name': 'Pebble Beach Golf Links',
        'location': 'Pebble Beach, CA',
        'par': 72,
        'rating': 75.9,
        'description': '''Its coastal holes along the cliffs of Stillwater Cove and Carmel Bay - Nos. 4-10 
        and Nos. 17-18 - rank among the most beautiful and challenging in the world. Playing Pebble Beach is 
        the epitome of bucket-list golf. Home to the AT&T Pebble Beach Pro-am annually every February.'''
    },
    {
        'id': 4,
        'name': 'Druids Glen',
        'location': 'Kent, WA',
        'par': 72,
        'rating': 75.1,
        'description': '''The landscape is the epitome of the dramatic terrain that the Pacific 
        Northwest is known for. Mount Rainier even serves as the backdrop for the course. The layout 
        is a challenging test with rolling fairways and undulating greens framed by mature trees.'''
    },
    {
        'id': 5,
        'name': 'TPC Louisiana',
        'location': 'Avondale, LA',
        'par': 72,
        'rating': 76.3,
        'description': '''As part of the Audubon Golf Trail, it stretches across more than 250 acres of 
        wetlands along the Mississippi River delta. The TPC Louisiana layout will challenge you with 
        more than 100 strategically placed bunkers and water hazards on several holes.'''
    },
    {
        'id': 6,
        'name': 'Plum Creek Golf Club',
        'location': 'Carmel, IN',
        'par': 72,
        'rating': 76.3,
        'description': '''Opened in 1998, this Pete Dye design has hosted several college and professional 
        golf tournaments. Several ponds and a winding stream come into play throughout the course, placing 
        a premium on smart play, all while minimizing the need for forced carries for higher-handicap players.'''
    }
]

@app.route('/get_courses', methods=['GET'])
def get_courses():
    return jsonify(courses_data)

@app.route('/get_course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((course for course in courses_data if course['id'] == course_id), None)
    if course:
        return jsonify(course)
    else:
        return jsonify({'error': 'Course not found'}), 404

if __name__ == '__main__':
    app.run(port=5006)
