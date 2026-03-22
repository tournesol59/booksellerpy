from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)
	
from werkzeug.exceptions import abort
from flaskr.db import get_db
from . import eBook

bp = Blueprint('book', __name__)
  
@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
		'SELECT b.id, title, author, categ, course_id, cs.intitule as intitule '
	    ' FROM books b JOIN course cs ON b.course_id = cs.id '
		' ORDER BY categ DESC '
    ).fetchall()
    return render_template('book/index.html')
		
@bp.route('/create', methods=('GET', 'POST'))
def create():
    if (request.method == 'POST'):
        title = request.form['title']
        author = request.form['author']
        categ = Categ(request.form['categ'])
        coursenaf = request.form['coursenaf']
        error = None
        message = ''
        course = None
        course_id = None
		
        if title == '':
            message = 'A title must be given as input'
        if author == '':
            message = 'An author name must be given'
        if (categ != 'OUVRAGE') or (categ != 'PROCEEDING'):
            message = 'A valid category must be given'
        else:
            if (categ == 'OUVRAGE'):
                categ_id = 1
            elif (categ == 'PROCEEDING'):
                categ_id = 2
		
        db=get_db()
        course = db.execute('SELECT id, codeNAF FROM course WHERE codeNA='+str(coursen)).fetchone();
        if (course == None):
            message = 'An existing course must be given'
        else:
            course_id = course['id']
				
        if (message != ''):
            flash(message)
        else:
            db.execute('INSERT INTO book(title, author, categ, course_id)'
                        'VALUES('+str(title)+','+str(author)+
						','+str(categ_id)+','+str(course_id)+')')
            db.commit()
		#return redirect(url_for('book.index')) #more indent on this line

    return render_template('book/create.html')
					  


