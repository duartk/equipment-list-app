from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    senha = db.Column(db.String(50))


class Equipment(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    partnumber = db.Column(db.String(50))
    description = db.Column(db.Text)
    family = db.Column(db.String(50))
    model = db.Column(db.String(50))
    config = db.Column(db.String(50))
    freq = db.Column(db.String(50))
    sbb = db.Column(db.String(50))


@app.route('/')
def index():
    return render_template('index.html', titulo='Relação de Equipamentos')

@app.route('/idu')
def idu():
    table = 'idu'
    lista = Equipment.query.filter_by(family='IDU').all()
    return render_template('lista_filter.html', titulo="IDU's", lista=lista, table=table)


@app.route('/odu')
def odu():
    table = 'odu'
    lista = Equipment.query.filter_by(family='ODU').all()
    return render_template('lista_filter.html', titulo="ODU's", lista=lista, table=table)


@app.route('/module')
def module():
    table = 'module'
    lista = Equipment.query.filter_by(family='MODULE').all()
    return render_template('lista_filter.html', titulo="AGS20L MODULE's", lista=lista, table=table)


@app.route('/sfp')
def sfp():
    table = 'sfp'
    lista = Equipment.query.filter_by(family='SFP').all()
    return render_template('lista_filter.html', titulo="SFP's", lista=lista, table=table)

@app.route('/coupler')
def coupler():
    table = 'coupler'
    lista = Equipment.query.filter_by(family='COUPLER').all()
    return render_template('lista_filter.html', titulo="COUPLER's", lista=lista, table=table)

@app.route('/polekit')
def polekit():
    table = 'polekit'
    lista = Equipment.query.filter_by(family='POLE KIT').all()
    return render_template('lista_filter.html', titulo="POLE KIT's", lista=lista, table=table)


if __name__ == '__main__':
    app.run(port=5006, debug=True)
