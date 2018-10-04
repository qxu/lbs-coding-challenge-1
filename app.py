from flask import Flask, render_template, jsonify
import json
from models import Meter, MeterData
from database import db_session

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/meters/')
def list_meters():
    meters = db_session.query(Meter).all()
    return render_template('meters.html', meters=meters)


@app.route('/meters/<int:meter_id>')
def list_meter_data(meter_id):
    meter_datas = db_session.query(MeterData).filter_by(meter_id=meter_id).order_by(MeterData.timestamp).all()
    return jsonify([data.to_json_dict() for data in meter_datas])
